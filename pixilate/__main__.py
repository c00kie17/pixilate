import sys
import urllib.request
from PIL import Image
import platform
import subprocess
import os
import ntpath

def load_image(image_path):
	try:
		image = Image.open(image_path)
	except Exception:
		print("cant find image in: "+image_path)
		sys.exit(1)
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
		sys.exit(1)

	try:
		save = bool(int(sys.argv[2]))
	except Exception:
		save = False
		print("save file is set to:",save)

	if 'http' in image_path:
		urllib.request.urlretrieve(image_path, "image.jpg")
		image_path = "image.jpg"

	image = load_image(image_path)

	image  = resize_image(image)

	image = transform(image)

	print(image)

	if save:
		file_name = ntpath.basename(image_path)
		file_name = file_name.split('.')[0]+".txt"
		file_path = os.path.join(os.getcwd(),file_name)
		with open(file_path, 'w+') as file:
			file.write(image)


if __name__ == '__main__':
	main()

	





		




