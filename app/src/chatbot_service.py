from app.src.models import llm
from app.src.data import products
from app.src.utils import read_prompt_file, replace_placeholders, format_products
import asyncio

from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

system_prompt = read_prompt_file("app/prompts/system.prompt.md")

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)

# Define the function that calls the model
async def call_model(state: MessagesState):
    formatted_products = format_products(products)
    system_prompt_filled = replace_placeholders(system_prompt,
                                                context=formatted_products)
    messages = [
        SystemMessage(content=system_prompt_filled),
        *state["messages"]
    ]
    response = await llm.ainvoke(messages)
    return {"messages": response}

# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}

async def chat():
    while True:
        query = input("You: ")  # Get user input
        if query.lower() == "exit":
            print("Exiting chat...")
            break  # Exit the loop

        input_messages = [HumanMessage(query)] 

        async for msg, metadata in app.astream(
            {"messages": input_messages}, config,
            stream_mode="messages",
        ):
            if msg.content:
                print(msg.content, end="", flush=True)
        print()

asyncio.run(chat())