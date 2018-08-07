from PIL import ImageFont, ImageDraw, Image  
import numpy as np  
import os
import random


# Establece la cooredada x0,y0 donde ubicar la placa dentro del backgound desde la esquina superior izquierda

plateCoordinatesDict={
"fondosRuido/background1.jpg":(116,105),
"fondosRuido/background2.jpg":(124,138),
"fondosRuido/background3.jpg":(144,140)
}

# Calcula el tamaño de la fuente para que el largo del texto dibjuado tenga un ancho  máximo del p% de la imagen
def calcFontSize (texto,font,image,p):
    textSize    =font.getsize(texto)
    textWidth   = textSize[0]
    textHeight  = textSize[1]
    factorX     = textWidth/font.size
    factorY     = textHeight/font.size
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
    
def getRandomChar():
   
    listChars   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    randomIndex = randomIndex=int(random.uniform(0,len(listChars)))
    return listChars[randomIndex]

def getRandomStringGroup(num):
    string =""
    for i in range(num):
        string += getRandomChar()
    return string

def I(a,b):
     randomInt = randomIndex=int(random.uniform(a,b+1))
     return randomInt

def createPlate(plateChars):

    # obtener el fondo
    backgroundName =getRandomFile("fondosRuido/")
    imageBackgrond = Image.open(backgroundName)

    # obener la placa base 
    basePlateName= getRandomFile("placas/")
    image = Image.open(basePlateName)
    draw = ImageDraw.Draw(image) 

    # obener la placa fuente
    fontName= getRandomFile("fonts/")
    font = ImageFont.truetype(fontName, 500)  
    fSize=calcFontSize(plateChars,font,image,0.95)
    font = ImageFont.truetype(fontName, fSize) 

    textSize=font.getsize(plateChars)
    textPx0 ,textPy0 =  calcCenterPosition(image.size,textSize)

    textWidth = textSize[0]
    textHeight = textSize[1]

    draw.text((textPx0, textPy0), plateChars, font=font,fill=(0,0,0))  
    imageResized=image.resize((103,52))
    xBackground=plateCoordinatesDict[backgroundName][0]
    yBackground=plateCoordinatesDict[backgroundName][1]
   
    x, y = imageResized.size
    imageBackgrond.paste(imageResized,(xBackground,yBackground))
    imageBackgrond.save("./result/" + plateChars + ".jpg")  


numberOfPlates= 200
for i in range(numberOfPlates):
    p = int((i/numberOfPlates)*100)
    g1 = getRandomStringGroup(I(2,3)) #genera un grupo que puede tener 2 a 3 caracteres
    g2 = getRandomStringGroup(I(2,3)) #genera un grupo que puede tener 2 a 3 caracteres
    g3 = getRandomStringGroup(I(1,2)) #genera un grupo que puede tener 1 a 2 caracteres
    stringPlate= g1 + "-"+  g2 + "-" + g3
    createPlate(stringPlate)
    print(stringPlate + " -- >" + str(p) + "%")
