import cv2
import io
import json
import requests
image=input("Enter name and format of image('image.jpg') :\n\n")
img = cv2.imread(image)
url_api = "https://api.ocr.space/parse/image"
_,compressedimage = cv2.imencode(".jpg", img, [1, 90])
file_bytes = io.BytesIO(compressedimage)
print("Languages available:\n  English\n  Chinese \n  French\n  Japanese")
lang1=input("\n\n\nEnter Text Language: \n")
lang1=lang1.lower()

if(lang1=="english"):
    lang="eng"
elif(lang1=="french"):
    lang="fre"
elif(lang1=="japanese"):
    lang="jpn"
elif(lang1=="chinese"):
    lang="cht"
result = requests.post(url_api,
              files = {image: file_bytes},
              data = {"apikey": "aeebacc24588957",
                     "language": lang})
result = json.loads(result.content.decode())
parsed_results = result.get("ParsedResults")[0]
text= parsed_results.get("ParsedText")
print(text)