from typing import Dict
import requests

url = "http://0.0.0.0:21001/list_multimodal_models"

payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
print(response.text)


a = {'IEITYuan/Yuan2-2B-Janus-hf': '___003', 'IEITYuan/Yuan2-2B-hf': '___001', 'IEITYuan/Yuan2-51B-hf': '___002'}
b = sorted(a, key=lambda x: a.get(x, x))
print(b)

a: Dict[str, Dict]