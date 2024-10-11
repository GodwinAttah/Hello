people = [
    {"Surname": "Godwin", "Location": "Joel"},
    {"Surname": "Goodness", "Location": "Jochebed"},
    {"Surname": "Joel", "Location": "Jays"},
    {"Surname": "Jochebed", "Location": "Lagos"}
]


people.sort(key=lambda person: person["Surname"])

print(people)