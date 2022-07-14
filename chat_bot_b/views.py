import json
import string
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from chat_bot_b.classes.Chatbot import Chatbot
from django.views.decorators.csrf import csrf_exempt

from chat_bot_b.models import Chatbot_Model
from chat_bot_b.utils.string_to_folder_name import string_to_folder_name


def chat_test(request):
    if request.user.is_authenticated:
        return HttpResponse("Hello U Are In The ChatBot Test Section")
    else:
        return redirect("welcome")


def chatbots_list(request):
    if request.user.is_authenticated and request.method == "GET":
        bots = Chatbot_Model.objects.filter(owner=request.user)
        return render(request, 'chatbot-templates/list.html', {'bots': bots})
    else:
        return redirect("welcome")


def create_new_chatbot(request):
    if request.user.is_authenticated and request.method == "GET":
        return render(request, 'chatbot-templates/create.html')
    elif request.user.is_authenticated and request.method == "POST":
        # get request body data
        data = request.POST
        chatbot_name = data.get('chatbot_name')
        chatbot_name_as_folder = string_to_folder_name(chatbot_name)
        intents = []
        for i in range(int(data.get('number_of_rows'))):
            intent_name = data.get('topic_' + str(i + 1) + '_name')
            intent_pattern = data.get('topic_' + str(i + 1) + '_patterns')
            intent_response = data.get('topic_' + str(i + 1) + '_responses')
            intents.append({
                'tag': intent_name,
                'patterns': intent_pattern.splitlines(),
                'responses': intent_response.splitlines()
            })

        # create new chatbot
        Chatbot_Model(
            name=chatbot_name,
            intents=intents,
            owner=request.user
        ).save()

        # merging basic intents with user's intents
        with open('./intents.json') as file:
            data = json.load(file)
            data['intents'] = data['intents'] + intents

        # create new chatbot files
        chatbot = Chatbot(chatbot_name_as_folder, intents=data['intents'])
        chatbot.create_new_bot()
        # chatbot.load_and_start_chatbot()

        return render(request, 'chatbot-templates/create.html')
    else:
        return redirect("welcome")


@csrf_exempt
def delete_chatbot(request):
    if request.user.is_authenticated and request.method == "POST":
        bot_id = request.POST.get('bot_id')
        chatbot = Chatbot_Model.objects.get(id=bot_id)
        chatbot.delete()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failure'})


# @csrf_exempt
# def activate_bot(request):
# if request.method == "POST":
#     # loaded_bot = None
#     # get bot id
#     bot_id = request.POST.get('bot_id')
#     # get bot object
#     bot = Chatbot_Model.objects.get(id=bot_id)
#     # get bot name
#     bot_name = bot.name.strip()
#     # get bot name as folder
#     bot_name_as_folder = string_to_folder_name(bot_name)
#     # get bot intents
#     bot_intents = bot.intents

#     print(bot_name_as_folder)

#     loaded_bot = Chatbot(bot_name_as_folder, intents=bot_intents)
#     print(loaded_bot)

#     # loaded_bot.load_chatbot()
#     return HttpResponse("Bot Activated")

# else:
#     return redirect("welcome")


@csrf_exempt
def get_bot_response(request):
    if request.method == "POST":
        bot_id = request.POST.get('bot_id')
        user_text = request.POST.get('msg')

        bot = Chatbot_Model.objects.get(id=bot_id)
        bot_name = bot.name.strip()
        bot_name_as_folder = string_to_folder_name(bot_name)
        bot_intents = bot.intents

        with open('./intents.json') as file:
            data = json.load(file)
            data['intents'] = data['intents'] + bot_intents

        response = Chatbot.load_and_get_response(
            chatbot_name=bot_name_as_folder,
            user_input=user_text,
            intents=data['intents']
        )

        # return bot response as json
        return JsonResponse({
            'status': 'success',
            'response': response
        })

    else:
        return redirect("welcome")
