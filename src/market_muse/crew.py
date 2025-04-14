# from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def get_groq_llm(model="groq/deepseek-r1-distill-llama-70b"):
    return LLM(
        model=model,
        api_key=os.getenv("GROQ_API_KEY"),
    )

@CrewBase
class MarketingPostsCrew:
    """MarketingPosts crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def influencer_evaluation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["influencer_evaluation_agent"],
            tools=[SerperDevTool()],
            verbose=True,
            memory=False,
            llm=get_groq_llm(),
        )

    @agent
    def campaign_prediction_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["campaign_prediction_agent"],
            # tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            memory=False,
            llm=get_groq_llm(),
        )

    @agent
    def optimization_strategy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["optimization_strategy_agent"],
            verbose=True,
            memory=False,
            llm=get_groq_llm(),
        )
        
    @agent
    def chief_campaign_director(self) -> Agent:
        return Agent(
            config=self.agents_config["chief_campaign_director"],
            verbose=True,
            memory=False,
            llm=get_groq_llm(),
        )

    @task
    def influencer_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["influencer_research_task"], agent=self.influencer_evaluation_agent()
        )

    @task
    def campaign_prediction_task(self) -> Task:
        return Task(
            config=self.tasks_config["campaign_prediction_task"],
            agent=self.campaign_prediction_agent(),
        )

    @task
    def optimization_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["optimization_strategy_task"],
            agent=self.optimization_strategy_agent(),
        )

    # @task
    # def campaign_idea_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["campaign_idea_task"],
    #         agent=self.chief_campaign_director(),
    #     )

    @task
    def campaign_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config["campaign_summary_task"],
            agent=self.chief_campaign_director(),
            context=[self.optimization_strategy_task()],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarketingPosts crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            llm=get_groq_llm(),
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
