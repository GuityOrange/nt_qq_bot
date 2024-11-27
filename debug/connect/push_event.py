import requests
from config.config_private import my_main_user_id

requests.post('http://localhost:3000/send_private_msg', json={
    'user_id': my_main_user_id,
    'message': [{
        'type': 'text',
        'data': {
            'text': 'Hello, World!'
        }
    }]
})