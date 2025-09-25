import streamlit as st
import ollama


MODEL = 'llama3.1:8b' #this is the model we are using

st.title("Hi, I'm Bob!")


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
    with st.chat_message("user"):
        st.markdown(prompt) #display prompt
    st.session_state['full_message'] = "" #defines a session state for the full message, empty at first as no request has yet been made
    with st.chat_message("assistant"):
        stream = generate_response()
        response = st.write_stream(stream) #write the stream response
        st.session_state.messages.append({'role': 'assistant', 'content': response}) #append assitant response into content



