def remove_elements(lista):#copio la lista para no modificar la original

    if len(copia_lista_uno) > 5: 
        del copia_lista_uno[5]  
    if len(copia_lista_uno) > 4: 
        del copia_lista_uno[4] 
        del copia_lista_uno[0]  

    return copia_lista_uno

def add_elements(lista):
    copia_lista_dos = lista[:]  
    copia_lista_dos.insert(0, 'Pink') 
    copia_lista_dos.append('Yellow') 
    
    return copia_lista_dos 


def is_empty(lista):
    return len(lista) == 0 


def check_lists(lista1, lista2):
    if len(lista1) >= 3 and len(lista2) >= 3: 
        return lista1[2] == lista2[2] 
    else: return False


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
