from agency_swarm import Agent

ceo = Agent(
    name="CEO",
    description="Oversees financial planning and management.",
    instructions="instructions.md",
    tools=[],  # CEO does not interact with the database directly
    temperature=0.5
)
