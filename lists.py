
def remove_elements(list_to_remove_elements):
	len_lista = len(list_to_remove_elements)
	if len_lista >=6:
		del list_to_remove_elements [5]
		del list_to_remove_elements [4]
		del list_to_remove_elements [0]
		return list_to_remove_elements

	elif len_lista ==5:
		del list_to_remove_elements [4]
		del list_to_remove_elements [0]
		return list_to_remove_elements

	elif len_lista <5 and len_lista >= 1:
		del list_to_remove_elements [0]
		return list_to_remove_elements

	else:
		return []


def add_elements(list_to_add_elements):
	list_to_add_elements.append("Yellow")
	list_to_add_elements.insert(0, "Pink")
	return list_to_add_elements


def is_empty(list_to_check):
	if list_to_check == []:
		return True 
	else: 
		return False 

def check_lists(list_to_compare1, list_to_compare2):
	lista1 = list_to_compare1
	lista2 = list_to_compare2
	if len(lista1) >= 3 and len(lista2)>= 3:
		if lista1[2] == lista2[2]:
			Valor = True
		else:
			Valor = False 
	else: 
		Valor = False 
	return Valor 	 


def list_of_lists(list_of_lists_to_modify):
	list1 = list_of_lists_to_modify[0]
	list2 = list_of_lists_to_modify[1]
	list3 = list_of_lists_to_modify[2]
	if len(list1) > 0:
		list1 = list1[0:2]
	else: 
		list1 = []
	if len(list2) >= 2:
		list2 = list2[1:4]
	else: 
		list2 = []
	if len(list3) > 0:
		list3 = list3[-2:]
	todo = [list1, list2, list3]
	return todo 
