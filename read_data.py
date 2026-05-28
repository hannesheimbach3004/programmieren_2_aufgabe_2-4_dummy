import json


def load_person_data():
    """A Function that knows where the person database is and returns a dictionary with the persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data


def get_person_list(person_data):
    persons_list = []
    for pers_dict in person_data:
        person_dict = pers_dict
        persons_list.append(pers_dict["lastname"] + ", " + person_dict["firstname"])
    return persons_list


def find_person_data_by_name(suchstring):

    person_data = load_person_data()

    if suchstring == "None":
        return {}

    two_names = suchstring.split(", ")
    vorname = two_names[1]
    nachname = two_names[0]

    for eintrag in person_data:
        if eintrag["lastname"] == nachname and eintrag["firstname"] == vorname:
            return eintrag
    return {}


def picture_path(suchstring):
    current_person_dict = find_person_data_by_name(suchstring)

    if "picture_path" in current_person_dict:
        current_picture_path = current_person_dict["picture_path"]
        return current_picture_path
    else:
        return "data/pictures/none.jpg"


if __name__ == "__main__":
    find_person_data_by_name("Huber, Julian")
    picture_path("Huber, Julian")
