# Uso de Batches o lotes, 
# El problema es que si alguna de las instrucciones falla, entonces él continúa
# con el siguiente. VER TRANSACCIONES SI SE BUSCA QUE TODO SEA CORRECTO

# VENTAJA: speed up the process and reduce the number of write requests made to the service.

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

with table.batch_writer() as batch:
    
    batch.put_item(
        Item = {
            'usuario': 'Daniel7',
            'Apellido': 'Vivas6',
            'edad': 282,
            'cargo': 'Ingeniero civil2',
            'Universidades': ['andes2', 'unal2'],
        }
    )

    batch.put_item(
        Item = {
            'usuario': 'Daniel3',
            'Apellido': 'Vivas3',
            'edad': 23,
            'cargo': 'Ingeniero civil3',
            'Universidades': ['andes3', 'unal3'],
        }
    )

    batch.put_item(
        Item = {
            'usuario': 'Daniel4',
            'Apellido': 'Vivas4',
            'edad': 23,
            'cargo': 'Ingeniero civil3',
            'Universidades': ['andes3', 'unal3'],
        }
    )

    batch.delete_item(
        Key = {
            'usuario': 'Daniel3',
            'Apellido': 'Vivas3'
        }
    )