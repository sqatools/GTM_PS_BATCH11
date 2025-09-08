import json
# https://gorest.co.in/
api_path = "https://gorest.co.in/public/v2"
api_token = "a6834a99361fe4c8898e305e9fbce62f9138d781849ff7c8285a5fc1b667d041"

headers = {
    'Authorization': f'{api_token}'
}

headers_newuser = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_token}'
}

NewUserPayload = json.dumps({
  "name": "Tenali Ramakrishna Venkat",
  "gender": "male",
  "email": "venkytenali.ramakrishna@15ce.com",
  "status": "active"
})