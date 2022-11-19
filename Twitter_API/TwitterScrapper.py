#Libraries
import tweepy
import configparser
import csv
import pandas as pd

def getUsers(): # Get the list of Users given in the DB
    doc = open("Laboratorio1-Github/data/UsersTwitter.txt","r")
    users = doc.readlines()
    users_list = []
    for i in users:
        users_list.append(i)
    print(users_list)
    return users_list

def configurateTokensKeys(): # Configuration for the tokens and keys given on Twitter
    
    config = configparser.RawConfigParser()
    config.read('Laboratorio1-Github/Twitter_API/config.ini') # Read the config doc with the Keys and tokens

    consumer_key = config["twitter"]["api_key"]
    consumer_secret = config['twitter']['api_key_secret']
    bear = config['twitter']['bear_token']
    access_token = config["twitter"]["access_token"]
    access_token_secret = config["twitter"]["access_token_secret"]
    
    return consumer_key, consumer_secret,access_token,access_token_secret,bear

def createDataFrame(users_doc):
        
    limit = 100

    for i in users_doc:
        query = i
        tweets = client.search_all_tweets(query=query,max_results=limit,tweet_mode="extended")
        
        # Print the tweets
        for tweet in tweets:
            print(tweet)

        # Create the Data Frame

        columns = ['User','Tweet']
        data = [] # Data of each tweet
        for tweet in tweets:
            data.append([tweet.user.screen_name,tweet.full_text])
        
        dataFrame = pd.DataFrame(data,columns = columns)
        return dataFrame

print(" <---- Start ----> ")

# Get the Keys and Tokens from Twitter
consumer_key, consumer_secret,access_token,access_token_secret,bear = configurateTokensKeys()

#       <--- IGNORE THIS --->
# I'm waiting for the update of Eureka account from Twitter. We need the Academic level to do the scrapper 

# We work with the Essential account for Twiiter Developers. So we use the API V2 and not the V1 that is only
# for the Academic Reseachers

# Configure the API with client for V.2

client = tweepy.Client(bearer_token = bear)

# Do the scrapping of the tweets for each user
users_doc = getUsers()

client = tweepy.Client(bear)

for username  in users_doc:
    
    query = "from:" + username

    # Get the last 100 tweets
    tweets = client.search_recent_tweets(query=query,
                                    tweet_fields = ["created_at", "text"],
                                    user_fields = ["name","username"],
                                    max_results = 100,
                                    expansions='author_id')

    # Create a csv with the data recolected

    try:
        rows = []
        for tweet in tweets.data:
            row = []
            row.append(tweet.created_at)
            row.append(tweet.text)
            row.append(tweet.author_id)
            rows.append(row)

        with open('Laboratorio1-Github/data/Tweets.csv','w',encoding="UTF8",newline = "" ) as file :
            writer = csv.writer(file)
            writer.writerows(str('Tweets obtenidos del usuario '+ username))
            writer.writerows(rows)
    except:
        print("No se pudo con " + username)


print("<-- Finished -->")
