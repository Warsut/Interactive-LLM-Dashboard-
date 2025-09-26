import streamlit as st
import ollama

#function to load the css styling
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#call the function to load the styling
load_css("Styling/style.css") 


MODEL = 'llama3.1:8b' #this is the model we are using

st.title("Hi, I'm Bob!")

st.sidebar.title("BOB A.I.")
with st.sidebar:
    st.markdown("What does this do?")
    st.button("+ New Chat")


#initializes the messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

#for all the messages we have in the session state --> display the message content
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])




def generate_response():
    response = ollama.chat(model=MODEL, stream=True, messages=st.session_state.messages) #will get the response from the model

    for chunk in response:
        token = chunk["message"]["content"] #token is getting the chunk content 
        st.session_state["full_message"] += token #adds to the full message so far
        yield token #display the token


if prompt:= st.chat_input("Type here"): #this text will show up in the input bar
    st.session_state.messages.append({"role": "user", "content": prompt}) #if the user types a prompt append it
    with st.chat_message("user", avatar="Assets/User_Icon.png"):
        st.markdown(prompt) #display prompt
    st.session_state['full_message'] = "" #defines a session state for the full message, empty at first as no request has yet been made
    with st.chat_message("assistant", avatar="Assets/smiley.jpg"):
        stream = generate_response()
        response = st.write_stream(stream) #write the stream response
        st.session_state.messages.append({'role': 'assistant', 'content': response}) #append assitant response into content



    file = st.file_uploader("Pick a file") #allows user to upload a file ..... this doesn't work yet, you can submit a file, but nothing happens
