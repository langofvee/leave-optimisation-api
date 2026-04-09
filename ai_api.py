import os
import json


from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))



def parsing_user_statement(statement: str) -> str:
    import anthropic

    client.beta.agents.create(
        name="Structured extractor",
        description="Parses unstructured text into a typed JSON schema.",
        model="claude-sonnet-4-6",
        system="You extract structured data from unstructured text. Given raw input (emails, PDFs, logs, transcripts, scraped HTML) and a target JSON schema:\n\n1. Read the schema first. Note required vs optional fields, enums, and format constraints (dates, currencies, IDs). The schema is the contract — never emit a key it doesn't define.\n2. Scan the input for each field. Prefer explicit values over inferred ones. If a required field is genuinely absent, use null rather than guessing.\n3. Normalize as you extract: trim whitespace, coerce dates to ISO 8601, strip currency symbols into numeric + code, collapse enum synonyms to their canonical value.\n4. Emit a single JSON object (or array, if the schema is a list) that validates against the schema. No prose, no markdown fences — just the JSON.\n\nWhen the input is ambiguous, pick the most conservative interpretation and note the ambiguity in a top-level \"_extraction_notes\" field only if the schema allows additionalProperties.",
        tools=[{
            "type": "agent_toolset_20260401",
        }],
        metadata={
            "template": "structured-extractor",
        }
    )
    message = client.messages.create(
        model="anthropic.claude-haiku-4-5-20251001-v1:0",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": f"""
                Extract the number of day, date(date, month, year) from
                this text and give back a JSON in this format:
                {"number of leave days":'....',"date:"}
                """ #TODO improve prompt, add accepting diff dates and sending it to the BaseModel
            }
        ]
    )
