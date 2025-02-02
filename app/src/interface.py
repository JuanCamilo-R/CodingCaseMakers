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

#user-dropdown {
    margin-bottom: 20px;
}
"""

def create_interface(chat_fn, clear_fn, products):
    # Create the Gradio interface

    users = {
        "User 1": 1,
        "User 2": 2,
        "User 3": 3
    }
    
    with gr.Blocks(css=custom_css) as demo:
        gr.Markdown(markdown_description, elem_id="title")  # Add a title and description

        user_dropdown = gr.Dropdown(
            choices=["User 1", "User 2", "User 3"],  # List of users
            label="Select User",  
            value="User 1",  # Default selected value
            elem_id="user-dropdown"  # ID for custom CSS
        )

        with gr.Row():
            # Chat history display
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(label="Chat History", height=800, elem_id="chatbot")  # Display chat history
                chat_fn_with_args = functools.partial(chat_fn, chat_id="1452")

                gr.ChatInterface(fn=chat_fn_with_args, type="messages", chatbot=chatbot)

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
                def update_product_display(category, user_value):
                    user_id = users[user_value]
                    product_list = products(user_id)
                    product_category = product_list.get(category)
                    display_text = f"## 🛍️ *{category}*\n\n"  # Category heading with an icon
                    for product in product_category:
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
                    inputs=[category_dropdown, user_dropdown],  # Input: selected category
                    outputs=product_display  # Output: updated product display
                )
                
                # Initialize the product display with the default category
                demo.load(
                    fn=update_product_display,  # Function to call
                    inputs=[category_dropdown, user_dropdown],  # Input: default category
                    outputs=product_display  # Output: updated product display
                )

        # Function to dynamically clear the chat with the selected user's chat_id
        def dynamic_clear_fn(user, category):
            if not user:
                return []
            user_id = users[user]
            clear_fn(chat_id=user_id)
            return [], update_product_display(category, user)

        # Attach clear function to dropdown change with dynamic user value
        user_dropdown.change(
            fn=dynamic_clear_fn,
            inputs=[user_dropdown, category_dropdown],  # Pass selected user value as chat_id
            outputs=[chatbot, product_display]  # Clears the chatbot when user changes
        )

        return demo