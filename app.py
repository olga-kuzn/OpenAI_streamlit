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

# richiesta = st.text_input('inserisci richiesta ')
# completion = client.chat.completions.create(
#                                             model=MODEL,
#                                             messages=[
#                                                 {"role": "system", "content": "Sei un assistente per lo studio. Cortesemente aiutami con i compiti"},
#                                                 {"role": "user", "content": richiesta}
#                                             ]
#                                             )

# st.write("Assistente: " + completion.choices[0].message.content)

# 1. Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# 2. Form to handle user submission smoothly
with st.form("my_form", clear_on_submit=True):
    user_input = st.text_input("La vostra richiesta:")
    submitted = st.form_submit_button("Submit")

# 3. Process and append to history on submit
if submitted and user_input:
    # Generate your output (e.g., uppercase transformation, AI response, calculation)
    completion = client.chat.completions.create(
                                            model=MODEL,
                                            messages=[
                                                {"role": "system", "content": "Sei un assistente per lo studio. Cortesemente aiutami con i compiti"},
                                                {"role": "user", "content": user_input}
                                            ]
                                            )

    generated_output = completion.choices[0].message.content
    st.write(generated_output)
    
    # Save both input and output as a pair
    st.session_state.history.append({
        "input": user_input,
        "output": generated_output
    })

# 4. Display the history log
st.subheader("History Log")
for index, item in enumerate(reversed(st.session_state.history)):
    st.markdown(f"**Entry #{len(st.session_state.history) - index}**")
    st.write(f"👉 **Input:** {item['input']}")
    st.write(f"✅ **Output:** {item['output']}")
    st.divider()
