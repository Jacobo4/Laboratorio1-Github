"""Copiar esto linea  alinea en CMD diccionario

1.  msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi

2. aws configure

3.  AWS Access Key ID [****************EIAT]: AKIA23ZX6D4AH4ROEIAT
    AWS Secret Access Key [****************eTsY]: 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
    Default region name [None]: us-east-1    
    Default output format [None]: (enter)

    AHORA SI SE PUEDE CORRER EL PYTHON
"""


# Esto extrae la info en un diccionario de un determinado usuario 

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mirandaz')

def get(user):
    try:
        response = table.get_item(Key={'user': user})
    except:
        print('error')
        raise
    else:
        return response['Item']

print(get('echelecabeza'))


#Todos los eventos
#Todos los event center (fiestas) - vale chimba
#Todos los establecimientos
#actilaizar asistentes
#obtener un establecimiento (event center)
# fiestas de un establecimiento

