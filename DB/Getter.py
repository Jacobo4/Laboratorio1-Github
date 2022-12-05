import boto3

#GET TODOS los centros de events
#Get TODAS las fiestas
#GET UN centro de evento. Yo le mando el id del centro de eventos
#GET UNA fiesta. Yo le mando el id de la fiesta
#UPDATE los asistentes de un una fiesta. Yo le mando el id de la fiesta
#GET TODAS las fietas de un centro de eventos. Yo le mando el id del centro de eventos
#GET la info de estadisticas. EJE x, EJe y ojala en un array

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('event_center')
centros=[]
for i in range (100):
    response = table.get_item(Key={'event_center_id': i+1})
    centros.append(response['Item']['nombre_centro'])
print('Todos los centros de eventos:',centros)



