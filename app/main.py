from app.src.interface import create_interface
from app.src.chatbot_service import chat


interface = create_interface(chat)
interface.launch()