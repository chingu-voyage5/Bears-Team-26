from pymongo import MongoClient
import pprint


client = MongoClient() #creating connection with mongodb
db = client.test_database #creating a database
project = db.project  #creating a collection..this is like table


def insert():
    project_name = input("Give your project_name: ")
    project_des = input("give your project description: ")
    list = [] #for taking tags
    print("give your project tags, tags should be at least 3 and max 5: ")
    i=0
    while i<5:
        k = input("")
        list.append(k)
        i = i+1
        if i==3:
            a = input("want to give more?y/n: ")
            if a=="n":
                break

    project.insert({'name': project_name,'description':project_des,'tags':list}) #inserting values in database

    ans = input("want to search projects similiar to yours?y/n: ")
    if ans == "y":
        search()
    else:
        print("see you soon")

    
    
    
    
    
def search():
    print("give tags to search for projects,maximum tags can be 3: ")
    list = []
    i=1
    while i<=3:
        k = input("")
        list.append(k)
        i=i+1
   
    for project in db.project.find({"tags": {"$all": list }}):
        pprint.pprint(project)
        
insert()

    
    
    
    
    


    

