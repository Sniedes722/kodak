import requests

x = 0
y = 100
a = 6
b = 7
while x <= y:
    payload = {'n1': a,'n2': b}
    r = requests.post("http://localhost/api/v1/sum",data=payload)
    print(r.json())
    a = a+b
    b = b+a
    x = x + 1
