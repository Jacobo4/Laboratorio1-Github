import boto3
dynamodb = boto3.resource('dynamodb')

#--------------GET TODOS los centros de events--------------

table = dynamodb.Table('event_center')
centros=[]
for i in range (100):
    response = table.get_item(Key={'event_center_id': i+1})
    centros.append(response['Item']['nombre_centro'])
print('Todos los centros de eventos:',centros)




#--------------Get TODAS las fiestas--------------
table = dynamodb.Table('fiesta')
fiestas=[]
for i in range (100):
    response = table.get_item(Key={'party_id': i+1})
    fiestas.append(response['Item']['party_name'])
print('Todos las fiestas:',fiestas)



#--------------GET UN centro de evento. Yo le mando el id del centro de eventos--------------

id_centro = int(input())
table = dynamodb.Table('event_center')
response = table.get_item(Key={'event_center_id':id_centro})
centro_event = response['Item']['nombre_centro']
print(centro_event)


#--------------GET UNA fiesta. Yo le mando el id de la fiesta--------------

id_fiesta = int(input())
table = dynamodb.Table('fiesta')
response = table.get_item(Key={'party_id':id_fiesta})
fiesta = response['Item']['party_name']
print(fiesta)


#--------------UPDATE los asistentes de un una fiesta. Yo le mando el id de la fiesta--------------



#--------------GET TODAS las fietas de un centro de eventos. Yo le mando el id del centro de eventos--------------




#--------------GET la info de estadisticas. EJE x, EJe y ojala en un array--------------

