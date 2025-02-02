import gradio as gr
from app.src.chatbot_service import chat
import functools

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

#recommended-products {
    background-color: #f9f9f9;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-left: 20px;
}
"""

def create_interface(chat_fn, clear_fn, products: dict):
    # Create the Gradio interface
    with gr.Blocks(css=custom_css) as demo:
        gr.Markdown(markdown_description, elem_id="title")  # Add a title and description

        with gr.Row():
            # Chat history display
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(label="Chat History", height=800, elem_id="chatbot")  # Display chat history
                chat_fn_with_args = functools.partial(chat_fn, chat_id="1452")
                gr.ChatInterface(fn=chat_fn_with_args, type="messages", chatbot=chatbot)
                # Clear button
                clear_button = gr.Button("Clear Chat", elem_id="clear-button")  # Button to clear chat history

           # Recommended products column
            with gr.Column(scale=1, elem_id="recommended-products"):
                # Dropdown for selecting categories
                category_dropdown = gr.Dropdown(
                    choices=["Highly Recommended", "Recommended", "Not Recommended"],  # Dropdown options
                    label="Select Category",  # Dropdown label
                    value="Highly Recommended",  # Default selected value
                    elem_id="category-dropdown"
                )
                
                # Output area to display products based on the selected category
                product_display = gr.Markdown(elem_id="product-display")
                
                # Function to update the product display based on the selected category
                def update_product_display(category):
                    product_list = products.get(category, [])
                    display_text = f"## 🛍️ *{category}*\n\n"  # Category heading with an icon
                    for product in product_list:
                        display_text += (
                            f"#### 🔹 *{product['name']}* - *${product['price']}*\n\n"
                            f"{product['description']}\n\n"
                            f"#### 📦 *In Stock:* {product.get('stock', 'Not found')}\n\n"
                            f"---\n"
                        )
                    return display_text.strip()
                
                # Update the product display when the dropdown value changes
                category_dropdown.change(
                    fn=update_product_display,  # Function to call
                    inputs=category_dropdown,  # Input: selected category
                    outputs=product_display  # Output: updated product display
                )
                
                # Initialize the product display with the default category
                demo.load(
                    fn=update_product_display,  # Function to call
                    inputs=category_dropdown,  # Input: default category
                    outputs=product_display  # Output: updated product display
                )
            
        clear_fn_with_chat_id = functools.partial(clear_fn, chat_id="1452")
        # Clear chat history
        clear_button.click(
            fn=clear_fn_with_chat_id,  # Clear the chat history
            inputs=None,
            outputs=chatbot
        )
        return demo