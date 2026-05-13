import streamlit as st
import pandas as pd
import requests

import os
from dotenv import load_dotenv
load_dotenv('.env')
OpenAI_key : str = os.getenv('OPENAI_API_KEY')

from openai import OpenAI

MODEL="gpt-4o-mini"
client = OpenAI()

richiesta = st.text_input('inserisci richiesta ')
completion = client.chat.completions.create(
                                            model=MODEL,
                                            messages=[
                                                {"role": "system", "content": "Sei un assistente per lo studio. Cortesemente aiutami con i compiti"},
                                                {"role": "user", "content": richiesta}
                                            ]
                                            )

st.write("Assistente: " + completion.choices[0].message.content)