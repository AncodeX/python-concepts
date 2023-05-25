def day_tuple():
    siblings = tuple()

    sister = ("Leidy",)
    brother = ("Alexander",)

    siblings = sister + brother
    print(type(siblings))

    family_members = siblings + ("Maria", "Ivan")

    print(family_members)

    hermanos = family_members[0:2]
    padres = family_members[2:4]

    print(hermanos, padres)

def day_dictionary():
    dog = {
        "name": "huku",
        "color": "white",
        "breed": "pitbull",
        "legs": 4,
        "age": 9,
    }

    print(dog)

    student = {
        "first_name": "daniel",
        "last_name": "ramirez",
        "gender": "male",
        "age": 19,
        "marital_status": "single",
        "skills": ["JavaScript", "SQL", "HTML", "CSS", "Python", "FastAPI", "Linux"],
        "country": "Colombia",
        "city": "Bogota",
        "address": "Street 8"
    }

    print(student)
    print(len(student))

    print(student["skills"])

    student["skills"].extend(["Console", "NodeJS"])

    print(student["skills"])

    student_keys = [k for k in student.keys()]
    student_values = [v for v in student.values()]
    print(student_keys, student_values)

    student_items = tuple(map(lambda k: k, student.items()))
    print(student_items)

    student.pop("city")
    print(student)
    student.clear()
    print(student)


if __name__ == "__main__":
    day_dictionary()
    