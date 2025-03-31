from agency_swarm import Agent
from tools.FinanceDBTool import FinanceDBTool

tracker = Agent(
    name="Tracker",
    description="Manages financial records using an SQLite database.",
    instructions="instructions.md",
    tools=[FinanceDBTool],
    temperature=0.2
)
