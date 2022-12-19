

userList = []


def crearUsuario():
    global userList
    userDic = {"userName": {}, "userPassword": {}, "userRol": {}}
    inputUserName = input("Dime el noombre del usuario: ")
    if len(userList) <= 0:
            userDic["userName"] = inputUserName
            inputUserPassword = input("Introduce la contraseña: ")
            userDic['userPassword'] = inputUserPassword
            inputUserRol = input("Introduce el rol: ")
            userDic['userRol'] = inputUserRol
            userList.append(userDic)
    else:
      for user in userList:
        if user['userName'] != inputUserName:
          userDic['userName'] = inputUserName
          inputUserPassword = input("Introduce la contraseña: ")
          userDic['userPassword'] = inputUserPassword
          inputUserRol = input("Introduce el rol: ")
          userDic['userRol'] = inputUserRol
          userList.append(userDic)
          break;
        elif user['userName'] == inputUserName:
          print("Ese usuario ya existe")
        




def borrarUsuario():
  if len(userList) <= 0:
    print("No hay ningún usuario")
  else:  
    for x in userList:
      print(x["userName"])
    usuarioEliminar = input("Selecciona el usuario que quieres eliminar: ")
    for usuario in userList:
      if usuario['userName'] == usuarioEliminar:
        userList.remove(usuario)
        print(f"Usuario {usuarioEliminar} eliminado correctamente")
        return
    print("No existe")
      
      
      
      
def modificarUsuario():
  usuarioModificar = input("Dime el nombre del usuario que quieres modificar: ")
  for usuario in userList:
    if usuario['userName'] == usuarioModificar:
      atriChange = input("Atributo a cambiar: ")
      valorAtri = input("Valor nuevo: ")
      usuario[atriChange] = valorAtri
      return
  print("Ese usuario no existe")




rolList = []

def crearRolesPredefinidos():
  rolList.append("basico")  
  rolList.append("medio")
  rolList.append("maximo")


def crearRol(): 
  nuevoRol = input("Qué rol nuevo quieres crear?")
  rolList.append(nuevoRol)
  print("Selecciona los permisos que tendrá el nuevo rol: ")
  print("""
        1. Elegir una tabla y MOSTRAR sus datos
        2. Elegir una tabla e INSERTAR DATOS
        3. Elegir una table y BORRAR sus DATOS
        4. Elegir una tablar y MODIFICAR sus DATOS
        5. Crear tabla
        6. Borrar tabla
        """)
  print(rolList)
  
  

def mostrarListaUsuarios():
  print(userList)

"""