import os
import openai
import datetime
import requests
import wikipedia
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel, Field
from typing import List

from langchain.tools import tool
from langchain.prompts import PromptTemplate,MessagesPlaceholder
from langchain.tools.render import format_tool_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.schema.runnable import RunnablePassthrough
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
import panel as pn
import param
from langchain_community.chat_models import ChatOpenAI