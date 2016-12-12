import xml.etree.ElementTree as ET
from urllib import request 
tree = ET.parse('name_of_xml_file.xml') 
root = tree.getroot()

image_link_list = [] # make empty list

for country in root.findall('pictures'): # picture is a tag name in .xml file
    image_link_list.append(country.find('actual').text) # save the tag text in list

for i in image_link_list: # This is for print our link
	print (i)

# carea a local path where we save our files
local_path = "/home/menon/Pictures/AmphiprionClarkii/" 

for image_link in image_link_list:
	image_file_name = image_link.split('/')[-1] # Extract the file name form link URL 
	print (image_file_name) # just print file name :)
	request.urlretrieve(image_link, local_path + image_file_name) # Download the files
