import requests
import json
import sys
import time
import itertools
import threading
from termcolor import colored


def animation(stop_event):
    while not stop_event.is_set():
        for x in itertools.cycle(["--", "//", "||", "\\"]):
            sys.stdout.write("\r" + x)
            sys.stdout.flush()
            time.sleep(0.1)


def get_key():
    with open("simple_chatgpt\key.json")as json_data:
        config = json.load(json_data)
        return config["api_key"]


def main():

    print(colored("What do you want to know?: ", "green"))
    question = input("")
    print("")

    if question == "q":
        print("Goodbye")

    else:

        stop_event = threading.Event()

        thread = threading.Thread(target=animation, args=(stop_event, ))
        thread.start()

        url = "https://simple-chatgpt-api.p.rapidapi.com/ask"
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": get_key(),
            "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
        }

        payload = {"question": question}

        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()

        stop_event.set()

        sys.stdout.write("\r")
        sys.stdout.flush()

        print(response_data["answer"])
        print(colored("=" * 200, "red"))
        print("")
        main()


if __name__ == "__main__":
    main()
