import requests

def sumRequest(n1,n2):
    payload = {'n1': n1,'n2': n2}
    r = requests.post("https://kodak-dev-sneed722.c9users.io:8081/api/v1/sum",data=payload)
    return r.json()
    #return calc
    
x = sumRequest(11,5)
resu = x['result']

html_str = '<html><body>' + str(resu) + '</body></html>'

file = open('index.html','w')
file.write(html_str)