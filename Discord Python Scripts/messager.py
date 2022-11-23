import requests
import time
import json

channel = int(input("Channel To Send Message in (channel_id): "))

def get_reply():
    while True:
        reply_input = input("Reply? (True/False): ")
        match reply_input:
            case "True":
                return True
            case "False":
                return False
            case _:
                print("Incorrect value, please enter either True or False")

def get_manual():
    while True:
        manual_input = input("Manual message input? (True/False): ")
        match manual_input:
            case "True":
                return True
            case "False":
                return False
            case _:
                print("Incorrect value, please enter either True or False")

def get_all():
    while True:
        all_input = input("All? (True/False): ")
        match all_input:
            case "True":
                return True
            case "False":
                return False
            case _:
                print("Incorrect value, please enter either True or False")

def get_messages_to_respond():
    messages_temp = []
    while True:
        message_input = input("Add messages to react to (Stop/message_id): ")
        if (message_input == "Stop"):
            break
        else:
            messages_temp.append(message_input)
    return messages_temp  

reply = get_reply()
manual = get_manual()
if (reply == True) and (manual == False):
    all = get_all()
elif (reply == True) and (manual == True):
    messages_to_respond = get_messages_to_respond()
message_text_to_send = input("Message To Send: ")
delay = float(input("Delay in Seconds: "))
repititions = int(input("How many times should it message: "))

headers = json.load(open('auth.json', 'r'))

if (reply):
    if (all) and (manual == False):
        def send_message(channelid: str, message: str, delay: float):
            r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
            jsonn = json.loads(r.text)
            reply_messages = []
            for i in jsonn:
                reply_messages.append(i['id'])
            for reply_message in reply_messages:
                time.sleep(delay)
                payload = {
                    'content': message,
                    'message_reference': {
                        'message_id': reply_message
                    }
                }
                requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', json=payload, headers=headers)
            print("messaged")
    elif (manual):
        def send_message(channelid: str, message: str, delay: float):
            time.sleep(delay)
            for message_to_respond in messages_to_respond:
                payload = {
                    'content': message,
                    'message_reference': {
                        'message_id': message_to_respond
                    }
                }
                requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', json=payload, headers=headers)
            print("messaged")
    else:
        def send_message(channelid: str, message: str, delay: float):
            r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
            jsonn = json.loads(r.text)
            time.sleep(delay)
            payload = {
                'content': message,
                'message_reference': {
                    'message_id': jsonn[0]['id']
                }
            }
            requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', json=payload, headers=headers)
            print("messaged")
else:
    def send_message(channelid: str, message: str, delay: float):
        time.sleep(delay)
        payload = {
            'content': message
        }
        requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', json=payload, headers=headers)
        print("messaged")

for i in range(repititions):
    send_message(channel, message_text_to_send, delay)