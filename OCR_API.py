import cv2
import numpy as np
import requests
import io
import json

class OCR_API():
	def result(self,filepath,args):
		img = cv2.imread(filepath)
		url_api = "https://api.ocr.space/parse/image"
		_, compressedimage = cv2.imencode(".jpg", img, [1, 90])
		file_bytes = io.BytesIO(compressedimage)
		result = requests.post(url_api,files = {filepath: file_bytes},data = {"apikey": "da2e0586b688957","language": "eng"})
		result = result.content.decode()
		result = json.loads(result)
		parsed_results = result.get("ParsedResults")[0].get("ParsedText")
		return parsed_results
		
#ocr_obj=OCR_API()
# print(ocr_obj.result(r"C:\Users\DELL\Tesseract-OCR\Images\bigsleep.jpg",1))