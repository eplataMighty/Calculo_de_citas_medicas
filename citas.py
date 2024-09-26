from datetime import datetime, timedelta
import pytz

# Definimos los doctores con sus especialidades y horarios de atención.
doctores = {
    1: {"nombre": "Dr. Pérez", "especialidad": "Cardiología", "inicio": "08:00", "fin": "10:00"},
    2: {"nombre": "Dr. López", "especialidad": "Dermatología", "inicio": "09:00", "fin": "11:00"}
}

# Lista vacía para almacenar las citas agendadas
citas_agendadas = []

# Definimos la zona horaria UTC y PST
utc = pytz.utc
pst = pytz.timezone('US/Pacific')

# Función para convertir una cadena de texto que representa la hora en un objeto datetime (sin zona horaria)
def convertir_hora(hora_str):
    return datetime.strptime(hora_str, "%H:%M").time()

# Función para obtener las franjas horarias disponibles para un doctor y una duración específica de la cita
def obtener_franjas_disponibles(doctor, duracion_cita):
    # Convertimos las horas de inicio y fin del doctor a objetos datetime completos en UTC
    hoy = datetime.now().date()
    inicio = utc.localize(datetime.combine(hoy, convertir_hora(doctor["inicio"])))
    fin = utc.localize(datetime.combine(hoy, convertir_hora(doctor["fin"])))
    intervalo = timedelta(minutes=duracion_cita)

    franjas = []
    while inicio + intervalo <= fin:
        franjas.append((inicio, inicio + intervalo))
        inicio += intervalo

    # Filtramos y eliminamos las franjas ya ocupadas por citas agendadas
    for cita in citas_agendadas:
        if cita["DoctorId"] == doctor["nombre"]:
            # Las citas ya deben estar en UTC, por lo que no es necesario hacer otra conversión
            franjas = [(start, end) for start, end in franjas if not (cita["start"] < end and start < cita["end"])]

    return franjas

# Función para agendar una cita para un paciente con un doctor en una franja horaria específica
def agendar_cita(paciente, doctor_id, duracion_cita):
    doctor = doctores[doctor_id]
    franjas = obtener_franjas_disponibles(doctor, duracion_cita)

    if franjas:
        print(f"\nHorarios disponibles para {doctor['nombre']} ({doctor['especialidad']}):")
        for i, (start, end) in enumerate(franjas, 1):
            start_pst = start.astimezone(pst)
            end_pst = end.astimezone(pst)
            print(f"{i}. {start_pst.strftime('%H:%M')} - {end_pst.strftime('%H:%M')} PST")

        seleccion = int(input("Selecciona una franja: ")) - 1
        start, end = franjas[seleccion]

        # Convertimos las horas de UTC a PST
        start_pst = start.astimezone(pst)
        end_pst = end.astimezone(pst)

        # Agregamos la cita a la lista, asegurándonos de que todas las fechas sean en UTC
        citas_agendadas.append({"Paciente": paciente, "DoctorId": doctor["nombre"], "start": start, "end": end})
        print(f"Cita agendada para {paciente} con {doctor['nombre']} de {start_pst.strftime('%Y-%m-%d %I:%M %p')} a {end_pst.strftime('%Y-%m-%d %I:%M %p')} PST")
    else:
        print(f"No hay horarios disponibles para {doctor['nombre']}.")

# Función para imprimir todas las citas que han sido agendadas
def imprimir_citas():
    if citas_agendadas:
        print("\n--- Citas Agendadas ---")
        for cita in citas_agendadas:
            start_pst = cita["start"].astimezone(pst)
            end_pst = cita["end"].astimezone(pst)
            print(f"{cita['Paciente']} con {cita['DoctorId']} de {start_pst.strftime('%Y-%m-%d %I:%M %p')} a {end_pst.strftime('%Y-%m-%d %I:%M %p')} PST")
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