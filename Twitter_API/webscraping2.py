
import requests
import os
import json
from configparser import RawConfigParser

config = RawConfigParser()
config.read('Laboratorio1-Github/Twitter API/config.ini')
BEARER_TOKEN = config.get('twitter','bear_token')


def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url():
    # Replace with Tweet ID below
    tweet_id = 20
    return "https://api.twitter.com/2/tweets/{}/quote_tweets".format(tweet_id)


def get_params():
    return {"tweet.fields": "created_at"}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    params = get_params()
    json_response = connect_to_endpoint(url, headers, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    print("inicio")
    main()
    print("fin")
