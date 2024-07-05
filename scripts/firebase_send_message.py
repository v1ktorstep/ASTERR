import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

# Initialize the Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate('service_account.json')
    firebase_admin.initialize_app(cred)

# Define the message
message = messaging.Message(
    data={
        'payload': b,
    },
    token=a
)

# Send the message
response = messaging.send(message)

print('Successfully sent message:', response)