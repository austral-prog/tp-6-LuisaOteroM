def remove_elements(lista):
    
    nueva_lista = lista[:]
    
    if len(nueva_lista) > 5:
        del nueva_lista[5]  
    if len(nueva_lista) > 4:
        del nueva_lista[4]  
    if len(nueva_lista) > 0:
        del nueva_lista[0]  

    return nueva_lista


def add_elements(lista):

    nueva_lista = lista[:]  
    nueva_lista1 = nueva_lista.insert(0, 'Pink')
    nueva_lista2 = nueva_lista1.append('Yellow')

    return nueva_lista2


def is_empty(lista):

    if len(lista) == 0:
        return True
    else:
        return False


def check_lists(lista1, lista2):
   
    if len(lista1) >= 3 and len(lista2) >= 3:
        return lista1[2] == lista2[2]
    else:
        return False


def list_of_lists(listas):
    nueva = []

    if len(listas) >= 1:
        sublista1 = listas[0][:2]  
    else:
        sublista1 = []
    nueva.append(sublista1)

  
    if len(listas) >= 2:
        sublista2 = listas[1][1:4]  
    else:
        sublista2 = []
    nueva.append(sublista2)

    if len(listas) >= 3:
        sublista3 = listas[2][-2:]  
    else:
        sublista3 = []
    nueva.append(sublista3)

    return nueva
