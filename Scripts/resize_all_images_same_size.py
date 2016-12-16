import os
from PIL import Image

input_dir = "/home/menon/Pictures"
directories = os.listdir(input_dir) # convert to list
new_size = (100, 100) # tuple with two elements width and hight 


for folder in directories:
	
	# print (folder)
	new_folder = os.listdir(input_dir + '/' + folder)
	# print (new_folder)

	try :

		for image in new_folder:
			
			# im = Image.open(image) # File not found ERROR
			im = Image.open(input_dir + "/" + folder + "/" + image)

			# The Algorithm orders from fastest to best quality are 
			# NEAREST, BILINEAR, BICUBIC, ANTIALIAS

			new_image = im.resize(new_size, Image.ANTIALIAS)

			# "/home/menon/Pictures/folder/100x100.jpg"
			new_image.save(input_dir + "/" + folder + "/"  + "100x100.jpg") 

			# If you want to remove old image 
			# os.remove(input_dir + "/" + folder + "/" + image)
			
	except Exception as e:
		print(e)
		print("Can't resize image " + str(image))
