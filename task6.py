def addTask():
    print("Hello please Add this info")
    task = {
        "id": input("id : "),
        "title": input ("Title : "),
        "due_data": input("due data : "),
        "is_complete":False
    }

addTask()   