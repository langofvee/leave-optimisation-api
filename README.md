
# Leave Optimisation API

A FastAPI application that helps users find optimal periods to take leave by combining their planned leave dates with public holidays and applying leave-optimisation logic.

## Overview

The application accepts:

* Number of leaves available
* Dates on which leave can be taken
* Whether Saturdays should be considered
* Whether Sundays should be considered
* Whether sandwich leaves should be considered
* Calendarific holiday information

It then combines the user's leave information with public holidays and uses optimisation logic to identify useful leave combinations.

## Project Structure

```text
leave-optimisation-api/
│
├── app/
│   └── main.py
│
├── schemas/
│   └── models.py
│
├── services/
│   ├── calendarific.py
│   ├── combinedLeaves.py
│   ├── creatingBinaryArray.py
│   └── slidingWindowLogic.py
│
├── config/
├── utils/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Components

**`app/main.py`**

Contains the FastAPI application and API endpoints.

**`schemas/models.py`**

Contains the Pydantic models used to validate API input and structure API output.

**`services/calendarific.py`**

Handles requests to the Calendarific API to retrieve public holidays.

**`services/combinedLeaves.py`**

Combines user-provided leave dates with public holiday dates.

**`services/creatingBinaryArray.py`**

Converts the combined dates into a binary representation used by the optimisation logic.

**`services/slidingWindowLogic.py`**

Contains the main leave optimisation algorithm.

## System Flow

```text
Client
   ↓
FastAPI API
   ↓
Validate input with Pydantic
   ↓
Retrieve public holidays
   ↓
Combine holidays + leave dates
   ↓
Create binary representation
   ↓
Apply sliding-window optimisation
   ↓
Return optimised leave plan
```

## API

### `GET /`

Basic health check for the application.

Example response:

```json
{
  "message": "So we're building a Leave Optimisation API"
}
```

### `POST /optimiseLeaves`

Accepts leave information and calendar/holiday information and processes them using the leave optimisation logic.

The endpoint validates that:

```text
number of leave dates == number of leaves
```

If they do not match, the API returns a `400` error.

## Technologies

* Python
* FastAPI
* Pydantic
* Uvicorn
* HTTPX
* python-dotenv
* Calendarific API

## Setup

Clone the repository and create a virtual environment:

```bash
python -m venv env
```

Activate it on Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
CALENDARIFIC_API_KEY=your_api_key
```

Do not commit `.env` to Git.

## Running the Application

From the project root:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Current Development

This project is being developed incrementally, with the optimisation algorithm and external API integrations being built and tested as separate components.
