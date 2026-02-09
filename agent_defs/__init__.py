"""Agent definitions for Finance Report Summary."""

from agents import Agent

from services.tools import summarize_report, translate_summary

financial_agent = Agent(
    name="Financial Summary Agent",
    instructions="You are a financial summarization expert. When given a financial report, extract key points and turn them into a brief, executive-level summary.",
    tools=[summarize_report],
    model="gpt-4o-mini",
)

localization_agent = Agent(
    name="Localization Agent",
    instructions="You are a translation and localization expert. Translate any English content into the user-specified language clearly and professionally.",
    tools=[translate_summary],
    model="gpt-4o-mini",
)

triage_agent = Agent(
    name="Finance Assistant",
    instructions="If the user asks for a financial report to be summarized, hand off to Financial Summary Agent. If the user asks for a summary to be translated, hand off to the Localization Agent.",
    handoffs=[financial_agent, localization_agent],
    model="gpt-4o-mini",
)
