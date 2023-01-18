
import sys
from sys import request


SERVICE1_URL = "http://service.example.com:8080"

message = request.get(sys.stdin.readline()).text
data = ["md5", message]

print(request.post(SERVICE1_URL, data="\n".join(data)))
