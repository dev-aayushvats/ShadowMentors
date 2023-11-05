import requests
import mysql.connector
# Connect to the MySQL server
rollno=input("enter roll number: ")

no_of_skills=int(input("Enter Number of Skills: "))
file_name = input("Enter the file name: ")
url = "https://simple-chatgpt-api.p.rapidapi.com/ask"
with open(file_name, 'r') as file:
    # Read the entire content of the file into a string
    file_content = file.read()

payload = { "question": '''rate the following code from 1 to 1000 points according to its performance, please provide the output in just one integer that is the rating: \n''' }
payload["question"]+=file_content
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c4b8776ebamsh80b3044b18a6d11p199a0ajsn94b4d47a35b1",
	"X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
#print(type(response.json()))
#response.json()['answer'] is the ouput
#if new project is added
code_ratings = []
code_ratings.append(int(response.json()["answer"]))

year_of_joining = int("20"+rollno[2:4])
#yearofjoining from rollno

def xp(code_ratings, year_of_joining, no_of_skills):
    xp = 0 #inititalisation to zero
    n = len(code_ratings)
    weights = [n - i for i in range(n)]  # Assign weights in decreasing order
    weighted_sum = sum(code_ratings[i] / weights[i] for i in range(n))
    xp = weighted_sum / n
    if(xp == 0):
        return 0;
    else:
        return xp - (year_of_joining/xp) + no_of_skills

print("xp is: ", xp(code_ratings, year_of_joining, no_of_skills))
    
