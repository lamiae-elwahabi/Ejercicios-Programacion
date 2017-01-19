import xml.etree.ElementTree as ET
tree = ET.parse('menu.xml')
root = tree.getroot()

menu={}
for food in root.findall('food'):
	price = food.find('price').text
	name = food.find('name').text
	menu[name] = price

for name, price in menu.items():
   print(name, ":", price)

#Precondición
#assert isinstance (menu, dict), "Esto no es un diccionario."
#CASOS TEST:
#CASO TEST 1: 

