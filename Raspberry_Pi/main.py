from fileinput import filename
import sys
import cv2 
import numpy as np 
import requests
import face_recognition as fr
import time

def getData(URL,filename):
    r = requests.get(URL+"/Medicion/getData")
    with open(filename,"wb") as file:
	    file.write(r.content)

def getResponse(URL):
    r = requests.get(URL+"/Results/getData")
    return r.text    

def faceRecon(filename):

    #list of filenames of the reference images
    refImg = ["usr1.png","usr2.png","usr3.png"]

    #Make a loop to analyze all of the reference images

    for i in refImg
        #Load reference picture
        picture_of_me = fr.load_image_file(refImg)
        # my_face_encoding now contains a universal 'encoding' of 
        # my facial features that can be compared to any other picture of a face!
        my_face_encoding = fr.face_encodings(picture_of_me)[0]

            #Load picture to compare
        unknown_picture = fr.load_image_file(filename)
        try:
            unknown_face_encoding = fr.face_encodings(unknown_picture)[0]
            # Now we can see the two face encodings are of the same person with `compare_faces`!
            results = fr.compare_faces([my_face_encoding], unknown_face_encoding)

            if results[0] == True:
            return "Reconocido"
            else:
                return "Noreconocido"
        except IndexError:
            return "Error"

def postResponse(response,URL):
    r = requests.post(URL+"/Results/newData/"+response)
    return r.text

def main(url):
    filename="response.png"
    getData(URL=url,filename=filename)
    time.sleep(2)
    response = faceRecon(filename=filename)
    postResponse(response=response,URL=url)
    print(getResponse(url))

if __name__ == "__main__":
    url = sys.argv[1:][0]
    while True: 
        main(url)
        time.sleep(15)
