from langchain_community.agent_toolkits import create_sql_agent, SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from src.config.llm_config import llm
from dotenv import load_dotenv
import os
load_dotenv()


username = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST", "localhost")
port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DB", "unions")

uri = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(uri)
db = SQLDatabase(engine)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
sql_agent = create_sql_agent(llm, toolkit, verbose=False, top_k_tables=2, max_iterations=3)