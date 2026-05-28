import streamlit as st
from PIL import Image
import read_data

person_data = read_data.load_person_data()
personenliste = read_data.get_person_list(person_data)

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox
current_user = st.selectbox("Patienten", options=personenliste, key="sbVersuchsperson")

currentpicturepath = read_data.picture_path(
    current_user
)  # den picturepath aus dem dicitonary auslesen

# Laden eines Bilds mit Safety falls kein Bild vorhanden
if currentpicturepath:
    image = Image.open(currentpicturepath)
    # Anzeigen eines Bilds mit Caption
    st.image(image, caption=current_user)
else:
    st.write("nix Bild da")


if __name__ == "__main__":
    person_dict = read_data.load_person_data()
    person_names = read_data.get_person_list(person_dict)
    print(person_names)
    print(current_user)
    currentuserdata = read_data.find_person_data_by_name(current_user)
    print(currentuserdata)
    currentpicturepath = read_data.picture_path(current_user)
    print(currentpicturepath)  ###
