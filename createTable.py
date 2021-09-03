import boto3 

# Create a client object
# session = boto3.Session(
#     aws_access_key_id = config('AccessKeyID'),
#     aws_secret_access_key = config('SecretAccessKey'),
#     # aws_session_token = config('')
# )

# Para la sesión descargué AWS CLI y corrí

    # aws configure      e ingresé todas las llaves que tiene el usuario de IAM

# Get the service resource
dynamodb = boto3.resource('dynamodb')

# Create a dynamoDB table
table = dynamodb.create_table(
    TableName = 'test2',
    KeySchema = [
        {
            'AttributeName': 'usuario',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Apellido',
            'KeyType': 'RANGE'
        }
    ],

    AttributeDefinitions = [
        {
            'AttributeName': 'usuario',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Apellido',
            'AttributeType': 'S'
        }
    ],

    ProvisionedThroughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)