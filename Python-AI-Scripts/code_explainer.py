import requests
url = "https://simple-chatgpt-api.p.rapidapi.com/ask"
file_name = input("Enter the file name: ")
with open(file_name, 'r') as file:
    # Read the entire content of the file into a string
    file_content = file.read()

payload = { "question": '''Please provide me with the stepwise explanation of the given code in not more than 70 lines: \n''' }
payload["question"]+=file_content
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c4b8776ebamsh80b3044b18a6d11p199a0ajsn94b4d47a35b1",
	"X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
#print(response.json())
output_string = response.json()["answer"]
with open('explanation.txt', 'w') as file:
    print(output_string, file=file)
