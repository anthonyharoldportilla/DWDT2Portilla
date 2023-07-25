class alumno:
    def __init__(self,nombre,apellido,edad,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.nacionalidad=nacionalidad
        self.nota=''
       

    
    def registrarNota(self,notaAlumno):
        self.nota=notaAlumno

if __name__=="__main__":
    alumnoSistema=[]
    comandosSistema=['R','C','P','S','M','X']
    while True:
        comandoInformacion=input("Ingrese un comando :")
        print(f"El comando ingresado es : {comandoInformacion}")
        if comandoInformacion in comandosSistema:
            if comandoInformacion=='R':
                print("Se ingresara un nuevo alumno :")
                nombre=input("Ingrese el nombre del alumno: ")
                apellido=input("Ingrese el apellido del alumno: ")
                edad=input("Ingrese la edad del alumno: ")
                nacionalidad=input("Ingrese la nacionalidad del alumno: ")
                objAlumno=alumno(nombre,apellido,edad,nacionalidad)
                alumnoSistema.append(objAlumno)
            elif comandoInformacion=='P':
                print("Se actualizaran los precios")
                for productoInfo in alumnoSistema:
                    if productoInfo.precioProducto=='':
                        precioProducto= input(f"Ingrese el precio del producto {productoInfo.nombreProducto}:")
                        productoInfo.ingresarPrecio(precioProducto)
            elif comandoInformacion=='M':
                print("Se mostrara los datos de los alumnos")
                print("\n")
                i=0
                for alumnoInfo in alumnoSistema:
                    print(f"Mostrando datos personales del alumno{i}")
                    print(f"Nombre del alumno : {alumnoInfo.nombre}")
                    print(f"Apellido del alumno : {alumnoInfo.apellido}")
                    print(f"Edad del alumno : {alumnoInfo.edad}")
                    print(f"Nacionalidad del alumno : {alumnoInfo.nacionalidad}")
                    i=i+1   
                    print("\n")


            else:
                print("comando de finalizacion")
                break

        else:
            print("Comando incorrecto, vuelva a ingresar :")
        
