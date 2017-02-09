# Import the modules
from PIL import Image

try:
	
	def medianOdd(myList):		#median formula
		listLength = len(myList)
		sortedValues = sorted(myList)
		middleIndex = (listLength + 1)//2 - 1
		return sortedValues[middleIndex]


	tempImage = []

	for i in range(9):		#Load all the images
		tempImage.append(Image.open(str(i+1) + ".png"))

	width, height = tempImage[1].size	#get the width and height of the image

	newImage = Image.new('RGB', (width, height))	#creates new image with same width and height
	
	for x in range(0, width):		
		for y in range(0, height):
			rPix = []		#list for red
			gPix = []		#list for green
			bPix = []		#list for blue
			for i in range(1, 9):		#All the Images
				r, g, b = tempImage[i].getpixel((x,y))	#get color of pixel
				rPix.append(r)
				gPix.append(g)
				bPix.append(b)
			rMed = medianOdd(rPix)
			gMed = medianOdd(gPix)
			bMed = medianOdd(bPix)
			pixColor = (rMed, gMed, bMed)
			newImage.putpixel((x,y), pixColor)		#putpixel

	newImage.show()
	newImage.save("new.png")

	

except:
	# Expload
	print("Didn't work")