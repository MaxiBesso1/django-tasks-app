from models import Tarea
"""
def iniciar(query):
    list=[]
    name = ""
    description = ""
    priority = ""
    position=0
    for object in query:
        print(object)
        for part in object:
            print(part)
            if part == "/":
                position+=1
            if position== 0:
                name+=object
            elif position == 1:
                description+=object
            elif position == 2:
                priority += object
        tuple=(name,description,priority)
        list.append(tuple)
        return list
    

tuple=[("maxi/besso/11"),("maxi1/besso1/12")]
print(iniciar(tuple))
"""
content_db = Tarea.objects.all()
print(content_db)

