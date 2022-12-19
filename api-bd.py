import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port="3306",
  password="12345678",
  database="company_manage"
)
mycursor = mydb.cursor()



#crear tablas con datos iniciales

#franquicia
def crearTablaFranquicias():
  global mycursor
  mycursor.execute(""" CREATE TABLE franquicias (
  `id_franquicia` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `ganancias_totales` INT NULL,
  `perdidas_totales` INT NULL,
  `descripcion` VARCHAR(400) NULL,
  PRIMARY KEY (`id_franquicia`))""")
  mydb.commit()
  print("tabla franquicia creada")
  
  
def meterDatosIncialesFranquicia():
  global mycursor
  sql = "INSERT INTO franquicias (nombre, ganancias_totales, perdidas_totales, descripcion) VALUES (%s, %s, %s, %s)"
  val = [
    ('Burguer King', 2400000, 300000, 'Fundada en 1954, Burger King es la segunda cadena de hamburguesas de comida rápida más grande del mundo. El hogar original de Whopper, nuestro compromiso con los ingredientes de primera calidad, las recetas exclusivas y las experiencias gastronómicas familiares es lo que ha definido nuestra marca durante más de 50 años exitosos.'),
    ('Telepizza', 2200000, 300000, 'Telepizza nació en Madrid en 1987 como una empresa familiar con claro ímpetu por la innovación y constante foco en la calidad de sus productos. Siendo de esta manera un pionero en el delivery de comida de calidad a casa.'),
    ('Taco Bell', 1900000, 200000,'Desde que en 1977 Taco Bell abrió su primer restaurante internacional en Guam comenzó una política de expansión por el mundo que nos ha llevado a día de hoy a tener más de 6.000 restaurantes en Estados Unidos y más de 500 restaurantes por todo el mundo.')
  ]
  mycursor.executemany(sql, val)
  mydb.commit()
  print("datos iniciales franquicia metidos")




#establecimientos
def crearTablaEstablecimientos():
  global mycursor
  mycursor.execute(""" CREATE TABLE establecimientos (
  `id_establecimiento` INT NOT NULL AUTO_INCREMENT,
  `id_franquicia` INT NOT NULL,
  `ganancias_establecimiento` INT NOT NULL,
  `perdidas_establecimiento` INT NOT NULL,
  `horario` VARCHAR(45) NOT NULL,
  `localizacion` VARCHAR(100) NULL,
  PRIMARY KEY (`id_establecimiento`))
  """)
  mydb.commit()
  print("tabla establecimientos creada")
def meterDatosInicialesEstablecimientos():
  global mycursor
  sql = "INSERT INTO establecimientos (id_franquicia, ganancias_establecimiento, perdidas_establecimiento, horario, localizacion) VALUES (%s, %s, %s, %s,%s)"
  val= [
    (1,40300, 27000, '9:00 - 24:00', 'C. de Isaac Peral, 38, 28015 Madrid'),
    (2,38000, 20000, '11:00 - 23:00', 'C. de Cea Bermúdez, 38, 28003 Madrid'),
    (1,70000, 85000, '9:00 - 24:00', 'C. de la Princesa, 3, 28008 Madrid')
  ]
  mycursor.executemany(sql,val)
  mydb.commit()
  print("datos inciales establecimientos metidos")


#clientes
def crearTablaClientes():
  global mycursor
  mycursor.execute(""" CREATE TABLE clientes (
    `id_cliente` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(30) NOT NULL,
    `apellidos` VARCHAR(60) NOT NULL,
    `edad` INT NOT NULL,
    `sexo` ENUM('masculino','femenino', 'otro') NOT NULL,
    `correo` VARCHAR(45) NOT NULL,
    `telefono` VARCHAR(9) NOT NULL,
    `DNI` VARCHAR(9) NOT NULL,
    `id_franquicia` INT NOT NULL,
    PRIMARY KEY (`id_cliente`))
  """)
  mydb.commit()
  print("tabla clientes creada")
