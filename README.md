# Telegram chat-bot
Hi everyone, this is repository for my personal demo project on connecting Telegram and OpenAI to provide answers to all the users questions using OpenAI GPT-3. This is written in `Python` and served with `Flask`. This bot can only handle:
* text messgaes
* it has a built-in menu options as well

You can interact with this bot [here](https://openinapp.co/23hsp?fbclid=PAAaYCbXvJnGrfMa75zVqWvgrdYXyn5_n5HNeXZUc_nFrxrUGoElWrM7kubCI).



### Youtube
I have recorded a quick video on the setup of this chat-bot, in case you want to replicate the work, you can watch it [here](https://youtu.be/pGuJNM_4F5g).

### What you will need
There are couple of things that you need before you get started following this repository.
* OpenAI API key, since it is open to all, you can create an account [here](https://openai.com/) and access the key.
* You need a telegram bot API key as well, you can get it with interacting with Botfather on Telegeram 
* API requesting application like Postman, Insomnia, etc.

### How to use it
To replicate the work of this repository and run it locally, you need to follow these steps:
* create a `.env` file inside the root directory, create these environmental variables:
    ```
    TOKEN=YOUR TELEGRAM BOT API KEY
    HEADER_TOKEN=A RANDOM STRING FOR SECURITY
    OPENAI_API_KEY=OPENAI API KEY
    ME=YOUR TELEGRAM ID
    
     ```
* create a virtual environment and activate it before installing the packages
* install all the required dependencies from the `requirements.txt` file
```python
pip install -r requirements.txt
```
* run the server with either of the following commands
```python
python run.py
```
```python
gunicorn run:app
```
* start NGROK engine on the same port as the python application is running.
* set the webhook by sendin a `POST` request on the following url
```python
http://localhost:5000/set-telegram-webhook
```
pass the following body with the request in `raw` `json` format    
```json
{
    "url": "YOUR NGRK URL/telegram",
    "secret_token": "HEADER_TOKEN DEFINED IN THE .env FILE"
}
```
* in case you want to set menu for the Telegram bot, you can send a `POST` request on the following url
```python
http://localhost:5000/set-telegram-menu-commands
```
pass the following body with the request in `raw` `json` format
```json
{
	"commands": [
		{
			"command": "/contactme",
			"description": "Contact me"
		},
		{
			"command": "/youtube",
			"description": "My youtube"
		}
	]
}
```
# About me
I am `Harshavardhan, I a student from ECE

* [YouTube](https://youtube.com/@Harshavaardhann)

