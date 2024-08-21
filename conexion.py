import mysql
import mysql.connector

class conexion():
    def __init__(self,host,user,password,database):
        self.host =  host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database)
    def conectar(self):
        return self.conexion
    
    def cargar_datos_cargo(self):
        bd = self.conectar()
        cursor = bd.cursor()
        sql = "SELECT * FROM `cargo`"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def cargar_datos_gradAcad(self):
        bd = self.conectar()
        cursor = bd.cursor()
        sql = "SELECT * FROM `gradoacademico`"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def cargar_datos_pais(self):
        bd = self.conectar()
        cursor = bd.cursor()
        sql = "SELECT * FROM `pais`"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def cargar_datos_parentezco(self):
        bd = self.conectar()
        cursor = bd.cursor()
        sql = "SELECT * FROM `parentezco`"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def consult_personal_data(self,id):
        try:
            bd = self.conectar()
            cursor = bd.cursor()
            sql = "SELECT * FROM `empleado` WHERE `idEmp` = %s"
            cursor.execute(sql,(id,))
            results = cursor.fetchall()
            return results[0] if results else {"respuesta":False,"Mensaje":"Error: Empleado no existe."}
        except Exception as ex:
            bd.close()
            return {"respuesta":False,"Mensaje":"Error: " + str(ex)}
        
    def consult_laboral_data(self,id):
        try:
            bd = self.conectar()
            cursor = bd.cursor()
            sql = "SELECT * FROM `laboral` WHERE `idEmp` = %s"
            cursor.execute(sql,(id,))
            results = cursor.fetchall()
            return results[0] if results else {"respuesta":False,"Mensaje":"Error: Empleado no existe."}
        except Exception as ex:
            bd.close()
            return {"respuesta":False,"Mensaje":"Error: " + str(ex)}
        
    def consult_familiar_data(self,id):
        try:
            bd = self.conectar()
            cursor = bd.cursor()
            sql = "SELECT * FROM `familiar` WHERE `idEmp` = %s"
            cursor.execute(sql,(id,))
            results = cursor.fetchall()
            return results if results else {"respuesta":False,"Mensaje":"Error: Empleado no existe."}
        except Exception as ex:
            bd.close()
            return {"respuesta":False,"Mensaje":"Error: " + str(ex)}
    
    def consult_acad_data(self,id):
        try:
            bd = self.conectar()
            cursor = bd.cursor()
            sql = "SELECT * FROM `nivelacademico` WHERE `idEmp` = %s"
            cursor.execute(sql,(id,))
            results = cursor.fetchall()
            return results[0] if results else {"respuesta":False,"Mensaje":"Error: Empleado no existe."}
        except Exception as ex:
            bd.close()
            return {"respuesta":False,"Mensaje":"Error: " + str(ex)}


    