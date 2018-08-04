from PIL import ImageFont, ImageDraw, Image  
import numpy as np  
import os
import random

 # Calcula el tamaño de la fuente para que el largo del texto dibjuado tenga un ancho  máximo del p% de la imagen
def calcFontSize (texto,font,image,p):
    textSize    =font.getsize(plateChars)
    textWidth   = textSize[0]
    textHeight  = textSize[1]
    factorX     = textWidth/font.size
    factorY     = textHeight/font.size
    print(image.size)
    # desiredHeight= image.size[1]*p
    desiredWith  =image.size[0]*p
    fontSize = int(desiredWith/factorX)
    return fontSize

def calcRandomPosition(containerImage):
    xMax=containerImage.size[0]
    yMax=containerImage.size[1]
    rx=int(random.uniform(0,xMax))
    ry=int(random.uniform(0,yMax))
    return rx,ry

def calcCenterPosition(eImage,iImage):
    exCenter=eImage[0]/2
    eyCenter=eImage[1]*0.48
    ixCenter=iImage[0]/2
    iyCenter=iImage[1]/2

    cx=exCenter-ixCenter
    cy=eyCenter-iyCenter
    return cx,cy
def getRandomFile(path):
    listFileNames= os.listdir(path)
    randomIndex=int(random.uniform(0,len(listFileNames)))
    return path + listFileNames[randomIndex]
    
# obener la placa base
basePlateName= getRandomFile("placas/")
image = Image.open(basePlateName)
   
draw = ImageDraw.Draw(image) 
# draw.line((0, 0) + image.size, fill=128)


plateChars="AX6S-1-23"


# listFonts= os.listdir("fonts/")
fontName= getRandomFile("fonts/")
print(fontName)

font = ImageFont.truetype(fontName, 500)  
fSize=calcFontSize(plateChars,font,image,0.95)
font = ImageFont.truetype(fontName, fSize) 

print("EL TAMAÑO DE FUENTE NECESARIO ES : " + str(fSize)) 

textPx0=0
textPy0=50

textSize=font.getsize(plateChars)
textPx0 ,textPy0 =  calcCenterPosition(image.size,textSize)

textWidth = textSize[0]
textHeight = textSize[1]

draw.text((textPx0, textPy0), plateChars, font=font,fill=(0,0,0))  




print("EL TAMAÑO ES : ") 
print(textSize)



draw.line((textPx0, textPy0) + (textPx0 +textWidth ,textPy0 + textHeight), fill=(0,255,0),width=2)  

image.save("./" + plateChars + ".jpg")  