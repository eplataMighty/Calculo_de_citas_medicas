
from datetime import datetime, timedelta

# Definimos los doctores con sus especialidades y horarios de atención.
doctores = {
    1: {"nombre": "Dr. Pérez", "especialidad": "Cardiología", "inicio": "08:00", "fin": "10:00"},
    2: {"nombre": "Dr. López", "especialidad": "Dermatología", "inicio": "09:00", "fin": "11:00"}
}

# Lista vacía para almacenar las citas agendadas
citas_agendadas = []

# Función para convertir una cadena de texto que representa la hora en un objeto datetime
def convertir_hora(hora_str):
    return datetime.strptime(hora_str, "%H:%M")

# Función para obtener las franjas horarias disponibles para un doctor y una duración específica de la cita
def obtener_franjas_disponibles(doctor, duracion_cita):
    # Convertimos las horas de inicio y fin del doctor a objetos datetime
    inicio = convertir_hora(doctor["inicio"])
    fin = convertir_hora(doctor["fin"])
    intervalo = timedelta(minutes=duracion_cita)  # Creamos el intervalo de la duración de la cita
    
    franjas = []  # Lista para almacenar las franjas disponibles
    
    # Calculamos las franjas horarias disponibles
    while inicio + intervalo <= fin:
        franjas.append((inicio, inicio + intervalo))  # Añadimos la franja (inicio, fin) a la lista
        inicio += intervalo  # Avanzamos el tiempo al siguiente intervalo
    
    # Filtramos y eliminamos las franjas ya ocupadas por citas agendadas
    for cita in citas_agendadas:
        if cita["DoctorId"] == doctor["nombre"]:
            franjas = [(start, end) for start, end in franjas if not (cita["start"] < end and start < cita["end"])]
    
    return franjas

# Función para agendar una cita para un paciente con un doctor en una franja horaria específica
def agendar_cita(paciente, doctor_id, duracion_cita):
    doctor = doctores[doctor_id]  # Obtenemos la información del doctor seleccionado
    franjas = obtener_franjas_disponibles(doctor, duracion_cita)  # Obtenemos las franjas disponibles
    
    # Verificamos si hay franjas disponibles
    if franjas:
        # Mostramos las franjas disponibles
        print(f"\nHorarios disponibles para {doctor['nombre']} ({doctor['especialidad']}):")
        for i, (start, end) in enumerate(franjas, 1):
            print(f"{i}. {start.strftime('%H:%M')} - {end.strftime('%H:%M')}")
        
        # El usuario selecciona una franja
        seleccion = int(input("Selecciona una franja: ")) - 1
        start, end = franjas[seleccion]  # Obtenemos la franja seleccionada
        
        # Agregamos la cita a la lista de citas agendadas
        citas_agendadas.append({"Paciente": paciente, "DoctorId": doctor["nombre"], "start": start, "end": end})
        print(f"Cita agendada para {paciente} de {start.strftime('%H:%M')} a {end.strftime('%H:%M')}")
    else:
        print(f"No hay horarios disponibles para {doctor['nombre']}.")

# Función para imprimir todas las citas que han sido agendadas
def imprimir_citas():
    if citas_agendadas:
        print("\n--- Citas Agendadas ---")
        # Recorremos la lista de citas agendadas y las imprimimos
        for cita in citas_agendadas:
            print(f"{cita['Paciente']} con {cita['DoctorId']} de {cita['start'].strftime('%H:%M')} a {cita['end'].strftime('%H:%M')}")
    else:
        print("\nNo hay citas agendadas.")

# Menú principal para agendar citas
def menu():
    while True:
        # Solicitamos al usuario el nombre del paciente
        paciente = input("\nNombre del paciente: ")
        
        # Mostramos los doctores disponibles
        print("\nDoctores disponibles:")
        for id, doc in doctores.items():
            print(f"{id}. {doc['nombre']} ({doc['especialidad']})")
        
        # Solicitamos al usuario que seleccione un doctor
        doctor_id = int(input("Selecciona un doctor: "))
        
        # Solicitamos la duración de la cita
        duracion_cita = int(input("Duración de la cita en minutos: "))
        
        # Agendamos la cita
        agendar_cita(paciente, doctor_id, duracion_cita)
        
        # Preguntamos si desean agendar otra cita
        continuar = input("¿Deseas agendar otra cita? (s/n): ").lower()
        if continuar != 's':
            break
    
    # Imprimimos todas las citas agendadas
    imprimir_citas()

# Ejecutamos el programa llamando al menú principal
menu()
