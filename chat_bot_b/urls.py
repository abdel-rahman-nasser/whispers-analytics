from django import views
from django.urls import path
from . import views

urlpatterns = [
    path(
        'create-new-chatbot/',
        views.create_new_chatbot,
        name="create_new_chatbot"
    ),
    path(
        'chatbots-list/',
        views.chatbots_list,
        name="chatbots_list"
    ),
    # path(
    #     'activate-bot/',
    #     views.activate_bot,
    #     name="activate_bot"
    # ),
    path(
        'delete-bot/',
        views.delete_chatbot,
        name="delete_chatbot"
    ),
    path(
        'get-bot-response/',
        views.get_bot_response,
        name="get_bot_response"
    ),
    path('test/', views.chat_test, name="chat_test"),
]
