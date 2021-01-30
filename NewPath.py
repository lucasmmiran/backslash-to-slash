#Lucas Mendes Miranda
#Raplaces "\" with "/" in a windows file path

def Npath(path):
    path = path.replace("\\", "/")
    return path

path = input("Insert the path you wish to change:\n")
print (Npath(path))