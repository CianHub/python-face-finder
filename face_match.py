import face_recognition

image_of_conor = face_recognition.load_image_file(
    './img/known/conor-mcgregor.jpeg')

conor_face_encoding = face_recognition.face_encodings(image_of_conor)