def meterDatosInicialesClientes():
  global mycursor
  sql = "INSERT INTO clientes (nombre, apellidos, edad, sexo, correo, telefono, DNI, id_franquicia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
  val = [
    ('Juan', 'Flores García', 45, 'masculino', 'soyjuanito@gmail.com', '637872543', '04739958Y', 2),
    ('Alma', 'López Méndez', 30, 'femenino', 'almalm09@gmail.com', '682454887', '36625372V', 2),
    ('Fernando', 'San Juan Abad', 23, 'masculino', 'sjafer@gmail.com', '653975746', '94473657Q', 3)
    ]
  mycursor.executemany(sql,val)
  mydb.commit()
  print("datos iniciales clientes metidos")


#reclamaciones
def crearTablaInicialReclamaciones():
  global mycursor
  mycursor.execute(""" CREATE TABLE reclamaciones(
    `id_reclamacion` INT NOT NULL AUTO_INCREMENT,
    `titulo` VARCHAR(100) NOT NULL,
    `fecha_creacion` DATE NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL,
    `estado` ENUM('no resuelta', 'resuelta') NOT NULL, 
    `id_cliente` INT NOT NULL,
    `id_franquicia` INT NOT NULL,
    PRIMARY KEY (`id_reclamacion`))
  """)
  mydb.commit()
  print("tabla reclamaciones creada")
  
def meterDatosIncialesReclamaciones():
  global mycursor
  sql = "INSERT INTO reclamaciones (titulo, fecha_creacion, descripcion, estado, id_cliente, id_franquicia) VALUES (%s, %s, %s, %s, %s, %s)"
  val = [
    ('Encargado maleducado','2022-09-19', 'El encargado además de no hacernos caso y pasar de nosotros bastante veces, fue maleucado y nos hablo de manera soez', 'no resuelta', 3, 1),
    ('Sitio sucio','2022-07-27', 'Nada más entrar nos dimos cuenta de la gran cantidad de suciedad que había, nos quedamos solo porque no había otro sitio cercano para comer', 'resuelta', 4, 1 ),
    ('Comida congelada','2022-08-10', 'Tras 40 minutos de espera por dos simples hamburguesas, llegan totalmente frías y para nada apetecibles', 'resuelta', 5,3 )
  ]
  mycursor.executemany(sql,val)
  mydb.commit()
  print("datos iniciales reclamaciones metidos")
  


#compras
def crearTablaCompras():
  global mycursor
  mycursor.execute(""" CREATE TABLE compras(
    `id_compra` INT NOT NULL AUTO_INCREMENT,
    `producto` VARCHAR(100) NOT NULL,
    `fecha` DATE NOT NULL,
    `precio` FLOAT NOT NULL,
    `id_cliente` INT NOT NULL,
    `id_franquicia` INT NOT NULL,
    PRIMARY KEY (`id_compra`))
  """)
  mydb.commit()
  print("tabla compras creadas")
  
def meterDatosInicialesCompras():
  global mycursor
  sql = "INSERT INTO compras (producto, fecha, precio, id_cliente, id_franquicia) VALUES (%s, %s, %s, %s, %s)"
  val = [
    (' 1menú infantil', '2022-10-25', 11.95, 2, 1),
    ('1 menú adulto extra', '2022-10-26', 14.95, 4, 2),
    ('3 refrescos grandes', '2022-11-19', 4.0, 5, 1)
  ]
  mycursor.executemany(sql, val)
  mydb.commit()
  
def crearTablaDepartamentos():
  global mycursor
  mycursor.execute(""" CREATE TABLE departamentos(
    `id_departamento` INT NOT NULL AUTO_INCREMENT,
    `nombre_departamento` VARCHAR(45) NOT NULL,
    `funcion` VARCHAR(200) NOT NULL,
    `gastos_departamento` INT NOT NULL,
    PRIMARY KEY (`id_departamento`)
  )
  """)
  mydb.commit()
  print("tabla departamentos creada")
  
def meterDatosInicialesDepartamentos():
  global mycursor
  sql = "INSERT INTO departamentos (nombre_departamento, funcion, gastos_departamento) VALUES (%s, %s, %s)"
  val = [
    ('marketing', 'publicidad y capatación de clientes', 6500),
    ('limpieza', 'limpieza y cuidado de los establecimientos', 3000),
    ('productos comida', 'obtener la comida necesaria para hacer la comida que se vende', 900000)
    ]
  mycursor.executemany(sql, val)
  mydb.commit()
  print("datos iniciales departamentos metidos")
  


