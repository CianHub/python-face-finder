import face_recognition

image_of_tenshin = face_recognition.load_image_file(
    './img/known/tenshin-nasukawa.png')
tenshin_face_encoding = face_recognition.face_encodings(image_of_tenshin)[0]

unknown_image = face_recognition.load_image_file(
    './img/unknown/2.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces(
    [tenshin_face_encoding], unknown_face_encoding)

if results[0]:
    print('Its Tenshin')
else:
    print('It is not Tenshin')
