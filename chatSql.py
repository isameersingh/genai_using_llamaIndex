# importing the lib
import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor

load_dotenv(r"D:\Projects using langchain and Sql\dotenv.env")
class ChatWithSql:
    """ChatWithSql class is use for chat and query user question with the Sql database
    """
    def __init__(self,db_user,db_password,db_host,db_name):
        """This is an Constructor method of the ChatWithSql class
        """
        os.environ["OPENAI_API_KEY"] = "sk-xxxxxx"
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name
    
    def message(self,query):
        """message method will take the query from the user and process the result and return the response

        Args:
            query (String): this is the questions of the user
        Returns :
            response(String) : This is the reponse genrated by llms
        """
        # Intializing the llm
        llm = ChatOpenAI(model_name = "gpt-3.5-turbo")
        # connecting with db
        db = SQLDatabase.from_uri(f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}")
        # Intializing the toolkit
        toolkit = SQLDatabaseToolkit(db=db,llm=llm)
        # creatin the agent executor
        agen_executor = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True
        )
         
        response = agen_executor.run(query)
        return response

# obj = ChatWithSql("root","12345","localhost","ahi_database")
# print(obj.message("How many rows do we have in cattle table ?"))