#incidencias
def crearTablaIncidencias():
  global mycursor
  mycursor.execute(""" CREATE TABLE incidencias(
    `id_incidencia` INT NOT NULL AUTO_INCREMENT,
    `titulo_incidencia` VARCHAR(45) NOT NULL,
    `descripcion` VARCHAR (400) NOT NULL,
    `gravedad` ENUM('alta', 'media', 'baja') NOT NULL,
    `estado_incidencia` ENUM('resuelta', 'no resuelta') NOT NULL,
    `id_empleado` INT NOT NULL,
    PRIMARY KEY (`id_incidencia`)
    )
    """)
  mydb.commit()
  print("tabla incidencias creada")



def meterDatosInicialesIncidencias():
  global mycursor
  sql = "INSERT INTO incidencias (titulo_incidencia, descripcion, gravedad, estado_incidencia, id_empleado) VALUES (%s, %s, %s, %s, %s)"
  val =  [
    ('maquina de freir nuggets averiada', 'una de las máquinas para freir nuggets hace un ruido raro y no coge temperatura', 'media', 'no resuelta', 55),
    ('baldosa rota', 'una de las baldosas de la zona de mesas está rota y hace feo', 'baja', 'no resuelta', 20),
    ('cadena baño de chicas rota', 'la cadena del baño de chicas no traga agua y por lo tanto no es funcional', 'alta', 'resuelta', 25)
  ]
  mycursor.executemany(sql, val)
  mydb.commit()
  print("datos iniciales incidencias metidos")



def crearTablaEmpleados():
  global mycursor
  mycursor.execute("""CREATE TABLE empleados(
    `id_empleado` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(20) NOT NULL,
    `apellidos` VARCHAR(100) NOT NULL,
    `edad` INT NOT NULL, 
    `correo` VARCHAR(100) NOT NULL, 
    `sueldo` INT NOT NULL, 
    `horario` VARCHAR(40) NOT NULL,
    `puesto` VARCHAR(40) NOT NULL,
    `id_franquicia` INT NOT NULL,
    `id_departamento` INT,
    PRIMARY KEY (`id_empleado`)
    )""") 
  mydb.commit()
  print("tabla empleados creada")



def meterDatosInicialesEmpleados():
  global mycursor
  sql = "INSERT INTO empleados (nombre, apellidos, edad, correo, sueldo, horario, puesto, id_franquicia, id_departamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = [
    ('Pedro', 'García Cuesta', 14, 'pedritogarci@gmail.com', 1400, '09:00 - 14:00', 'gestor de marketing y redes sociales', 2, 1 ),
    ('Luis', 'Soles Jímenez', 21, 'solesjimenezluis@gmail.com', 1200, '12:00 - 18:00', 'gestor de marketing y redes sociales', 2, 3 ),
    ('María', 'Pérez Fernández', 45, 'pedritogarci', 1000, '14:30:00 - 20:00', 'gestor de marketing y redes sociales', 2, 5 ),
  ]
  mycursor.executemany(sql, val)
  mydb.commit()
  print("datos iniciales empleados metidos")







######## Parte de usuarios y roles ##################################################################################################################################
#########################################################################################################################################################################

def crearUsuariosYMeterDatosInicialesUsuarios():
  mycursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id_usuario INT AUTO_INCREMENT PRIMARY KEY, nombre_usuario VARCHAR(50), contrasena_usuario VARCHAR(50), rol VARCHAR(50))")
  sql = "INSERT INTO usuarios (nombre_usuario,contrasena_usuario,rol) VALUES (%s, %s, %s)"
  val = [("senior_cangrejo", "dinero", "administrador"),("bob_esponja", "hamburguesa", "basico"),("arenita", "ciencia", "lector")]
  mycursor.executemany(sql, val)
  mydb.commit()
  print("Tabla usuarios con datos iniciales metidos creada")
  
def crearRolesYMeterDatosIniciales():
  mycursor.execute("CREATE TABLE IF NOT EXISTS roles (id_rol INT AUTO_INCREMENT PRIMARY KEY, rol VARCHAR(50))")
  sql = "INSERT INTO roles (rol) VALUES (%s)"
  val = [("administrador",),("basico",),("lector",)]
  mycursor.executemany(sql, val)
  mydb.commit()
  print("Tabla roles con datos iniciales metidos creada")

