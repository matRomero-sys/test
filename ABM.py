import json

print("Este es mi programaa")

base_datos = "base_datos.json"

def verif_contra(usuario, int):
    for i in range(int):
        contrasena = input("Ingrese la contraseña: ")
        if contrasena == usuario.get("contrasena"):
            return True
        else:
            print(f"Contraseña incorrecta, le quedan {(int-1)-i} intentos")
    else:
        print("Ha agotado todos los intentos...")
        return False

def agregar_usuario():
    with open(base_datos, "r") as archivo:
        usuarios = json.load(archivo)
        
    nuevo_usuario = {
        "nombre" : input("Ingrese el nombre: "),
        "contrasena" : input("Ingrese la contraseña: ")
    }
    
    usuarios.append(nuevo_usuario)
    
    with open(base_datos, "w") as archivo:
        json.dump(usuarios, archivo, indent=len(nuevo_usuario)+2)

def editar_usuario():
    with open(base_datos, "r") as archivo:
        usuarios = json.load(archivo)
    
    nombre = input("Ingrese el nombre del usuario que desea editar: ")
    
    for usuario in usuarios:
        if nombre == usuario.get("nombre"):
            if verif_contra(usuario, 3):
                
                while True:
                    print("Qué atributo quiere cambiar?")
                    for clave in usuario.keys():
                        print(clave)
                    clave_cambiar = input("").lower()
                    if clave_cambiar in usuario.keys():
                        print("Qué valor desea ponerle? ")
                        usuario[clave_cambiar] = input("")
                        print(f"Se cambió el valor del atributo {clave_cambiar}")
                    else:
                        print("Ese atributo no existe")
                        
                    while True:
                        respuesta = input("Desea cambiar otro atributo? (y/n)\n").lower()
                        if not (respuesta == "n" or respuesta == "y"):
                            print("Respuesta no válida")
                        break     
                    if respuesta == "n":
                        break
            else:
                break
    else:
        print("Usuario no existente")
    
    with open(base_datos, "w") as archivo:
        json.dump(usuarios, archivo, indent=len(usuarios[0])+2)

def mostrar_usuarios():
    with open(base_datos, "r") as archivo:
        usuarios = json.load(archivo)
    for usuario in usuarios:
        print(f"Usuario: {usuario.get('nombre')}")

def eliminar_usuario():
    with open(base_datos, "r") as archivo:
        usuarios = json.load(archivo)
    
    nombre = input("Ingrese el nombre del Usuario a eliminar: ")
    
    for usuario in usuarios:
        if nombre == usuario.get("nombre"):
            if verif_contra(usuario, 3):
               usuarios.remove(usuario)
               print("Usuario Eliminado con éxito")
            break
    else:
        print("Usuario no existente")
    
    with open(base_datos, "w") as archivo:
        json.dump(usuarios, archivo, indent=len(usuarios[0])+2)

while True:
    print("1. agregar usuario \n 2. editar un usuario \n 3. eliminar un usuario \n 4. Mostrar usuarios \n 5. Salir")
    request = input("\nQué acción desea hacer?\n").lower()
    if request == "1":
        agregar_usuario()
    elif request == "2":
        editar_usuario()
    elif request == "3":
        eliminar_usuario()
    elif request == "4":
        mostrar_usuarios()
    elif request == "5":
        break
    else:
        print("Opción no válida")