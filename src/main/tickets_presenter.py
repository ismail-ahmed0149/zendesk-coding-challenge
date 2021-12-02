
from main.agent import Agent
from ticket import Ticket


class TicketsPresenter:

    """Manages the presentation of all tickets for a given agent
    """

    _agent: Agent

    def __init__(self, agent: Agent) -> None:
        self._agent = agent


    def print_ticket(self, ticket: Ticket) -> None:
        """Format and print out what has been deemed the most
        salient pieces of data for the ticket
        """

        print(ticket['subject'] + " " + ticket['priority'] +  " " + ticket['requester_id'])

         
    def print_full_ticket(self, ticket: Ticket) -> None:
        """Print the full JSON object associated with this ticket

        """

        print(ticket)
        

    def present_tickets(self) -> None:
        # Check if the agent has less than 25 tickets

        stay_in_menu = True


        while stay_in_menu:
            if len(self._agent._tickets) <= 25:

                self.present_full_view()
                
            else:
                self.present_page_view()

            choice = input('If you want to stay, press "c" to continue or "q" to quit. ') 

            if choice == 'q':
                stay_in_menu = False
            
            

    def present_full_view(self) -> None:
        stay_in_menu = True


        for i in range(0, len(self._agent._tickets)):
                self.print_ticket(self._agent._tickets[i])
            
        while stay_in_menu:            

            index = input("Type the index of the ticket you would like a more detailed view of. If you want to view all tickets again, press 'v'. If you want to quit, press 'q'")

            if index == 'q':
                stay_in_menu = False
            elif index == 'v':
                for i in range(0, len(self._agent._tickets)):
                    self.print_ticket(self._agent._tickets[i])
            else:
                self.print_full_ticket(self._agent._tickets[int(index)])

    def present_page_view(self) -> None:

        stay_in_menu = True

        pages = []

        page = []

        # Separate all tickets into groups of 5 that user can page through


        for i in range(0, len(self._agent._tickets)):
            if i + 1 % 5 == 0 or i == len(self._agent._tickets) - 1:
                page.append(self._agent._tickets[i])
                pages.append(page)
                page = []
            else:
                page.append(self._agent._tickets[i])

        self.present_page(pages[0])
        print("1/5") 
        print()

        curr_page = page[0]

        while stay_in_menu:

            choice = input('If you want to switch to a different page, type the corresponding page number. If you would like to quit, type "q".')

            if choice == 'q':
                stay_in_menu = False
            else:
                curr_page = pages[int(choice) - 1]
                self.present_page(curr_page)




    def present_page(self, page: list[Ticket]) -> None:

        for ticket in page:
            self.print_ticket(ticket=ticket)

        

        

        

             

    

     
         







