
from main.agent import Agent
from ticket import Ticket


class TicketsPresenter:

    """Manages the presentation of all tickets for a given agent
    """

    _agent: Agent

    def __init__(self, agent: Agent) -> None:
        self._agent = agent


    def print_ticket(self, ticket_index: int) -> None:
        ticket = self._agent._tickets[ticket_index]

        

    def present_all_tickets(self) -> None:
        # Check if the agent has less than 25 tickets
        if len(self._agent._tickets) <= 25:
            pass

        else:
            pass

    

     
         







