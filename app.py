import streamlit as st
import pandas as pd
import requests

import os
from dotenv import load_dotenv
load_dotenv('.env')
OpenAI_key : str = os.getenv('OPENAI_API_KEY')

