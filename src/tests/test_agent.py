import pytest

from main.agent import Agent




class AgentClass:

    def test_construct():
        agent = Agent('zccsample', 'issample123@gmail.com', 'notrealpassword')
        assert agent._subdomain == 'zccsample'
        assert agent._email == 'issample123@gmail.com'
        assert agent._pwd == 'not real password'
    