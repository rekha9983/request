import os
import requests
import json
def course():
    from requests.api import options, request
    result=requests.get('https://saral.navgurukul.org/api/courses')
    data=result.json()
    courses=[]
    if os.path.exists("data.json")==True:
        file=open("data.json")
        x=json.load(file)
        l=x["availableCourses"]
        count=0
        print("MERAKI  COURSESS IS HERE :- ")
        print("")
        for i in  l:
            count=count+1
            courses.append(i["name"])
            print(count,".",i["name"],"-----",i["id"])
    else:
        f=open("data.json","w")
        y=json.dump(data,f,indent=4)
        f.close()
        file=open("data.json")
        x=json.load(file)
        l=x["availableCourses"]
        print("MERAKI  COURSESS IS HERE :- ")
        print("")
        count=0
        for i in  l:
            count=count+1
            courses.append(i["name"])
            print(count,".",i["name"],"------",i["id"])
    file=open("data.json")
    b=json.load(file)
    l=x["availableCourses"]
    c=1
    choose=int(input("CHOOSE YOUR COURSE SERIAL NUMBER.="))
    ex_number=0
    for j in range(len(l)):
        if j==(choose-1):     
            from requests.api import options, request
            result=requests.get("https://saral.navgurukul.org/api/courses/"+l[j]["id"]+"/exercises")
            
            data=result.json()
            if os.path.exists("exercise data.json")==True:
                file=open("exercise data.json")
                x=json.load(file)
                f=open("exercise data.json","w")
                y=json.dump(data,f,indent=4)
                f.close()
                file=open("exercise data.json")
                x=json.load(file)
                l=x["data"]

            else:
                f=open("exercise data.json","w")
                y=json.dump(data,f,indent=4)
                f.close()
                file=open("exercise data.json")
                x=json.load(file)
                l=x["data"]
            j=0
            v=1
            slug=[]
            while j<len(l):
                print(v,l[j]["name"])
                slug.append(l[j]["slug"])
                v=v+1
                j=j+1
            slugname=int(input("ENTER YOUR SLUG NUMBER ="))
            result=requests.get("http://saral.navgurukul.org/api/courses/"+ str(choose)+"/exercise/getBySlug?slug=" + slug[slugname-1])
            b=result.json()
            print("CONTENT",b["content"])
            print("....................")
            print(" ")
            print("ENTER 'U' FOR UP")
            print("ENTER 'N' FOR NEXT")
            print("ENTER 'P' FOR PREVIOUS")
            print("ENTER 'E' FOR EXIT ")
            options=input("NOW WHAT YOU WANT UP,NEXT,EXIT,PREVIOUS =")
            if options=="u":
                course()
            elif options=="n":
                result=requests.get("http://saral.navgurukul.org/api/courses/"+ str(choose)+"/exercise/getBySlug?slug=" + slug[slugname])
                b=result.json()
                print("CONTENT",b["content"])
                print("....................")
            elif options=="p":
                result=requests.get("http://saral.navgurukul.org/api/courses/"+ str(choose)+"/exercise/getBySlug?slug=" + slug[slugname-2])
                b=result.json()
                print("CONTENT",b["content"])
                print("....................")
            else:
                break
course()
again=input("IF YOU WANT SEE AGAIN COURSE DETAILS  CHOSSE 'Y' OTHERWISE CHOOSE  'N' FOR EXIT =")
if again=="y":
    course()
else:
    print("THANK YOU! NOW YOU ARE EXIT THIS CODE ")
    breakpoint