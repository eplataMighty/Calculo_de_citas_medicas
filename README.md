# Sistema de Agendamiento de Citas Médicas

Este proyecto es un simple sistema de agendamiento de citas médicas donde los pacientes pueden reservar citas con doctores en horarios específicos. El programa permite seleccionar un doctor y agendar una cita en una franja horaria disponible basada en la duración de la cita deseada.

## Funcionalidades
- Agendar citas médicas para pacientes.
- Filtrar horarios disponibles de los doctores.
- Evitar solapamientos de citas ya agendadas.
- Mostrar todas las citas agendadas.

## Estructura de Datos
### Doctores
Cada doctor tiene:
- **nombre**: El nombre del doctor.
- **especialidad**: La especialidad del doctor (Cardiología, Dermatología, etc.).
- **inicio**: La hora de inicio del horario de atención.
- **fin**: La hora de fin del horario de atención.

### Citas Agendadas
Cada cita agendada incluye:
- **Paciente**: El nombre del paciente.
- **DoctorId**: El nombre del doctor con el cual se agendó la cita.
- **start**: La hora de inicio de la cita.
- **end**: La hora de fin de la cita.

## Cómo Funciona
1. El sistema solicita el nombre del paciente.
2. Luego, muestra una lista de doctores disponibles con sus respectivas especialidades.
3. El paciente selecciona un doctor.
4. El sistema solicita la duración de la cita en minutos.
5. Se muestran las franjas horarias disponibles para el doctor seleccionado.
6. El paciente selecciona una franja horaria para agendar la cita.
7. El sistema registra la cita evitando que se solapen citas ya agendadas.
8. Finalmente, muestra la lista completa de citas agendadas al finalizar el programa.

## Ejecución del Programa
Para ejecutar el programa, basta con correr el archivo `citas.py` en cualquier entorno que soporte Python 3. 
El usuario debe seguir las instrucciones del menú interactivo para agendar citas.

www.mightyservices.in

![image](https://github.com/user-attachments/assets/2ad71bd3-7e06-4c2c-ba8b-aeb28d2f2547)
![image](https://github.com/user-attachments/assets/207922f8-52ff-45c7-a34f-7208fbdc802b)