#####################################################################

#Crear Usuarios
def crearUsuario():
  global listaTabla
  print("Dime el nombre del usuario: ")
  nombreUsuario = input()
  print("Dime la contraseña del usuario: ")
  contrasenaUsuario = input()

  print("Elige el Rol del Usuario, Opciones:")
  mycursor.execute("SELECT rol FROM roles")
  roles = mycursor.fetchall()
  print(roles)
  rolElegido = input()

  sql = "INSERT INTO usuarios (nombre_usuario,contrasena_usuario,rol) VALUES (%s, %s, %s)"
  val = [(nombreUsuario,contrasenaUsuario,rolElegido)]
  mycursor.executemany(sql,val)
  mydb.commit()
  print("Usuario creado")


#Modificar Usuarios
def modificarUsuario():
  mycursor.execute("SELECT nombre_usuario FROM usuarios")
  ListaDatos = mycursor.fetchall()
  print(ListaDatos)

  print("Escribe el Nombre del Usuario que quieras Modificar: ")
  usuario = input()
  mycursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = '" + usuario+"'")
  usuarioInfo = mycursor.fetchall()
  
  
  print("¿Qué deseas modificar? Escribelo tal cual: nombre_usuario, contrasena_usuario o rol")
  print(usuarioInfo)

  campoModificar = input()
  if campoModificar == "nombre_usuario" or campoModificar == "contrasena_usuario" or campoModificar == "rol":
    if campoModificar == "rol":
      mycursor.execute("SELECT rol FROM roles")
      mycursor.fetchall()
      print("Escribe el nuevo rol "+ campoModificar)
      print("Estos son los Roles disponibles que puedes utilizar:")
      mycursor.execute("SELECT rol FROM roles")
      roles = mycursor.fetchall() 
      print(roles)
      nuevoRol = input()
      sql = f"UPDATE usuarios SET rol = '{nuevoRol}' WHERE nombre_usuario = '{usuario}'"
      mycursor.execute(sql)
      print(f"usuario {usuario} modificado correctamente")
    
    elif campoModificar == "contrasena_usuario":
      nuevaContrasena = input("Dime la nueva contraseña: ")
      sql = f"UPDATE usuarios SET contrasena_usuario = '{nuevaContrasena}' WHERE nombre_usuario = '{usuario}'"
      print(sql)
      mycursor.execute(sql)
      print(f"usuario {usuario} modificado correctamente")
      
    elif campoModificar == "nombre_usuario":
      nuevoNombre = input("Introduce el nuevo nombre: ")
      sql = f"UPDATE usuarios SET nombre_usuario = '{nuevoNombre}' WHERE nombre_usuario = '{usuario}'"
      print(sql)
      mycursor.execute(sql)
      print(f"usuario {usuario} modificado correctamente")

      
  else:
    print("Error al modificar usuario")

  mydb.commit()  





def BorrarUsuario():
  print("Escribe el nombre del usuario que quieras Borrar:")
  mycursor.execute("SELECT nombre_usuario FROM usuarios")
  usuarios = mycursor.fetchall()
  print(usuarios)
  usuario = input()
  sql = f"DELETE FROM usuarios WHERE nombre_usuario = '{usuario}'"
  mycursor.execute(sql)
  mydb.commit()




#Crear nuevo rol
def crearRol():
  print("Hay estos roles:")
  mycursor.execute("SELECT Rol FROM Roles")
  roles = mycursor.fetchall() 
  print(roles)
  print("Introduce el nombre del nuevo rol: ")
  nuevoRol = input()
  sql = "INSERT INTO Roles (Rol) VALUES (%s)"
  val = [(nuevoRol,)]
  mycursor.executemany(sql, val)
  mydb.commit()




def borrarRol():
  print("Escribe el rol que quieres borrar: ")
  mycursor.execute("SELECT rol FROM roles")
  roles = mycursor.fetchall()
  print(roles)
  rol = input()
  sql = f"DELETE FROM roles WHERE rol = '{rol}'"
  mycursor.execute(sql)
  mydb.commit()



###########################################################################################



