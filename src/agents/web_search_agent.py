from langchain_community.tools import DuckDuckGoSearchRun


def web_search(query):
    search = DuckDuckGoSearchRun()

    return search.run(query)
