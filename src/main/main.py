from agent import Agent
from tickets_presenter import TicketsPresenter

def main():

    print("Welcome to Ticket Viewer")

    print("Type in 's' to sign in or 'q' to quit.")


    subdomain = input('Please input the subdomain name for your Zendesk agent account')
    email = input('Please input the email associated with your Zendesk agent account')
    pwd = input('Please input the password for your Zendesk agent account') 

    user_agent = Agent(subdomain = subdomain, email = email, pwd = pwd)
    user_agent.set_all_tickets()

    presenter = TicketsPresenter(user_agent)

    presenter.present_tickets()










if __name__ == '__main__':
    main()














