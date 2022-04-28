
import requests
import json
# from rest_framework.renderers import JSONRenderer
URL ="http://127.0.0.1:8000/resumeapi/"


with open(r"C:\Projects\Resume\Resume_Parser\output\Alice Clark CV.txt", 'r') as f:   
    data = f.read()

# data = JSONRenderer().render(data)
data=data.replace('\n',' ')
data = { 'text' : data}
# print(type(data))


#insert data
def post_data():
    global data
    json_data = json.dumps(data)
    r = requests.post(url=URL, data = json_data)
    data = r.json()
    print(data)
post_data()
