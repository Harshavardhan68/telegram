import json
from flask import request


from outside_apis.openai_api import text_complition

def process_request(request: request) -> dict:
    '''
    Process the incoming data of the Telegram request

    Parameters:
        - request(falsk.request)

    Returns:
        - dict of these key and value 
        {
            'is_text': is_text,
            'is_chat_deleted': is_chat_deleted,
            'sender_id': sender_id,
            'message': message,
            'secret_token': secret_token,
            'first_name': first_name
        }
    '''
    
    body = request.get_json()
    headers = request.headers
    secret_token = headers['X-Telegram-Bot-Api-Secret-Token']

    message = ''
    is_bot = True
    is_text = False
    first_name = ''
    sender_id = None


    if 'message' in body.keys():
        sender_id = body['message']['from']['id']
        first_name = body['message']['from']['first_name']
        is_bot = body['message']['from']['is_bot']

        if 'text' in body['message'].keys():
            message += body['message']['text']
            is_text = True

    return {
        'is_text': is_text,
        'sender_id': sender_id,
        'message': message,
        'secret_token': secret_token,
        'first_name': first_name,
        'is_bot': is_bot
    }

def generate_response(message: str) -> str:
    '''
    Process the incoming message for different command and generate a response string

    Parameters:
        - message(str): incoming message from Telegram

    Returns:
        - str: formated response for the command
    '''
    if message == '/what is your name':
        return 'shiva sai'
    elif message == '/youtube':
        return 'You can watch my video tutorials here: https://youtube.com/@Harshavaardhann'
    elif message == '/website':
        return 'click here to visit my website https://www.smtart.ml/ '
    elif message == '/buyacoffee':
        return 'If you like my work please consider buying me a coffee here: https://www.buymeacoffee.com/Harshavardhann '
    elif message == '/imagechatbot':
        return 'It’s converts your descriptions into images. :-You can reach out by clicking here @Harshaimage_bot )'
    elif message == '/start':
        return 'Hello! Im a chatbot created by @K_Harshavardhan . How can I help you today?'
    else:
        result = text_complition(message)
        if result['status'] == 1:
            return result['response'].strip()
        else:
            return 'Sorry, I am out of service at this moment.'
