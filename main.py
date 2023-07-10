import streamlit as st
import json
import random
# Load JSON data
with open('data/data.json') as file:
    data = json.load(file)
intents = data['intents']
# Set page configuration
st.set_page_config(page_title='FPTB-Chatbot', page_icon=':robot_face:')
st.sidebar.subheader('About')
st.sidebar.info('This is a chatbot created by Paul Edward.')

st.title('FPTB Chatbot')
st.image('images/user_avatar.jpeg', width=100)

# Main chatbot function
def chat():
    user_input = st.text_input('User:', '')

    if st.button('Send'):
        response = get_response(user_input)
        st.image('images/bot_avatar.png', width=100)

        st.text_area('Bot:', value=response, height=200)
        user_input = ""

def get_response(user_input):
    for intent in intents:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm sorry, I didn't understand that."
# Call the chat function to run the chatbot
chat()
