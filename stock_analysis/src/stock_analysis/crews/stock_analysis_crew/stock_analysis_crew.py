from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from src.config import ollama_llm, ollam_embedder
from src.stock_analysis.tools.stock_info_tool import StockInfoTool



# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class StockAnalysisCrew:
    """Stock Analysis Crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would lik to add tools to your crew, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def finra_stock_report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["finra_stock_report_writer"],
            llm=ollama_llm,
            tools=[StockInfoTool()]
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def write_finra_stock_report(self) -> Task:
        return Task(
            config=self.tasks_config["write_finra_stock_report"],
            llm=ollama_llm,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            verbose=True,
            planning_llm=ollama_llm,
            manager_llm=ollama_llm,
            share_crew=False,
            process=Process.sequential,
            # memory=True,
            # cache=True,
            embedder=ollam_embedder
        )
