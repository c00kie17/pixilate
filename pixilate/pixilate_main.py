import sys
import urllib.request
from PIL import Image
import platform
import subprocess
import os

def load_image(image_path):
	try:
		image = Image.open(image_path)
	except Exception:
		print("cant find image in: "+image_path)
		sys.exit()
	return image 

def resize_image(image,new_width=100):
	old_width, old_height = image.size
	ratio = float(old_height)/float(old_width)
	new_height = int(ratio * new_width)
	dim = (new_width, new_height)
	image = image.resize(dim)
	return image

def get_color(pixel):
	return "\x1b[48;2;"+str(pixel[0])+";"+str(pixel[1])+";"+str(pixel[2])+"m  \x1b[0m" 	


def transform(image,step=100):
	image = image.convert('RGB')
	pixels = list(image.getdata())
	string_image = [get_color(pixel) for pixel in pixels]
	for index in range(step, len(string_image), step+1):
		string_image.insert(index,'\n',)
	return ''.join(string_image) 

def main():
	try:
		image_path = sys.argv[1]
	except IndexError:
		print('please enter a image path')
		sys.exit()

	try:
		save = bool(int(sys.argv[2]))
	except IndexError:
		save = False

	if 'http' in image_path:
		urllib.request.urlretrieve(image_path, "image.jpg")
		image_path = "image.jpg"

	image = load_image(image_path)

	image  = resize_image(image)

	image = transform(image)

	print(image)

	if save:
		file_name = image_path.split('/')[-1]
		file_name = file_name.split('.')[0]+".txt"
		file_path = os.path.join(os.getcwd(),file_name)
		file = open(file_path,"w+")
		file.write(image)
		file.close()


if __name__ == '__main__':
	main()

	





		




