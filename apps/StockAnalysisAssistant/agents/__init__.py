from .technical_analysis_agent import TechnicalAnalysisAgent
from .fundamental_analysis_agent import FundamentalAnalysisAgent
from .decision_agent import DecisionAgent

class AgentManager:
    def __init__(self, llm_provider="local", max_retries=3, debug=False):
        self.agents = {
            "fundamental": FundamentalAnalysisAgent(llm_provider=llm_provider, max_retries=max_retries, debug=debug),
            "technical": TechnicalAnalysisAgent(llm_provider=llm_provider, max_retries=max_retries, debug=debug),
            "decision": DecisionAgent(llm_provider=llm_provider, max_retries=max_retries, debug=debug)
        }

    def get_agent(self, agent_name):
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Invalid agent name: {agent_name}")
        return agent