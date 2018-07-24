import os
from constante import *
import random

MAP_LINE_SIZE = 15
MAP_COLUMN_SIZE = 15


structure = []
elementVide = []
listItem = [aiguille, tube, ether]




with open("laby.txt", "r") as test:
	test = test.read().split('\n')
	for line in test:
		structure.append(list(line))


def placementItem(): 
	for line in range(MAP_LINE_SIZE):
		for col in range(MAP_COLUMN_SIZE):
			if structure[line][col]==' ':
				elementVide.append((line, col))

			
def displayLine():
	i = 0
	while i < len(structure):
		for elmt in structure:
			print('ligne {} : {}'.format(i, elmt))
			i += 1

def extraction():
	lenObject = len(listItem)
	filtre =  random.sample(elementVide, lenObject)
	for i in range(lenObject):
		line = filtre[i][0]
		col = filtre[i][1]
		#line, col = filtre[i]
		structure[line][col] = listItem[i]

	print("\nExtraction de 3 Coordonnee: {}".format(filtre))

	print('\n- Mettre dans la coordonnee {} : Objet: {}'.format(filtre[0], aiguille))
	print('- Mettre dans la coordonnee {} : Objet: {}'.format(filtre[1], tube))
	print('- Mettre dans la coordonnee {} : Objet: {}'.format(filtre[2], ether))

	print('\nA = aiguille\nT = tube\nE = ether')
	print('\nNouvelle Structure avec les 3 objets ajoutes aleatoirement:\n {}'.format(structure))


structure[1][1] = macGyver  #position de MAC dans le labyrinthe
structure[13][8] = guardian #position du gardien dans le labyrinthe


print('\nStructure du labyrinthe: \n {}'.format(structure))
placementItem()
print("\nCoordonnee Element Vide: {}".format(elementVide))
extraction()

