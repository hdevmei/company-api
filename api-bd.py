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
def crearTablaFranquicia():
  global mycursor
  mycursor.execute(""" CREATE TABLE franquicia (
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
  sql = "INSERT INTO franquicia (nombre, ganancias_totales, perdidas_totales, descripcion) VALUES (%s, %s, %s, %s)"
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
  
#departamentos
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
  print("datos iniciales incidencias metidos")







####################################################################################


#crearTablaFranquicia()
#meterDatosIncialesFranquicia()



#crearTablaEstablecimientos()
#meterDatosInicialesEstablecimientos()



#crearTablaClientes()
#meterDatosInicialesClientes()



#crearTablaInicialReclamaciones()
#meterDatosIncialesReclamaciones()



#crearTablaCompras()
#meterDatosInicialesCompras()



#crearTablaDepartamentos()
#meterDatosInicialesDepartamentos()


#crearTablaIncidencias()
#meterDatosInicialesIncidencias()


#crearTablaEmpleados()
#meterDatosInicialesEmpleados()


#asignar las claves foráneas a las tablas




#pedir si el usuario quiere ver datos, crear datos, eliminar datos o cambiar datos


def menuOpcionesPrincipal():
  continuar = True
  while(continuar):
    opcionCorrecta = False
    while(not opcionCorrecta):
      
        print("\n \n \n \n =======MENÚ PRINCIPAL=====================")
        print("Elige una opción")
        print("1. Elegir una tabla y MOSTRAR sus DATOS")
        print("2. Elegir una tabla e INSERTAR ")
        print("3. Elegir una tabla y BORRAR sus DATOS")
        print("4. Elegir una tabla y modificar sus DATOS")
        print("5. Crear tabla")
        print("6. Borrar Tabla")
        print("7. Salir del programa")
        print("===========================================")
        opcion = int(input("selecciona una opción: "))
        
        if opcion < 1 or opcion > 7 :
          print("Opción incorreca, introduce otra vez")
        elif opcion == 7:
          continuar = False
          print("Has salido del programa")
          break
        else:
          opcionCorrecta = True
          ejecutarOpcionMenuPrincipal(opcion)



def ejecutarOpcionMenuPrincipal(opcion):
  
  if opcion ==1:
      mostrarDatosTabla()
  elif opcion == 2:
      insertarDatosTabla()
  elif opcion == 6:
      borrarTabla()
      


##### Funcion ver que tablas hay y será compartida

def mostrarNombreTablas():
  global mycursor
  mycursor.execute("""SHOW TABLES""")
  myresult = mycursor.fetchall()
  print("-----------------------------------------------")
  for x in myresult:
    print(x)
  print("-----------------------------------------------")

###########

def mostrarDatosTabla():
  mostrarNombreTablas()
  tablaParaVerDatos = input("de que tabla quieres ver los datos: ")
  global mycursor
  mycursor.execute(f"""SELECT * FROM {tablaParaVerDatos}""")
  myresult = mycursor.fetchall()
  print("-----------------------------------------------")
  for x in myresult:
    print(x)
  print("-----------------------------------------------")




#mal
def insertarDatosTabla():
  mostrarNombreTablas()

  tablaParaInsertarDatos = input("en qué tabla quieres insertar datos: ")
  numeroDatosInsertar = int(input("¿cuantos elementos nuevos quieres insertar?: "))
  print("cada elemento nuevo tiene que tener los siguientes atributos")
  global mycursor
  mycursor.execute(f"""SELECT Column_name
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_NAME = N'{tablaParaInsertarDatos}' ORDER BY ORDINAL_POSITION LIMIT 1
  """)
  tuplaNombreColumnas = mycursor.fetchall()
  #for x in myresult:
  # print(x)
  print(tuplaNombreColumnas)

  longitudCampoDatos = len(tuplaNombreColumnas)
  print(longitudCampoDatos)

  print("Introduce correctamente los atributos de los elementos por orden")
  #insertar datos
  indiceDatoNuevo = 1
  while indiceDatoNuevo <= numeroDatosInsertar:
    
    print(f"Introduce ORDENADAMENTE las propiedades del elemento {indiceDatoNuevo}")
    valoresElementoUsuarioLista = []
    #creamos una lista pero la convertirmos luego a tupla
    campoMetido = 0
    while campoMetido <= longitudCampoDatos-1:
      propiedadNueva = input("Introduce la propiedad nueva: ")
      valoresElementoUsuarioLista.append(propiedadNueva)
      print(valoresElementoUsuarioLista)
      campoMetido += 1
    indiceDatoNuevo += 1
    valoresElementosUsuarioTupla = tuple(valoresElementoUsuarioLista)
    print(valoresElementosUsuarioTupla)
    
    
    
    sql = (f"""INSERT INTO {tablaParaInsertarDatos} {tuplaNombreColumnas} VAlUES {valoresElementosUsuarioTupla}""")
    print(sql)
    mydb.commit()





def borrarTabla():
  print("queremos borrar una tabla")
  tablaParaBorrar = input("¿Qué tabla quieres borrar? ")
  try:
    mycursor.execute(f"DROP TABLE {tablaParaBorrar}")
    mydb.commit
    print("tabla {compras} borrada")
  except:
    print(f"La tabla  {tablaParaBorrar} no existe")
  
  
  
menuOpcionesPrincipal()

