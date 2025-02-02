import gradio as gr
from app.src.chatbot_service import chat

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

def create_interface(chat_fn):
    # Create the Gradio interface
    with gr.Blocks(css=custom_css) as demo:
        gr.Markdown(markdown_description, elem_id="title")  # Add a title and description
        
        # Chat history display
        chatbot = gr.Chatbot(label="Chat History", height=800, elem_id="chatbot")  # Display chat history
        
        gr.ChatInterface(fn=chat_fn, type="messages", chatbot=chatbot)
        
        # Clear button
        clear_button = gr.Button("Clear Chat", elem_id="clear-button")  # Button to clear chat history
        
        # Clear chat history
        clear_button.click(
            fn=lambda: [],  # Clear the chat history
            inputs=None,
            outputs=chatbot
        )
        return demo