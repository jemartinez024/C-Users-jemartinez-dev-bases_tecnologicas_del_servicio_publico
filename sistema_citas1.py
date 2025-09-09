print("*** Bienvenido al Sistema de Citas ***")

n = 0
i = 0

n = int(input("Ingrese la cantidad de citas a registrar: "))

solicitudes = [] # lista vecia
for i in range (1, n + 1):
    name_solicitante = str(input("Ingrese el Nombre o los Nombres de los Solicitantes: " ))
    time_cita = int(input("Ingrese el tiempo estimado de la solicitud: " ))
    
#solicitudes.append(name_solicitante, time_cita)
solicitudes.append((name_solicitante, time_cita)) # agrega una tupla a la lista
print("Lista de solicitudes ordenadas por tiempo estimado:")

"solicitudes.sort(key=lambda x: x[1]) # ordena la lista por el segundo elemento (tiempo de cita)"

solicitudes.sort() # ordena la lista
print(solicitudes)






