import requests
import time

token = '981262545:AAGGFMJ_7i8lg_wCRuYQGCozJmxoRhAec10'
api = 'https://api.telegram.org/bot981262545:AAGGFMJ_7i8lg_wCRuYQGCozJmxoRhAec10/'


def get_updates(req):
    param = {'timeout': 100, 'offset': 'none'}
    res = requests.get(req + 'getUpdates', data = param)
    return res.json()


def last_update(data):
    results = data['result']
    last = len(results) - 1
    return results[last]


def get_chat_id(data):
    chat_id = data['message']['chat']['id']
    return chat_id


def send_message(id, text):
    param = {'chat_id': id, 'text': text}
    res = requests.post(api + 'sendMessage', data = param).json()
    return res


def text_msg(data):
    msg = data['message']['text']
    switcher = {
        'hi': 'hi my friend!',
        'hello': 'hello my friend!',
        'how are you?': 'thanks, fine! you?'
    }
    res_text = switcher.get(msg, 'what do you say?')
    return res_text


def main():
    print('Listening...')
    update_id = last_update(get_updates(api))['update_id'] + 1
    while True:
        if update_id == last_update(get_updates(api))['update_id']:

            send_message(get_chat_id(last_update(get_updates(api))), text_msg(last_update(get_updates(api))))
            update_id+=1
    time.sleep(1)


if __name__ == '__main__':
    main()

