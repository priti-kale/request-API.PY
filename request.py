
import requests
import json 
from pprint import pprint
f=requests.get("http://join.navgurukul.org/api/partners")
s=json.loads(f.text)
with open("partener.json","w") as l:
    json.dump(s,l,indent=2)
l=[]
for i in s:
    for j in s[i]:
        l.append(j["id"])
list1=[]
def ascending():
    # list1=[]
    l.sort()
    for i in l:
        for j in s:
            for k in s[j]:
                for p in k:
                    # print((p))
                    if p=="id":
                        if i==k[p]:
                            list1.append(k)
    with open("new.json","w") as f:
        json.dump(list1,f,indent=4)


def desending():
    l.sort(reverse=True)
    # print(l)
    for i in l:
        for j in s:
            for k in s[j]:
                for p in k:
                    if p=="id":
                        if i==k[p]:
                            list1.append(k)
                                  
    with open("new.json","w") as f:
        json.dump(list1,f,indent=4)
def user():
    user=input("enter the your choice ascending [A] or desending [D] :-")
    if user=="A":
        ascending()
    elif user=="D":
        desending()
    else:
        print("enter the valid choice:-")
        user()    
user()                                      
                        