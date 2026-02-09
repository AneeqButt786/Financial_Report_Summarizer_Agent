# Financial_Report_Summarizer_Agent# Finance Report Summary and Localization System

## Overview

An AI-powered system for intelligent financial report analysis and multilingual capabilities. It automatically generates executive-level summaries of financial reports and offers instant translation into multiple languages, making financial information accessible to global stakeholders.

## Features

- Executive-level financial report summarization
- Translation into Spanish, French (extensible)
- Multi-agent handoff (Finance Summary Agent, Localization Agent)
- Chainlit chat UI

## Tech Stack

- Python 3.12+
- OpenAI Agents SDK (openai-agents)
- Chainlit (chat UI)
- python-dotenv (environment variables)

## Setup

1. `cd Financial_Report_Summarizer_Agent`
2. `pip install -r requirements.txt` (or `uv sync`)
3. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`

## Run Commands

```bash
chainlit run app.py
```

## Example Use Cases

1. "Please summarize this financial report: [paste report text]"
2. "Can you translate the summary into Spanish?"
3. "Summarize and then translate to French"

## Folder Structure

```
Financial_Report_Summarizer_Agent/
├── app.py
├── config.py
├── agent_defs/__init__.py
├── services/
│   ├── __init__.py
│   └── tools.py
├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── logging.py
├── .env.example
├── README.md
└── requirements.txt
```
