#!/usr/bin/python3.6
# pip3.6 install --user google-cloud
# pip3.6 install --user google-cloud-vision

import xlrd
from google.cloud import vision
import os
import pandas as pd

Application_Credentials = 'your json credentials file'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Application_Credentials
client = vision.ImageAnnotatorClient()
image = vision.types.Image()
#urls.xlsx has the image urls 
loc = ("urls.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
df = pd.DataFrame()
# loop through every url, retreive the image and send to google vision
for i in range(sheet.nrows):
    image_src_temp = sheet.cell_value(i, 0)
    image.source.image_uri = image_src_temp
    response = client.label_detection(image=image)
    labels = response.label_annotations
    l = []
    for label in labels:
        l.append(label.description)
    s = ' '.join(l)
    print("s")
    print(s)
    df = df.append({'URL': image_src_temp, 'Labels': s}, ignore_index=True)
df.to_excel("Labels.xlsx",index=False)
