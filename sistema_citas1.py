print("*** Bienvenido al Sistema de Citas ***")


# Programa para registrar solicitudes con tiempo en horas y minutos

n = int(input("Ingrese la cantidad de citas a registrar: "))

solicitudes = [] # lista vecia
for i in range (1, n + 1):
    name_solicitante = str(input(f"Ingrese el Nombre del Solicitante: {i} " ))
    hour = int(input(f"Ingrese las horas estimadas para la solicitud {i}: "))
    min = int(input(f"Ingrese los minutos estimados para la solicitud {i}: "))
    time = hour * 60 + min # # Convertir todo a minutos para poder ordenar fácilmente
    solicitudes.append((name_solicitante, time)) # agrega una tupla a la lista

solicitudes.sort(key=lambda x: x[1]) # ordena la lista por el segundo elemento (tiempo de cita)
print("Lista de solicitudes ordenadas por tiempo estimado:")

for solicitud in solicitudes:
    name_solicitante = solicitud[0]
    time = solicitud[1]
    hour = time // 60
    min = time % 60
    print(f"Nombre: {name_solicitante} - Tiempo: {hour}h {min}m")
    #print(f"Nombre: {solicitud[0]} - Tiempo: {solicitud[1]}")








