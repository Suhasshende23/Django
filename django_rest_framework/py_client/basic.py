import requests


# endpoint="https://httpbin.org/anything/"
endpoint="http://127.0.0.1:8000/api/" 

get_response=requests.get(endpoint) #HTTp Request
# print(get_response.text)  #print raw text response code


# HTTP Request -> HTML
#REST API HTTP Request ->JSON
#Javascript Object Notation ~ Python Dict
print(get_response.json())
# print(get_response.status_code)
