import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

# Creating a new item

# table.put_item(
#     Item={
#         'usuario': 'Daniel',
#         'Apellido': 'Vivas',
#         'edad': 26,
#         'cargo': 'Ingeniero civil',
#         'Universidades': ['andes', 'unal'],
#     }
# )

table.put_item( # Si corro un put_item varias veces reemplazará 
                # la antigua informaión con la nueva, por ejemplo si cambio
                # la edad
    Item={
        'usuario': 'Daniel',
        'Apellido': 'Vivas2',
        'edad': 28,
        'cargo': 'Ingeniero civil',
        'Universidades': ['andes', 'unal'],
    }
)

# table.put_item(
#     Item={
#         'usuario': 'Juan',
#         'Apellido': 'Vivas',
#         'edad': 29,
#         'cargo': 'Medico',
#         'Universidades': ['San martín', 'Sabana'],
#         'esposa': {
#             'nombre': 'Daniela',
#             'añosCasados': 2
#         }
#     }
# )

# Updating an item

table.update_item(
    Key = {
        'usuario': 'Daniel',
        'Apellido': 'Vivas'
    },
    UpdateExpression='SET edad = :val1',
    ExpressionAttributeValues={
        ':val1': 1000
    }
)

response = table.get_item(
    Key = {
        'usuario': 'Daniel',
        'Apellido': 'Vivas'
    }
)
item = response['Item']
print(item)

# Deleting an item

table.delete_item(
    Key = {
        'usuario': 'Daniel',
        'Apellido': 'Vivas2'
    }
)