def inicioSesion():
    UsuarioExiste = False
    while (not UsuarioExiste):
      print("Escribe tu Nombre de usuario")
      mycursor.execute("SELECT nombre_usuario, contrasena_usuario, rol FROM usuarios")
      usuarios = mycursor.fetchall()
      print(usuarios)
      usuario = input("Usuario: ")
      contrasena = input("Contraseña: ")
      for i in range(len(usuarios)):
        if str(usuarios[i][0]) == usuario and str(usuarios[i][1]) == contrasena:
          UsuarioExiste = True
          print("Credenciales correctas")
          if str(usuarios[i][2]) == "administrador":
            menuOpcionesAdministrador()
          elif str(usuarios[i][2]) == "basico":
            menuOpcionesBasico()
          elif str(usuarios[i][2]) == "lector":
            menuOpcionesLector()
          else:
            print("El rol de este usuario no hace nada.")
          break
        elif i == len(usuarios)-1:
          print("El usuario o la contrasena NO son correctas, vuelve a intentarlo")
    
  


#########Administrador################################################
def menuOpcionesAdministrador():
  continuar = True
  while(continuar):
    opcionCorrecta = False
    while(not opcionCorrecta):
      
        print("\n \n \n \n =======  MENÚ PRINCIPAL ADMINISTRADOR  =====================")
        print("Elige una opción")
        print("1. Elegir una tabla y MOSTRAR sus DATOS")
        print("2. Elegir una tabla e INSERTAR ")
        print("3. Elegir una tabla y BORRAR sus DATOS")
        print("4. Elegir una tabla y modificar sus DATOS")
        print("5. Crear tabla")
        print("6. Borrar Tabla")
        print("7. Crear Usuarios")
        print("8. Borrar Usuarios")
        print("9. Modificar usuarios")
        print("10. Crear Roles de usuario")
        print("11. Borrar roles")
        print("12. Salir del programa")
        print("===========================================")
        
        
        opcion = int(input("selecciona una opción: "))
        if opcion < 1 or opcion > 13 :
          print("Opción incorreca, introduce otra vez")
        elif opcion == 12:
          continuar = False
          print("Has salido del programa")
          break
        else:
          opcionCorrecta = True
          ejecutarOpcionMenuAdministrador(opcion)
 
        opcionCorrecta = False


def ejecutarOpcionMenuAdministrador(opcion):
  if opcion ==1:
      mostrarDatosTabla()
  elif opcion == 2:
      insertarDatosTabla()
  elif opcion == 3:
    borrarDatosDeUnaTabla()
  elif opcion ==4:
    modificarDatosTabla()
  elif opcion == 5:
    crearNuevaTabla()
  elif opcion == 6:
      borrarTabla()
  elif opcion == 7:
    crearUsuario()
  elif opcion == 8:
   BorrarUsuario()
  elif opcion== 9:
    modificarUsuario()
  elif opcion == 10:
    crearRol()
  elif opcion == 11:
    borrarRol()
    
      

  
######Basico############################################################
def menuOpcionesBasico():
  continuar = True
  while(continuar):
    opcionCorrecta = False
    while(not opcionCorrecta):
      
        print("\n \n \n \n =======  MENÚ PRINCIPAL BASICO =====================")
        print("Elige una opción")
        print("1. Elegir una tabla y MOSTRAR sus DATOS")
        print("2. Elegir una tabla e INSERTAR ")
        print("3. Elegir una tabla y BORRAR sus DATOS")
        print("4. Elegir una tabla y modificar sus DATOS")
        print("5. Salir del programa")
        print("===========================================")
        
        opcion = int(input("selecciona una opción: "))
        if opcion < 1 or opcion > 5 :
          print("Opción incorreca, introduce otra vez")
        elif opcion == 5:
          continuar = False
          print("Has salido del programa")
          break
        else:
          opcionCorrecta = True
          ejecutarOpcionesMenuBasico(opcion)
 
        opcionCorrecta = False


def ejecutarOpcionesMenuBasico(opcion):
  if opcion ==1:
      mostrarDatosTabla()
  elif opcion == 2:
      insertarDatosTabla()
  elif opcion == 3:
    borrarDatosDeUnaTabla()
  elif opcion ==4:
    modificarDatosTabla()
    
    
    
 #####Lector##########################################################
