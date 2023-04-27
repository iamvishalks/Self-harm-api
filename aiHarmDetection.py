import requests


def findResult(text):
    response = requests.post(
        'http://127.0.0.1:5000/harmDetection/', data={'text': text})
    return(f"\nHUMAN: {text} \n\nTHERAPIST: {response.text.strip()}")


def fullOutput(text):
    response = requests.post(
        'http://127.0.0.1:5000/harmDetection/fullOutput', data={'text': text})
    return response.json()

    