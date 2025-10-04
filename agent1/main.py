import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.team.team import Team
from agno.tools.reasoning import ReasoningTools

# -----------------------------
# Charger les variables d'environnement depuis .env
# -----------------------------
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("⚠️ Clé API Mistral manquante dans le fichier .env")

# -----------------------------
# Agent 1 : Analyse du ticket client
# -----------------------------
analyst_agent = Agent(
    name="Analyst Agent",
    role="Analyzes client issues and extracts the main problem.",
    model=MistralChat(id="mistral-medium", api_key=api_key),
    instructions=(
        "You are a support ticket analyst. "
        "Read the user's message and summarize the core issue in one short sentence. "
        "Do not provide any solution."
    )
)

# -----------------------------
# Agent 2 : Générateur de réponse
# -----------------------------
response_agent = Agent(
    name="Response Agent",
    role="Generates a professional and empathetic reply for the customer.",
    model=MistralChat(id="mistral-medium", api_key=api_key),
    instructions=(
        "You are a customer support representative. "
        "Write a clear, concise, and polite answer based on the issue identified by the analyst. "
        "Always be professional and friendly."
    )
)

# -----------------------------
# Team : Coordination des deux agents
# -----------------------------
support_team = Team(
    name="Support Client Team",
    model=MistralChat(id="mistral-medium", api_key=api_key),
    members=[analyst_agent, response_agent],
    tools=[ReasoningTools(add_instructions=True)],
    instructions=[
        "Collaborate to analyze the client's problem and provide a final, professional response.",
        "Use polite, natural language as if addressing a real customer.",
        "Output only the final answer from the Response Agent.",
    ],
    markdown=True,
    show_members_responses=True  # 🔍 Active cette ligne pour voir les échanges internes
)

# -----------------------------
# Exécution de la team
# -----------------------------
if __name__ == "__main__":
    support_team.print_response(
        "Je n'arrive pas à finaliser mon paiement sur le site.",
        stream=False,
        show_full_reasoning=False,
        stream_intermediate_steps=False,
    )
