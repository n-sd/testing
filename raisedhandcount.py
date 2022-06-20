import raisedhandsmodule
import openpifpaf
import sys
import os
from PIL import Image, ImageFont, ImageDraw
import glob

#print(argv[1])





for file in glob.glob("*"):
	print(file)
	raisednumber = 0
	os.system("python3 -m openpifpaf.predict " + file + " --json-output --disable-cuda")


	raisednumber = raisedhandsmodule.raisedhandscount( file + '.predictions.json')


	testimage = Image.open(file)
	title_font = ImageFont.truetype('JetBrainsMono-Medium.ttf', 100)
	title_text = raisednumber
	image_editable = ImageDraw.Draw(testimage)
	image_editable.text((15,15), title_text, (0, 0, 255), font=title_font)
	testimage.save(file+'counted.png')

#raisedhandsmodule.raisedhandscount(sys.argv[1])


