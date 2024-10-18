from pathlib import Path
import pdf2image
import cv2
from pdf2image import convert_from_path
import os
from scanner.scan import DocScanner

# If in pdf convert and store to jpeg
def convert_to_jpeg(pdf_path,output_folder):
    print("*"*50)
    print("converting.......")
    pages = convert_from_path(pdf_path, 200)
    i=0
    for page in pages:
        i+=1
        join= 'page'+str(i)+'.jpg'
        path= Path.joinpath(output_folder,join)
        page.save(path, 'JPEG')
        return path

#Store if format is jpeg
def in_jpeg(img_path,output_folder):
    img=cv2.imread(img_path)
    output_path= Path.joinpath(output_folder,os.path.basename(img_path))
    scanner = DocScanner()
    scanner.scan(img_path,output_path)
    return output_path
