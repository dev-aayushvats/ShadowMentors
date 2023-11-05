import requests
url = "https://simple-chatgpt-api.p.rapidapi.com/ask"

payload = { "question": '''give me one random best project idea in 30 words at maximum''' }

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c4b8776ebamsh80b3044b18a6d11p199a0ajsn94b4d47a35b1",
	"X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
