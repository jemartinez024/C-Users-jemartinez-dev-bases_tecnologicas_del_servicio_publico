student_list = ["Arturo", "Maria", "Juan", "Luis", "Ana"]
student = str(input("Ingrese el nombre del alumno: "))
if student not in student_list:
    print("Error: El alumno no está en la base de datos.")
    exit()
else:
    print("El alumno está en la lista.")
    print(f"Las calificaciones de {student} son: ")
materias = ["Español", "Matemáticas", "Programacion", "Ingles", "Civismo"]
calificaciones = []
for materia in materias:
    calificacion = float(input(f"Ingrese la calificación de {materia}: "))
    calificaciones.append(calificacion)
promedio = sum(calificaciones) / len(calificaciones)
print("El promedio de calificaciones es:", promedio)
if promedio == 6:
    print("El alumno ha aprobado.")
elif promedio == 9:
    print("El alumno es buen estudiante.")
elif promedio == 10:
    print("Felicidades eres un estudiante ejemplar.")
else:
    print("El alumno ha reprobado.")