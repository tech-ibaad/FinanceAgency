from agency_swarm import Agency
from agents.CEOAgent.CEOAgent import ceo
from agents.TrackerAgent.TrackerAgent import tracker

agency = Agency(
    [
        ceo,  # CEO is the main communicator with the user
        [ceo, tracker]  # CEO communicates with the Tracker agent
    ]
)

# Start the agency
agency.demo_gradio()
