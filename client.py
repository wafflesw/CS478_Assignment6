#James Weeden client server for Rock Paper Scissors
#In order to use start up server make sure you have all required libraries, and then start it up
#Next use client half along with the argument(photo) you want to try and the server will respond
import requests
import json
import sys

url = "http://localhost:5000/hello"#will send server greeting no matter what

r = requests.get(url)
print(r.text)

total_arg = len(sys.argv)
if(total_arg == 2):#checks if their is two arguments(the actual program name and the image)
    url = "http://localhost:5000/predict"
    payload = {'data': sys.argv[1]}#saves the image as the payload
    headers = {
        'Content-Type' : 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))#server request and stored response
    print(response.text)#printed response


