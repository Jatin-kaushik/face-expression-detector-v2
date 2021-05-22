import json
import time
import requests
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')
img_str =  image_to_base64('Model/11.jpg')


api = "http://localhost:5002/face_detector"
header = {"Content-Type": "application/json"}
Input_json = {'img':img_str}
start_time = time.time()
r = requests.post(url= api, data=json.dumps(Input_json), headers= header)
end_time = time.time()
response = r.json()
print(response)
print("Time Taken: ", end_time-start_time)