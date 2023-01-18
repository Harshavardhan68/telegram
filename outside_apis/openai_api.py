TOKEN="5833201640:AAFsPC9V_ReaSZ3KPtqrNPgVW4Zd28R0XLc"
HEADER_TOKEN="Harshavardhan"
OPENAI_API_KEY="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"
ME="1411294375"


import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Human: {prompt}\nAI: ',
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
        
