import xml.etree.ElementTree as ET
tree = ET.parse('playListVLC.xml')
root = tree.getroot()

menu={}
for food in root.findall('food'):
	price = food.find('price').text
	name = food.find('name').text
	menu[name] = price
