import boto3
import json


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('event_center')

records = ""

with open ('event_center.json','r') as datafile:
    records = json.load(datafile)

count = 0
for i in records:
    print(i)
    response = table.put_item(Item=i)
    count += 1

