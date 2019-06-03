import random 
import numpy as np

class suffixTree:
	
	def __init__(self):
		self.suffixNodes = [0,1]

	class Node:
		def __init__(self,data):
			self.data = data
			self.children = []
			self.isSuffixNode = True

		def addChildren(self, obj):
			self.children.append(obj)


class Crossover:

	def __init__(self, sequence1, sequence2):
		self.Operations = []
		self.probability = 0.6
		self.sequence1 = sequence1
		self.sequence2 = sequence2
		self.length		= len(sequence1)
		self.len_cross = round(self.probability*self.length)
		self.off1 = [None] * self.length
		self.off2 = [None] * self.length
		self.map_section_arr_1 = []
		self.map_section_arr_2 = []

		self.choice = "PMX"


	def remove_duplicates(self, elements, sorted_list):
		iterator = len(sorted_list) -1

		while(iterator):
			new_pos = np.where(sorted_list==elements[iterator]) or None 
			new_pos = new_pos[0]
			if (new_pos):
				elements[iterator] = elements[new_pos]
				elements = elements[-new_pos]
				sorted_list = sorted_list[-new_pos]
			else:
				iterator -= 1

		self.map_section_arr_1 = elements
		self.map_section_arr_2 = sorted_list

	def pmx(self):

		rc1 = random.randrange(1,self.length-self.len_cross+1)
		rc2 = rc1 + self.len_cross

		map_section_1 = [None] * (rc2-rc1)
		map_section_2 = [None] * (rc2-rc1)

		ms1 = self.sequence1[rc1:rc2]
		ms2 = self.sequence2[rc1:rc2]

		self.off1[rc1:rc2] = ms2
		self.off2[rc1:rc2] = ms1

		order = np.argsort(ms1)
		index = 0


		for iterator in order:
			map_section_1[index] = ms1[iterator]
			map_section_2[index] = ms1[iterator]
			index += 1

		self.remove_duplicates(map_section_1, map_section_2)

		normal_sequence = list(range(self.length))
		op_sequence		= normal_sequence[0:rc1] + normal_sequence[rc2-1:]


		for iterator in op_sequence:
			item_list_1 = np.where(self.map_section_arr_2 == self.sequence1[iterator]) or None
			item_list_2 = np.where(self.map_section_arr_1 == self.sequence2[iterator]) or None

			itemlst1 = item_list_1[0]
			itemlst2 = item_list_2[0]

			if(itemlst1):
				self.off1[iterator] = self.map_section_arr_1[itemlst1]
			else:
				self.off1[iterator] = self.sequence1[iterator]

			if(itemlst2):
				self.off2[iterator] = self.map_section_2[itemlst2]
			else:
				self.off2[iterator] = self.sequence2[iterator]

class KeyWordTree:
	# This is a Node class that is internal to the BinarySearchTree class. 
	class Node:
		def __init__(self,val):
			self.val = val
			self.out = {}

			
		def getVal(self):
			return self.val
		
		def setVal(self,newval):
			self.val = newval
			
		def getLeft(self):
			return self.left
		
		def getRight(self):
			return self.right
		
		def setLeft(self,newleft):
			self.left = newleft
			
		def setRight(self,newright):
			self.right = newright
			
		# This method deserves a little explanation. It does an inorder traversal
		# of the nodes of the tree yielding all the values. In this way, we get
		# the values in ascending order.
		def __iter__(self):
			if self.left != None:
				for elem in self.left:
					yield elem
					
			yield self.val
			
			if self.right != None:
				for elem in self.right:
					yield elem

		def __repr__(self):
			return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
			
	# Below are the methods of the BinarySearchTree class. 
	def __init__(self, root=None):
		self.root = root
		
	def insert(self,val):
		self.root = BinarySearchTree.__insert(self.root,val)
		
	def __insert(root,val):
		if root == None:
			return BinarySearchTree.Node(val)
		
		if val < root.getVal():
			root.setLeft(BinarySearchTree.__insert(root.getLeft(),val))
		else:
			root.setRight(BinarySearchTree.__insert(root.getRight(),val))
			
		return root
		
	def __iter__(self):
		if self.root != None:
			return iter(self.root)
		else:
			return iter([])

	def __str__(self):
		return "BinarySearchTree(" + repr(self.root) + ")"
 
def main():
	s = input("Enter the first sequence: ")
	lst_string1 = s.split(" ")
	sequence1 = []
	for x in lst_string1:
		sequence1.append(int(x))

	v = input("Enter the second sequence: ")
	lst_string2 = v.split(" ")
	sequence2 = []
	for x in lst_string2:
		sequence2.append(int(x))
	cros = Crossover(sequence1,sequence2)

	cros.pmx()

	print(cros.off1)
	print(cros.off2)
	# lst = s.split()
	
	# tree = BinarySearchTree()
	
	# for x in lst:
	# 	tree.insert(float(x))
		
	# for x in tree:
	# 	print(x)

if __name__ == "__main__":
	main()