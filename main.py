from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math
import csv

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
pdfmetrics.registerFont(TTFont('LEMONMILK', 'LEMONMILK-Light.ttf'))

names=[]
i=0
x = 107
y = 655

with open('names.txt', 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    names.append(row[0])

pages = math.ceil( len(names) / 8 )

while (i < len(names)): 
  can.setFont('LEMONMILK',  35 - len(names[i]))

  if (i % 2 == 1):
    can.drawString(x,y, names[i])
    x=107
    y-=155
    
  if (i % 2 == 0): 
    can.drawString(x,y, names[i])
    x+=241
    
  i+=1

can.save()
    # new page based on original.pdf
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("original.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = open("namesToPrint" + str(pages) + ".pdf", "wb")
output.write(outputStream)
outputStream.close()

#method:
# merge namestoprint1 + namestoprint2 etc