def menuOpcionesLector():
  continuar = True
  while(continuar):
    opcionCorrecta = False
    while(not opcionCorrecta):
      
        print("\n \n \n \n =======  MENÚ PRINCIPAL LECTOR =====================")
        print("Elige una opción")
        print("1. Elegir una tabla y MOSTRAR sus DATOS")
        print("2. Salir del programa")
        print("===========================================")
        
        opcion = int(input("selecciona una opción: "))
        if opcion < 1 or opcion > 2 :
          print("Opción incorreca, introduce otra vez")
        elif opcion == 2:
          continuar = False
          print("Has salido del programa")
          break
        else:
          opcionCorrecta = True
          ejecutarOpcionesMenuBasico(opcion)

        opcionCorrecta = False
      

def ejecutarOpcionesMenuLector(opcion):
    if opcion ==1:
      mostrarDatosTabla()
      
    


##### Funcion ver que tablas hay y será compartida

def mostrarNombreTablas():
  global mycursor
  mycursor.execute("""SHOW TABLES""")
  myresult = mycursor.fetchall()
  print("-----------------------------------------------")
  #print("Existen las siguientes tablas")
  for x in myresult:
    print(x)
  print("-----------------------------------------------")

###########

def mostrarDatosTabla():
  mostrarNombreTablas()
  try:
    tablaParaVerDatos = input("de que tabla quieres ver los datos: ")
    global mycursor
    mycursor.execute(f"""SELECT * FROM {tablaParaVerDatos}""")
    myresult = mycursor.fetchall()
    print("-----------------------------------------------")
    for x in myresult:
      print(x)
    if len(myresult) == 0:
      print(f"La tabla está {tablaParaVerDatos} está vacía")
    print("-----------------------------------------------")
  except:
    print(f"La tabla {tablaParaVerDatos} no existe")




def insertarDatosTabla():
  mostrarNombreTablas()

  tablaParaInsertarDatos = input("en qué tabla quieres insertar datos: ")
  numeroDatosInsertar = int(input("¿cuantos elementos nuevos quieres insertar?: \n"))
  print("cada elemento nuevo tiene que tener los siguientes atributos")
  global mycursor
  mycursor.execute(f"""DESCRIBE {tablaParaInsertarDatos}
  """)
  
  tuplaNombreColumnas = mycursor.fetchall()
  for x in tuplaNombreColumnas:
    print(x)
    
  print("")
  longitudCampoDatos = len(tuplaNombreColumnas)

  try:
    print(f"el id_{tablaParaInsertarDatos} se pone solo\n")
    #insertar datos
    indiceDatoNuevo = 1
    while indiceDatoNuevo <= numeroDatosInsertar:
      print(f"Introduce los datos del elemento {indiceDatoNuevo}")
      sql = f"INSERT INTO {tablaParaInsertarDatos} ("
      valuesS = ""
      nuevosValores = []
      for x in range (1, longitudCampoDatos):
        print(tuplaNombreColumnas[x][0])
        nuevosValores.append(input())
        sql = sql + str(tuplaNombreColumnas[x][0])
        valuesS = valuesS+"%s" 
        if x < longitudCampoDatos -1:
          sql = sql + ","
          valuesS = valuesS+ ", "
      sql = sql  + ") VALUES (" + valuesS + ")"
      val = nuevosValores
      
      mycursor.execute(sql, val)  
      mydb.commit() 
      print(f"Elmento {indiceDatoNuevo} intrducido correctamente\n")
      indiceDatoNuevo += 1
    
  except: 
    print("Error al insertar datos")
  





def borrarTabla():
  mostrarNombreTablas()
  tablaParaBorrar = input("¿Qué tabla quieres borrar? ")
  try:
    mycursor.execute(f"DROP TABLE {tablaParaBorrar}")
    mydb.commit()
    print(f"tabla {tablaParaBorrar} borrada")
  except:
    print(f"La tabla  {tablaParaBorrar} no existe")





