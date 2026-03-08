from langchain_core.prompts import PromptTemplate
from src.config.llm_config import llm

prompt = PromptTemplate(
    input_variables=["db_data", "web_data"],
    template="""Analyze the following information and generate insights.

Database Data:
{db_data}

Web Data:
{web_data}

Provide a short summary and key insights
            """,
)

analysis_agent = prompt | llm


def run_analysis_agent(db_data, web_data):
    response = analysis_agent.invoke({
        "web_data": web_data,
        "db_data": db_data
    })
    return response.content
