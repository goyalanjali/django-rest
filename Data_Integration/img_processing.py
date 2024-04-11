import json
import requests

url = ' '
image = ' '

res = requests.post(
    url,
    data = {
        'api_key': ' ',
        'recognizer': 'auto',
        'ref_no': ' '
    },
    files = {
        'file': open(image, 'rb')
    }
)

with open('response1.json','w') as f:
    json.dump(json.load(res.text), f)

with open('response1.json', 'r') as f:
    data = json.load(f)

print(data['receipts'][0].keys())        

items = data['receipts'][0]['items']

print(f"your purchase at {data['receipts'][0]['merchant_name']}")

for item in items:
    print(f"item['description] - {data['receipts'][0]['currency']} {item['amount']}")

print('-' * 30)
print(f"Subtotal: {data['receipts'][0]['currency']} {data['receipts'][0]['Subtotal']}")  
print(f"Tax: {data['receipts'][0]['currency']} {data['receipts'][0]['Tax']}")
print('-' * 30)
print(f"Total: {data['receipts'][0]['currency']} {data['receipts'][0]['Total']}")


# rb = reading bytes