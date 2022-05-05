
import sqlite3

def crear_db():
    try:
        con = sqlite3.connect('./mybasededatos.db')
        print("La conexion se ha realizado con exito")
        return con
    except Exception as e:
        print("Ha ocurrido un error", e)

def crear_tabla_jugadores(con):
    try: 
        cursor = con.cursor()
        cursor.execute("create table jugadores(id interger primary key, nombre varchar (100), apellido varchar (100), dorsal interger)")
        con.commit()
        print("La tabla jugadores ha sido creada")
    except Exception as e:
        print("Ha ocurrido un error",e)

def insertar_jugadores(con,datos):
    
    cursor = con.cursor()
    cursor.execute("begin")

    try:

        cursor.execute("insert into jugadores(id,nombre, apellido, dorsal) values(?,?,?,?)", datos)
        con.commit()
        print("El registro ha sido insertado con éxito")
    except Exception as e:
        print("Ha ocurrido un error", e)
        cursor.execute("rollback")


def listar_jugadores(con):
    try:
        cursor = con.cursor()
        cursor.execute("select * from jugadores")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Exception as e:
        print("Ha ocurrido un error", e)

def actualizar_jugadores(con):
    try: 
        cursor = con.cursor()
        cursor.execute("update jugadores set nombre = 'Ronaldo' where id =4")

        con.commit()
        print("Registro actualizado")

    except Exception as e:
        print("Ha ocurrido un error", e)


def eliminar_jugadores(con):
    try:
        cursor = con.cursor()
        cursor.execute("delete from jugadores where id=4")
        con.commit()
        print("Registro eliminado")

    except Exception as e:
        print("Ha ocurrido un error", e)      




con = crear_db()
#crear_tabla_jugadores(con)
datos = (4,"Neymar", "Jr", 7)

insertar_jugadores(con,datos)

actualizar_jugadores(con)
eliminar_jugadores(con)
listar_jugadores(con)



def crear_tabla_rankingjugadores(con):
    try: 
        cursor = con.cursor()
        cursor.execute("create table rankingjugadores(id interger primary key,nombre varchar(100))")
        con.commit()
        print("La tabla rankingjugadores ha sido creada")
    except Exception as e:
        print("Ha ocurrido un error",e)

def insertar_rankingjugadores(con,datos1):
    
    cursor = con.cursor()
    cursor.execute("begin")

    try:

        cursor.execute("insert into rankingjugadores(id, nombre) values(?,?)", datos1)
        con.commit()
        print("El registro ha sido insertado con éxito")
    except Exception as e:
        print("Ha ocurrido un error", e)
        cursor.execute("rollback")


def listar_rankingjugadores(con):
    try:
        cursor = con.cursor()
        cursor.execute("select * from rankingjugadores")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Exception as e:
        print("Ha ocurrido un error", e)

def actualizar_rankingjugadores(con):
    try: 
        cursor = con.cursor()
        cursor.execute("update rankingjugadores set nombre = 'Ronaldo' where id =2")

        con.commit()
        print("Registro actualizado")

    except Exception as e:
        print("Ha ocurrido un error", e)


def eliminar_rankingjugadores(con):
    try:
        cursor = con.cursor()
        cursor.execute("delete from rankingjugadores where id=2")
        con.commit()
        print("Registro eliminado")

    except Exception as e:
        print("Ha ocurrido un error", e)


#crear_tabla_rankingjugadores(con)
datos1 = (3, "Lewandowsky")
insertar_rankingjugadores(con,datos1)
actualizar_rankingjugadores(con)
eliminar_rankingjugadores(con)
listar_rankingjugadores(con)

