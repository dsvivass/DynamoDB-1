import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users/Daniel6e')

print(table)

response = table.query(
    KeyConditionExpression = Key('usuario').eq('Juan')
)

items = response['Items']

print(items)

# También puedo escanear por otros atributos

response = table.scan(
    FilterExpression=Attr('edad').lt(30)
)
items = response['Items']
print(items)