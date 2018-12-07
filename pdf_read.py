from __future__ import print_function
import PyPDF2
import textract
import re
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import os

global head
head = []
lst = []
cont=[]

def getPDFContent(path):
    global content 
    content = ""
    p = file(path, "rb")
    pdf = PyPDF2.PdfFileReader(p)
    num_pages = pdf.numPages
    for i in range(0, num_pages):
        content += pdf.getPage(i).extractText() + "\n"
    if content != "":
    	content = content
    	email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",content)
    	print ("the email id is", email)
    	ph = re.findall(r"([91|\+91]?\s?\d{10})",content)
    	print ("Phone no: ", ph)
	print ('\n')
    content = " ".join(content.replace(u"\xa0", " ").strip().split())     
    cont.append(content)
    return cont

def extract(lst,key):
	used_counted = []
	for h in lst:
		if key not in used_counted:
			if key in h:
				used_counted.append(key)
				str1 = ''.join(h)
				ind = head.index(key)
				if ind == (len(head)-1):
					befor_keyowrd, keyword, after_keyword = str1.partition(key)
					print (key, after_keyword)
				else:
					ind1 = ind+1
					str2 = head[ind1]
					befor_keyowrd, keyword, after_keyword = str1.partition(key)
					b_k, keyword, after_keyword  = after_keyword.partition(str2)
					print (key, b_k)
					print ('\n')


path = 'resume_name.pdf'
cont1 = getPDFContent(path)
pdfFileObj = open(path,'rb')
path1 = os.path.realpath(pdfFileObj.name)
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
for i in range(0, pages):
	pageObj = pdfReader.getPage(i)
	CO = textract.process(path1, method='pdfminer')
lst.append(CO.split('\n'))

for i in lst :
	for j in i:
		if j.isupper() and len(j)>7:
			head.append(j)
for i in range(len(head)):
	key = head[i]
	extract(lst, key)

