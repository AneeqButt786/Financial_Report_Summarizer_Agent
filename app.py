"""Finance Report Summary and Localization - Chainlit App. Run with: chainlit run app.py"""

import chainlit as cl
from agents import Runner, set_default_openai_key

from config import get_config
from agent_defs import triage_agent
from utils.logging import get_logger

logger = get_logger(__name__)


def _ensure_config():
    cfg = get_config()
    set_default_openai_key(cfg["openai_api_key"])
    return cfg


@cl.on_chat_start
async def on_chat_start():
    try:
        _ensure_config()
        await cl.Message(
            content="""**Finance Report Summary & Localization**

I provide intelligent financial report analysis and multilingual capabilities:
- **Summarization** - Executive-level summaries of financial reports
- **Translation** - Instant translation into Spanish, French, etc.

Paste a financial report to summarize, or ask to translate a summary.""",
            author="Finance Assistant",
        ).send()
    except ValueError as e:
        await cl.Message(content=f"**Configuration Error:** {e}", author="System").send()
        raise


@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content.strip()
    if not user_input:
        await cl.Message(content="Please provide a financial report or translation request.", author="Finance Assistant").send()
        return
    status_msg = await cl.Message(content="Processing...", author="Finance Assistant").send()
    try:
        _ensure_config()
        logger.info("Processing: %s", user_input[:80])
        result = await Runner.run(triage_agent, user_input)
        await status_msg.remove()
        await cl.Message(content=f"## Result\n\n{result.final_output}", author="Finance Assistant").send()
        logger.info("Request processed successfully")
    except Exception:
        logger.exception("Request failed")
        await status_msg.remove()
        await cl.Message(content="Something went wrong. Please try again.", author="Finance Assistant").send()
