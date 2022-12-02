import sys
import time
import requests
import cv2 
import numpy as np 



if __name__ == "__main__":
    img = sys.argv[1:][0]
    url = ' https://43b2-200-68-183-53.ngrok.io/Medicion/newData'
    files = {'file': open('ref_img/' + img, 'rb')}

    r = requests.post(url,files=files)

    print(r.text)