def modificarDatosTabla():
  try:
    mostrarNombreTablas()
    tablaParaModificar = str(input("¿de que tabla quieres modificar datos?: "))
    mycursor.execute(f"SELECT * FROM {tablaParaModificar}")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
    idSeleccionado = input("Qué id quieres modificar?: ")
    mycursor.execute("DESCRIBE " + tablaParaModificar)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x[0])
    campoParaModificar = input(f"Qué campo quieres cambiar del elemento con id {idSeleccionado}?: ")
    nuevoValor = input("Escribe el nuevo valor: ")
    sql = f"UPDATE {tablaParaModificar} SET {campoParaModificar} = '{nuevoValor}' WHERE ID_{tablaParaModificar[:-1]} = {idSeleccionado}"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print(f"Tabla {tablaParaModificar} modificada correctamente")
  except:
    print(f"Error al intentar modificar tabla {tablaParaModificar}")



def borrarDatosDeUnaTabla():
  mostrarNombreTablas()
  try:  
    tablaParaBorrarDatos = input("de que tabla quieres borrar los datos: ")
    numeroElementosEliminar = int(input("¿cuantos elementos quieres eliminar? :  "))
    #muestra informacion tabla
    global mycursor
    mycursor.execute(f"""SELECT * FROM {tablaParaBorrarDatos}""")
    myresult = mycursor.fetchall()
    print("-----------------------------------------------")
    for x in myresult:
        print(x)
    print("-----------------------------------------------")
    
    indiceElementoBorrar = 1
    while indiceElementoBorrar <= numeroElementosEliminar:
    #sql borrar dato de tabla
      id_deElementoBorrar = input("Dime el id del elemento que quieres borrar: ")
      #borro la s del nombre de la tabla para poder usarlo como el nombre del id (id_nombreTablaSinS)
      #el nombre de la tabla en plural y el nombre del id de la clave primaria en singular
      nombreId = tablaParaBorrarDatos[:-1]
      sql = f""" DELETE FROM {tablaParaBorrarDatos}
      WHERE id_{nombreId} = "{id_deElementoBorrar}"
      """
      mycursor.execute(sql)
      mydb.commit()
      indiceElementoBorrar += 1
      print(mycursor.rowcount, "elemento(s) borrado(s)")
  except:
    print("Error al borrar tablas")




def crearNuevaTabla():
    try:
      print("queremos crear nueva tabla")
      nombreTabla = input("Dime el nombre de la tabla: ")
      sql = ' CREATE TABLE '
      sql = sql + nombreTabla + " ("
      print(sql)
      numeroCamposTabla = int(input("¿Cuántos campos tiene la tabla?: "))
      for i in range(numeroCamposTabla):
        campoNombre = input("nuevo campo: ")
        sql = sql+ "`" + campoNombre + "`" + " "
        tipoVariable = input("tipo variable: \n (si es auto incremental escribe AUTO_INCREMENT al lado) \n (si es clave primaria escribe PRIMARY KEY al lado): \n")
        sql = sql + tipoVariable + ", "
      
      #codigo sql obtenido  
      sql = sql[:-2] + ')'
      global mycursor
      mycursor.execute(sql)
      mydb.commit()
      print("Tabla " +  nombreTabla  + " creada correctamente")

    except:
      print("Error al crear la tabla")





#LLAMADA A FUNCIONES
#DESCOMENTAR FUNCIONES EN TU BASE DE DATOS PARA QUE CREEN LAS TABLAS Y SE RELLENEN, una vez creadas comentar las funciones porque sale error de tablas ya creadas
#PARA QUE FUNCIONE EL PROGRAMA NUNCA COMENTAR LA FUNCION INICIOSESION()

print("========================================")

"""
crearTablaFranquicias()
meterDatosIncialesFranquicia()



crearTablaEstablecimientos()
meterDatosInicialesEstablecimientos()



crearTablaClientes()
meterDatosInicialesClientes()



crearTablaInicialReclamaciones()
meterDatosIncialesReclamaciones()



crearTablaCompras()
meterDatosInicialesCompras()



crearTablaDepartamentos()
meterDatosInicialesDepartamentos()


crearTablaIncidencias()
meterDatosInicialesIncidencias()


crearTablaEmpleados()
meterDatosInicialesEmpleados()


crearUsuariosYMeterDatosInicialesUsuarios()
crearRolesYMeterDatosIniciales()

"""
print("---------------------------------------------")

########################################################
###Funcion que siempre tiene que estar ------>##########
########################################################
inicioSesion()