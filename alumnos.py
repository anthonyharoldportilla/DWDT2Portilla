class alumnos:
    def __init__(self,nombre,apellido,edad,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.nacionalidad=nacionalidad
        self.nota=''
       
    def registrarNota(self,notaAlumno):
        self.nota=notaAlumno
    
    def obtener_numero(self):
        while True:
            notaAlumno = input(f"Alumno {alumnoInfo.nombre} {alumnoInfo.apellido}, Ingrese nota:")
            if notaAlumno.isnumeric():
                notaValida = int(notaAlumno)
                if 0 <= notaValida <= 20:
                    return notaValida
                else:
                    print("Error: La nota debe estar entre 0 y 20. Inténtalo nuevamente.")
            else:
                print("Error: Ingresa solo números. Inténtalo nuevamente.")



   # def calculoPromedio(notasAlumno,contador):
    #    promedioAlumnos=notasAlumno//contador
     #   return promedioAlumnos
        

if __name__=="__main__":
    alumnoSistema=[]
    comandosSistema=['R','C','P','S','M','X']
    while True:
        print("\n")
        print("Bienvenido al registro de notas")
        print("\n")
        comandoInformacion=input("Ingrese un comando :")
        print(f"El comando ingresado es : {comandoInformacion}")
        if comandoInformacion in comandosSistema:
            if comandoInformacion=='R':
                print("Se ingresara un nuevo alumno :")
                nombre=input("Ingrese el nombre del alumno: ")
                apellido=input("Ingrese el apellido del alumno: ")
                edad=input("Ingrese la edad del alumno: ")
                nacionalidad=input("Ingrese la nacionalidad del alumno: ")
                objAlumno=alumnos(nombre,apellido,edad,nacionalidad)
                alumnoSistema.append(objAlumno)
            elif comandoInformacion=='P':   
                i=0 
                sumaNotas=0
                sumaNotasTotal=0
                for alumnoInfo in alumnoSistema: 
                    sumaNotasTotal= alumnoInfo.nota + sumaNotasTotal
                    #print(f"sumanotas {sumaNotasTotal} y cantidad {i}")
                    i=i+1
                #print(f"sumanotas {sumaNotasTotal} y cantidad {i}")
                valPromedio=sumaNotasTotal//i
                print(f"El promedio de notas para {i} alumnos es : {valPromedio}")
            elif comandoInformacion=='S':   
                i=0 
                sumaNotas=0
                sumaNotasTotal=0
                for alumnoInfo in alumnoSistema: 
                    sumaNotasTotal= alumnoInfo.nota + sumaNotasTotal
                    #print(f"sumanotas {sumaNotasTotal} y cantidad {i}")
                    i=i+1
                #print(f"sumanotas {sumaNotasTotal} y cantidad {i}")
                valSumaNotas=sumaNotasTotal
                print(f"La suma de notas para {i} alumnos es : {valSumaNotas}")
            elif comandoInformacion=='C':
                print("Se actualizaran las notas")
                for alumnoInfo in alumnoSistema:
                    if alumnoInfo.nota=='':                       
                        notavalida=alumnoInfo.obtener_numero() 
                        alumnoInfo.registrarNota(notavalida)
                                                                                          
            elif comandoInformacion=='M':
                print("Se mostrara los datos de los alumnos")
                print("\n")
                i=0
                for alumnoInfo in alumnoSistema:
                    print(f"Mostrando datos personales del alumno{i}")
                    print(f"Nombre del alumno : {alumnoInfo.nombre}")
                    print(f"Apellido del alumno : {alumnoInfo.apellido}")
                    print(f"Edad del alumno : {alumnoInfo.edad}")
                    print(f"Nota del alumno : {alumnoInfo.nota}")
                    print(f"Nacionalidad del alumno : {alumnoInfo.nacionalidad}")
                    i=i+1   
                    print("\n")
            elif comandoInformacion=='X':
               print("Finalizo programa")
               exit()               
            else:
                print("comando de finalizacion")
                break

        else:
            print("Comando incorrecto, vuelva a ingresar :")
        
