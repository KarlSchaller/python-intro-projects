#https://www.gpb.org/irasshai/japanese1/lesson1
#http://www.gpb.org/files/pdfs/irasshai//1L2.pdf

import requests

'''
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#print(len(res.text))
res.raise_for_status()

target = open('miscstuff/rj.txt', 'wb')
for chunk in res.iter_content(100000):
    target.write(chunk)

target.close()
'''

'''
baseURL = 'http://www.gpb.org/files/pdfs/irasshai/'
for i in range(1, 74):
    targetURL = baseURL + '1L' + str(i) + '.pdf'
    res = requests.get(targetURL)
    res.raise_for_status()
    if i < 10:
        targetFile = open('miscstuff/00' + str(i) + '.pdf', 'wb')
    else:
        targetFile = open('miscstuff/0' + str(i) + '.pdf', 'wb')
    for chunk in res.iter_content(100000):
        targetFile.write(chunk)
    targetFile.close()
    print(targetURL)

baseURL = 'http://www.gpb.org/files/pdfs/irasshai/'
for i in range(1, 63):
    targetURL = baseURL + '2L' + str(i) + '.pdf'
    res = requests.get(targetURL)
    res.raise_for_status()
    if i < 27:
        targetFile = open('miscstuff/0' + str(73+i) + '.pdf', 'wb')
    else:
        targetFile = open('miscstuff/' + str(73+i) + '.pdf', 'wb')
    for chunk in res.iter_content(100000):
        targetFile.write(chunk)
    targetFile.close()
    print(targetURL)
'''

import PyPDF2, os

pdfFiles = os.listdir('miscstuff')
pdfFiles = sorted(pdfFiles)
#print(pdfFiles)

pdfWriter = PyPDF2.PdfFileWriter()

for target in pdfFiles:
    target = open('miscstuff/' + target, 'rb')
    pdf = PyPDF2.PdfFileReader(target)
    for pageNum in range(pdf.numPages):
        page = pdf.getPage(pageNum)
        pdfWriter.addPage(page)

outTarget = open('all.pdf', 'wb')
pdfWriter.write(outTarget)
outTarget.close()

#------------------------------------------------------------------------

import webbrowser, sys

print(sys.argv)
if len(sys.argv) == 0:
    print("Please enter an argment")
elif sys.argv[1] == '-x':
    print("extracting")

baseURL = "https://www.google.com/maps/place/"
if len(sys.argv) > 1:
    print(sys.argv)
    target = baseURL + "+".join(sys.argv[1:])
    webbrowser.open(target)
else:
    #target = baseURL + 

#1801 N. Broad Street Philadelphia, PA 19122 USA
#870+Valencia+St,+San+Francisco,+CA+
