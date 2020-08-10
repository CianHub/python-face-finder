import face_recognition
from PIL import Image, ImageDraw

image_of_conor = face_recognition.load_image_file(
    './img/known/conor-mcgregor.jpeg')
conor_face_encoding = face_recognition.face_encodings(image_of_conor)[0]

image_of_nate = face_recognition.load_image_file(
    './img/known/nate-diaz.jpg')
nate_face_encoding = face_recognition.face_encodings(image_of_nate)[0]

image_of_john = face_recognition.load_image_file(
    './img/known/john-mcarthy.jpg')
john_face_encoding = face_recognition.face_encodings(image_of_john)[0]

image_of_herb = face_recognition.load_image_file(
    './img/known/herb-dean.jpg')
herb_face_encoding = face_recognition.face_encodings(image_of_herb)[0]

known_face_encodings = [conor_face_encoding,
                        nate_face_encoding, john_face_encoding, herb_face_encoding]
known_face_names = ['Conor McGregor',
                    'Nate Diaz', 'John McCarthy', 'Herb Dean']

test_image = face_recognition.load_image_file(
    './img/groups/conor-nate7.jpg')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)
    name = "unknown person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)),
                       fill=(0, 0, 0), outline=(0, 0, 0))
        draw.text((left + 6, bottom - text_height - 5),
                  name, fill=(255, 255, 255, 255))
    else:

        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)),
                       fill=(0, 0, 0), outline=(0, 0, 0))
        draw.text((left + 6, bottom - text_height - 5),
                  name, fill=(255, 255, 255, 255))


del draw

pil_image.show()
