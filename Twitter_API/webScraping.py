
# Libraries

from configparser import ConfigParser
import tweepy

config = ConfigParser()
config.read('Laboratorio1-Github/Twitter API/config.ini')

try : 

    # Get the auth values
    api_key = config.get('twitter', 'api_key')
    api_key_secret = config.get('twitter','api_key_secret')
    access_token = config.get('twitter','access_token')
    access_token_secret = config.get('twitter','access_token_secret')
    
    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    print("Autentificación realizada con exito")


except:
    print("No se pudo realizar una autentificación del programa")
    exit()

client = tweepy.Client(consumer_key= api_key,consumer_secret = api_key_secret,access_token= access_token,access_token_secret= access_token_secret)
query = 'news'

tweets = client.search_recent_tweets(query='news', max_results=10)

for tweet in tweets.data:
    print(tweet.text)
