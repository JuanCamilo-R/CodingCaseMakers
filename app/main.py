from app.src.interface import create_interface
from app.src.recommendation_service import categorize_recommendations
from app.src.chatbot_service import chat, delete_chat

interface = create_interface(chat, delete_chat, categorize_recommendations)
interface.launch()