carreras = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas = [
    ("Juan", "Pérez", 38, 0),
    ("Carlos", "Santana", 29, 1),
    ("Raúl", "Sosa", 19, 2)
]

estudiantes = []

for _ in range(5):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = int(input("Ingrese edad: "))
    carrera = int(input("Ingrese carrera (0-Software, 1-Contabilidad, 2-Derecho): "))

    nueva_persona = (nombre, apellido, edad, carrera)
    personas.append(nueva_persona)

for persona in personas:
    nombre, apellido, edad, indice = persona
    
    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carreras[indice]
    }
    
    estudiantes.append(estudiante)

print("\nLista de estudiantes:")
for est in estudiantes:
    print(est)