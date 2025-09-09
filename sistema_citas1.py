print("*** Bienvenido al Sistema de Citas ***")

n = 0
i = 0

n = int(input("Ingrese la cantidad de citas a registrar: "))

solicitudes = [] # lista vecia
for i in range (1, n + 1):
    name_solicitante = str(input("Ingrese el Nombre o los Nombres de los Solicitantes: " ))
    time_cita = int(input("Ingrese el tiempo estimado de la solicitud: " ))
    
solicitudes.append(name_solicitante, time_cita) # agregamos a la lista
print(solicitudes)






