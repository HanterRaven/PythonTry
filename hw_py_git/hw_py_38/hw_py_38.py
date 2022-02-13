import json
from random import choice


def gen_person():
    name = ""
    tel = ""

    letters = ["a", "b", "c", "d", "e", "f", "e", "g"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    while len(name) != 7:
        name += choice(letters)
    while len(tel) != 10:
        tel += choice(num)
    person = {"name": name, "tel": tel}
    return person


def write_json(person_dict):
    count = 0
    try:
        data = json.load(open('persons111.json'))
        count = len(data)
    except FileNotFoundError:
        data = {}
    data[count] = person_dict
    with open("persons111.json", "w") as fil:
        json.dump(data, fil, indent=2)


for i in range(5):
    write_json(gen_person())
