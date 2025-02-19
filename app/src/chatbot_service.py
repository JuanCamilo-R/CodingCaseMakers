from app.src.models import llm
from app.src.data import products
from app.src.utils import read_prompt_file, replace_placeholders, format_products

from typing import AsyncGenerator, List
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# Load system prompt once to avoid redundant file reads
SYSTEM_PROMPT = read_prompt_file("app/prompts/system.prompt.md")

# Initialize workflow
workflow = StateGraph(state_schema=MessagesState)

async def call_model(state: MessagesState) -> dict:
    """
    Calls the LLM model with a formatted system prompt and user messages.
    
    Args:
        state (MessagesState): The state containing user messages.
    
    Returns:
        dict: The updated message state with LLM response.
    """
    formatted_products = format_products(products)
    system_prompt_filled = replace_placeholders(SYSTEM_PROMPT, context=formatted_products)
    
    messages = [
        SystemMessage(content=system_prompt_filled),
        *state["messages"]
    ]
    
    response = await llm.ainvoke(messages)
    return {"messages": response}

# Define the workflow graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Memory checkpointing
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

async def chat_from_console():
    config = {"configurable": {"thread_id": "abc123"}}
    while True:
        query = input("You: ")  # Get user input
        if query.lower() == "exit":
            print("Exiting chat...")
            break  # Exit the loop

        input_messages = [HumanMessage(query)] 

        async for msg, _ in app.astream(
            {"messages": input_messages}, config,
            stream_mode="messages",
        ):
            if msg.content:
                print(msg.content, end="", flush=True)
        print()

async def chat(message: str, chat_history: List[str], chat_id: str) -> AsyncGenerator[str, None]:
    """
    Handles the chat interaction asynchronously.
    
    Args:
        message (str): User input message.
        chat_history (List[str]): List of previous chat messages.
    
    Yields:
        str: Streamed response from the model.
    """
    CONFIG = {"configurable": {"thread_id": chat_id}}
    input_messages = [HumanMessage(content=message)]
    response = ""

    async for msg, _ in app.astream({"messages": input_messages}, CONFIG, stream_mode="messages"):
        if msg.content:
            response += msg.content
            yield response

def delete_chat(chat_id):
    CONFIG = {"configurable": {"thread_id": chat_id}}
    app.update_state(CONFIG, {"messages": []})
