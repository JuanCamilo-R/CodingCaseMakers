import gradio as gr

# Define your chatbot function
def chatbot_response(message, chat_history):
    # Simulate a chatbot response (you can replace this with your actual chatbot logic)
    bot_message = f"🤖Makers Tech Bot: {message}"
    chat_history.append((message, bot_message))  # Append user and bot messages to the history
    return "", chat_history  # Clear the input box and update the chat history

# Custom Markdown for the interface
markdown_description = """
# **Makers Tech Pro Assistant**

 I’ll help you find the **best tech devices** suchlaptops, gadgets, and more—at the **best prices**. Just tell me what you need, and I’ll provide personalized recommendations, price comparisons, and exclusive deals. Let’s make tech shopping simple and stress-free!
"""

# Custom CSS for styling
custom_css = """
#chatbot {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

#user-input {
    background-color: #ffffff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
}

#send-button {
    background-color: #254384;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}

#send-button:hover {
    background-color: #45a049;
}

#clear-button {
    background-color: #254384;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}

#clear-button:hover {
    background-color: #e53935;
}

#title {
    color: #2c3e50;
    font-size: 60px;
    font-weight: bold;
    margin-bottom: 20px;
}

#description {
    color: #34495e;
    font-size: 24px;
    margin-bottom: 20px;
}
"""

# Create the Gradio interface
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown(markdown_description, elem_id="title")  # Add a title and description
    
    # Chat history display
    chatbot = gr.Chatbot(label="Chat History", height=400, elem_id="chatbot")  # Display chat history
    
    # Input and submit button
    with gr.Row():
        user_input = gr.Textbox(label="Your Message", placeholder="Type something...", scale=4, elem_id="user-input")  # Input textbox
        submit_button = gr.Button("Send", scale=1, elem_id="send-button")  # Submit button
    
    # Clear button
    clear_button = gr.Button("Clear Chat", elem_id="clear-button")  # Button to clear chat history
    
    # Define interactions
    submit_button.click(
        fn=chatbot_response,  # Function to call
        inputs=[user_input, chatbot],  # Inputs: user message and chat history
        outputs=[user_input, chatbot]  # Outputs: clear input and update chat history
    )
    
    # Clear chat history
    clear_button.click(
        fn=lambda: [],  # Clear the chat history
        inputs=None,
        outputs=chatbot
    )


# Launch the interface
demo.launch()