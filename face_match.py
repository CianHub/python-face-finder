import face_recognition

image_of_conor = face_recognition.load_image_file(
    './img/known/conor-mcgregor.jpeg')
conor_face_encoding = face_recognition.face_encodings(image_of_conor)[0]

unknown_image = face_recognition.load_image_file(
    './img/unknown/1.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
