# Write code below 💖

# Inicializamos las variables de puntos para cada casa
Gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0

# Función para hacer preguntas
def hacer_pregunta(pregunta, opciones_validas, asignacion_puntos):
    respuesta_valida = False
    while not respuesta_valida:
        try:
            respuesta = int(input(pregunta))
            if respuesta in opciones_validas:
                respuesta_valida = True  # Cambiamos la condición para salir del bucle
                for casa, puntos in asignacion_puntos[respuesta].items():
                    globals()[casa] += puntos
            else:
                print(f"Te equivocaste! Responde nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Preguntas
hacer_pregunta("""
Q1) ¿Qué prefieres, el amanecer o el atardecer?
    1) Amanecer
    2) Atardecer""", 
    [1, 2],
    {1: {"Gryffindor": 1, "Ravenclaw": 1}, 2: {"Slytherin": 1, "Hufflepuff": 1}}
)

hacer_pregunta("""
Q2) ¿Qué habilidad preferirías tener?
    1) Hablar con los animales
    2) Leer la mente
    3) Volar
    4) Transformarte en otra persona""", 
    [1, 2, 3, 4],
    {1: {"Hufflepuff": 1}, 2: {"Ravenclaw": 1}, 3: {"Gryffindor": 1}, 4: {"Slytherin": 1}}
)

hacer_pregunta("""
Q3) ¿Qué tipo de persona te inspira más?
    1) Alguien valiente y decidido
    2) Alguien ambicioso y estratégico""", 
    [1, 2],
    {1: {"Gryffindor": 1, "Ravenclaw": 1}, 2: {"Slytherin": 1, "Hufflepuff": 1}}
)

hacer_pregunta("""
Q4) ¿Qué lugar del castillo de Hogwarts te atrae más?
    1) La torre de astronomía
    2) El invernadero
    3) La sala común
    4) El bosque prohibido""", 
    [1, 2, 3, 4],
    {1: {"Ravenclaw": 1}, 2: {"Hufflepuff": 1}, 3: {"Gryffindor": 1}, 4: {"Slytherin": 1}}
)

hacer_pregunta("""
Q5) Si tuvieras una mascota mágica, ¿cuál elegirías?
    1) Búho
    2) Gato""", 
    [1, 2],
    {1: {"Ravenclaw": 1, "Slytherin": 1}, 2: {"Gryffindor": 1, "Hufflepuff": 1}}
)

hacer_pregunta("""
Q6) ¿Cómo reaccionarías si alguien insulta a un amigo?
    1) Lo confrontas directamente
    2) Tratas de calmar la situación
    3) Ignoras el comentario
    4) Buscas una manera sutil de vengarte""", 
    [1, 2, 3, 4],
    {1: {"Gryffindor": 1}, 2: {"Hufflepuff": 1}, 3: {"Ravenclaw": 1}, 4: {"Slytherin": 1}}
)

hacer_pregunta("""
Q7) ¿Qué elegirías si pudieras obtener solo uno de estos objetos mágicos?
    1) La capa de invisibilidad
    2) La varita de saúco""", 
    [1, 2],
    {1: {"Ravenclaw": 1, "Hufflepuff": 1}, 2: {"Gryffindor": 1, "Slytherin": 1}}
)

hacer_pregunta("""
Q8) ¿Qué actividad disfrutas más?
    1) Resolver acertijos
    2) Ayudar a tus amigos
    3) Explorar lugares nuevos
    4) Planear tu próximo movimiento""", 
    [1, 2, 3, 4],
    {1: {"Ravenclaw": 1}, 2: {"Hufflepuff": 1}, 3: {"Gryffindor": 1}, 4: {"Slytherin": 1}}
)

hacer_pregunta("""
Q9) ¿Cómo prefieres pasar tu tiempo libre?
    1) Leyendo libros interesantes
    2) Compartiendo con tus amigos""", 
    [1, 2],
    {1: {"Ravenclaw": 1, "Slytherin": 1}, 2: {"Gryffindor": 1, "Hufflepuff": 1}}
)

hacer_pregunta("""
Q10) Si pudieras viajar en el tiempo, ¿qué harías?
    1) Ir al pasado para corregir errores
    2) Ir al futuro para explorar el mundo
    3) Vivir el presente plenamente
    4) Usar el tiempo como herramienta estratégica""", 
    [1, 2, 3, 4],
    {1: {"Hufflepuff": 1}, 2: {"Ravenclaw": 1}, 3: {"Gryffindor": 1}, 4: {"Slytherin": 1}}
)

# Resultados
print(f"""
Resultados finales:
Gryffindor: {Gryffindor}
Hufflepuff: {Hufflepuff}
Ravenclaw: {Ravenclaw}
Slytherin: {Slytherin}
""")
