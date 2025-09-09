# Programa para registrar solicitudes con tiempo en horas y minutos
print("*** Bienvenido al Sistema de Citas ***")

n = int(input("Ingrese la cantidad de citas a registrar: "))

solicitudes = [] # lista vecia
for i in range (1, n + 1):
    name_solicitante = str(input(f"Ingrese el nombre del solicitante {i} : " ))
    
    while True:
    
        hour = int(input(f"Ingrese las horas estimadas para la solicitud {i} : "))
        min = int(input(f"Ingrese los minutos estimados para la solicitud {i} : "))
    
        time = hour * 60 + min # # Convertir todo a minutos para poder ordenar fácilmente
        if time <= 120: 
            break
        else:
            print("El tiempo total no debe superar los 120 minutos. Intente nuevamente.")
        
    solicitudes.append((name_solicitante, time)) # # Guardar cada solicitud como tupla (nombre, tiempo en minutos)

solicitudes.sort(key=lambda x: x[1]) # ordena la lista por el segundo elemento (tiempo de cita)
print("Lista de solicitudes ordenadas por tiempo estimado:")

for solicitud in solicitudes:
    name_solicitante = solicitud[0]
    time = solicitud[1]
    hour = time // 60 # Divide time entre 60 y devuelve solo la parte entera (sin decimales).
    min = time % 60 # Devuelve lo que sobra después de dividir entre 60
    print(f"Nombre: {name_solicitante} - Tiempo: {hour}h {min}m")

print("Citas generadas exitosamente")








