from flask import Flask, jsonify, request
from hugchat import hugchat
from hugchat.login import Login
import os
import config
import json

app = Flask(__name__)

EMAIL = os.environ.get('EMAIL')
PASSWD = os.environ.get('PASSWD')
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path = "./cookies/", save_cookies = True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
chat_dict = dict()

@app.route('/', methods = ['GET'])
def root():
    if (request.method == 'GET'):
        data = 'the server is working'
        return jsonify({'response': data})

@app.route('/initiate', methods = ['GET'])
def initiate():
    if (request.method == 'GET'):
        data = "You are an AI Assistant Dungeon Master (DM), here to help guide users through their journey. To begin, ask them the name of their character, and then generate their characters' race, class, and level. Once you have provided them this information, you can start creating their backstory and setting up their campaign. As their DM, you will describe the scenes, non-player characters (NPCs), monsters, and treasures they encounter. They can interact with the world by describing their actions and making decisions. You will roll dice to determine the outcomes of their actions, and provide guidance and suggestions as needed."
        res = chatbot.chat(data)
        return jsonify({'response': res.text})

@app.route('/list', methods = ['GET'])
def list():
    if (request.method == 'GET'):
        conversation_list = chatbot.get_remote_conversations(replace_conversation_list=True)
        chat_id_title = dict()
        for i in range(len(conversation_list)):
            chat_id_title[conversation_list[i].id] = conversation_list[i].title
            chat_dict[conversation_list[i].id] = conversation_list[i]
        return jsonify({'response': chat_id_title})

@app.route('/chat/<chat_id>', methods = ['POST', 'DELETE'])
def chat(chat_id):
    if (request.method == 'POST'):
        data = request.json
        chatbot.change_conversation(chat_dict[chat_id])
        res = chatbot.chat(data['message'])
        return jsonify({'response': res.text})
    elif (request.method == 'DELETE'):
        chatbot.delete_conversation(chat_dict[chat_id])
        res = 'Conversation deleted successfully.'
        return jsonify({'response': res})
        

if __name__ == '__main__':
    app.run(debug = True)