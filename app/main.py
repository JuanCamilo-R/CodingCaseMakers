from app.src.interface import create_interface
from app.src.recommendation_service import categorize_recommendations
from app.src.chatbot_service import chat, delete_chat

recommendations = categorize_recommendations(1)
interface = create_interface(chat, delete_chat, recommendations)
interface.launch()