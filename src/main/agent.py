from _typeshed import Self
import requests
from ticket import Ticket

class Agent:

    """

    Instance Attributes:
        -  _subdomain: String for the subdomain
    
    
    """

    _subdomain: str
    _email: str
    _pwd: str
    _tickets: list[Ticket]

    def __init__(self, subdomain: str = '', usr: str = '', pwd: str = '', ) -> None:
        self._subdomain = subdomain 
        self._usr = usr 
        self._pwd = pwd 


    def set_all_tickets(self) -> None:
         
        response = requests.get(self._url, auth=(self._email, self._pwd))
        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        tickets = data['tickets']

        for raw_ticket in tickets:
            ticket = self.json_to_ticket(raw_ticket)
            self._tickets.append(ticket)


    def json_to_ticket(self, raw_ticket: dict) -> Ticket:

        ticket = Ticket()
        ticket.set_ticket(raw_data=raw_ticket)

        return ticket




        




