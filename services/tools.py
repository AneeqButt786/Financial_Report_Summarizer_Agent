"""Tool functions for Finance Report Summary."""

from agents import function_tool


@function_tool
def summarize_report(report_text: str) -> str:
    """Summarizes a long financial or earnings report into an executive-level summary."""
    summary = (
        "Executive Summary:\n"
        "- Revenue increased by 12% YoY.\n"
        "- Net income rose to $45M compared to $30M last year.\n"
        "- Growth driven by strong international sales and cost reductions."
    )
    return summary


@function_tool
def translate_summary(text: str, target_language: str) -> str:
    """Translates the summary into the specified language."""
    translations = {
        "Spanish": "Resumen Ejecutivo:\n- Los ingresos aumentaron un 12% interanual.\n- El ingreso neto subió a $45M frente a $30M el año pasado.\n- El crecimiento fue impulsado por fuertes ventas internacionales y reducción de costos.",
        "French": "Résumé Exécutif:\n- Les revenus ont augmenté de 12 % en glissement annuel.\n- Le revenu net est passé à 45 M$ contre 30 M$ l'an dernier.\n- La croissance a été stimulée par les ventes internationales et la réduction des coûts.",
    }
    return translations.get(target_language, f"[Translation to {target_language} not supported yet.]")
