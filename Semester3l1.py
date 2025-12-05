Grades ={
    "mohammed": {
        "english": "88",
        "math": "78",
        "science": "90"
    },
    "ahmed": {
        "engilish" : "96",
        "math": "98",
        "science": "97"
    },
    "yusuf": {
        "english": "49",
        "math": "32",
        "science" : "15"
    }
}
def show_grade():
    question1 = input("Which students grade would you like to see?")
    print(question1)
    question1b = question1.lower()
    if question1b in Grades:
        question2 = input("What class are you checking?")
        print(question2)
        question2b = question2.lower()
        if question2b in Grades[question1b]:
            print(Grades[question1b][question2b])
        else:
            print("Sorry, that class dosen't exist,")
    else:
        print("Sorry, that name isn't in our data,")

show_grade()