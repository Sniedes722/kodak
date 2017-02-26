import requests

x = 0
y = 10
a = 6
b = 7
while x <= y:
    payload = {'n1': a,'n2': b}
    r = requests.post("https://kodak-sneed722.c9users.io:8081/api/v1/sum",data=payload)
    print(r.json())
    x = x + 1
