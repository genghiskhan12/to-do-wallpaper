import ctypes
import sys
import subprocess
from PIL import Image,ImageDraw,ImageFont
import os 
from colour import Color
def wallpaper(name):    
	SPI_WALLPAPER = 0x14
	SPIF_UPDATINGFILE = 0x2
	SPI_SETDESKWALLPAPER=20 
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, 'C:\\Users\\ejinb\\Desktop\\programming files\\programing languages\\PYTHON\\wallpaper\\'+name+'.jpg' , 3)
	#ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image , 3)


def image_maker(text,name,size,color,font):
	print('Only supported JPEG or JPG')
	image_format = input('J for JFIF , JP for JPG: ')
	if image_format == 'J':

		image = Image.open(name+'.jfif')
	elif image_format == 'JP':
		image = Image.open(name+'.jpg')

	#image = 
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype(os.getcwd()+'\\fonts\\'+font,size=int(size))
	
	x = (image.size[0] / 2) + 30
	y = (image.size[1] / 2) + 30
	
	#color= # black color
	draw.text((x, y), text, font=font,fill=color)
	image.save(name+'.jpg',subsampling=0,quality=95)
				
def color_chooser():
	try:
		c = input('Type the color name: ')
		color = Color(c).rgb
		for x in color:
			color[x] = int(x)
	except:
		print('Color not found!! ')
	
	return color	

	'''
	r = input('r:')
	g = input('g:')
	b = input('b:')

	return f'rgb({r},{g},{b})'
	'''

def font_chooser():
	path = os.getcwd() + "\\fonts"
	print(path)
	print('font available now: ')
	fonts = []
	for i in os.listdir(path):
		print(i)
		fonts.append(i)

	choosen_font = input('Please choose font from the list: ')
	if choosen_font in fonts == False:
		font = 'Alphakind.ttf'
	else:
		font = choosen_font

	return font


def main():
	text = input('Task: ')
	name = input('File name: ')
	size = input('Font size: ')

	choose_color = input('Do you want to choose the font color? YES/NO: ')
	if choose_color == 'YES':
		color = color_chooser()
	elif choose_color == 'NO':
		color = 'rgb(3,23,252)'

	choose_font = input('Do you want to choose the font? YES/No: ')
	if choose_font == 'YES':
		font = font_chooser()
	elif choose_font == 'NO':
		font = 'Alphakind.ttf'
	image_maker(text,name,size,color,font)

	wallpaper(name)




if __name__ == '__main__':
		main()
