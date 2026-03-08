from src.agents.sql_agent import sql_agent
from src.agents.web_search_agent import web_search
from src.agents.analysis_agent import analysis_agent


def run_system(query):

    print("Running SQL agent...")
    db_result = sql_agent.invoke({"input": query})
    db_data = db_result["output"]

    print("SQL Result:", db_data)

    print("Running Web agent...")
    web_data = web_search(query)

    print("Web Result:", web_data)

    print("Running Analysis agent...")
    result = analysis_agent.invoke({
        "db_data": db_data,
        "web_data": web_data
    })

    return result.content


query_input = "Get Tesla revenue and latest news"

print("Starting system...")
print(run_system(query_input))