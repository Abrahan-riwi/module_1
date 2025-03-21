import os
os.system('clear')


def selected_option_message(options,selected_option):
    print(f'\n{design*52}')
    return print(f' Opcion seleccionada: ✅ {options[selected_option-1]}\n ')

def error_message(option):
    return print(f'❌ La opcion: { option } no es valida.')

def save_student_and_notes(name, notes, save_list, prom, state):
    save_list.append({
        'name': name,
        'notes': notes,
        'prom': round(prom, 2), # Redondear con el promedio a 2 decimales
        'state': state,
    })
    return print(f'\n ✅ El estudiante ha sido guardado correctamente')
    # return print(f'El estudiante: {name} y sus notas: {notes} han sido guardadas correctamente')

def save_notes(note, notes_list):
    notes_list.append(note)

def edit_student_and_notes(students, prom):
    if len(students) > 0:
        for student in students:
            # Actualizar el estado del estudiante según el nuevo umbral
            if float(student["prom"]) >= float(prom):
                student["state"] = "aprobado"
            else:
                student["state"] = "reprobado"
        print(' Lista de estudiantes actualizados ')
        for idx, student in enumerate(students, start=1):
            print(f'{idx}. Nombre: {student["name"]:<4} | Promedio: {student["prom"]:<4.2f} | Estado: {student["state"]:<4}')
    else:
        print('')

opciones = [
    'Registrar estudiantes',
    'Estudiantes registrados',
    'Estudiantes Aprobados',
    'Estudiantes Reprobados',
    'Ver cuantas calificaciones son mayores que un valor en especifico',
    'Establecer nueva nota para aprobar',
    'Salir'
]

design_light = '-'
design = '='
error = '❌'
note_approved = 60
notes = []
students_and_notes = []





while True:
    
    print(f'{design*48}\n Bienvenido al programa para calcular promedios \n{design*48}\n')
    
    for i, opcion in enumerate(opciones, start=1):
        print(f'{i}. {opcion}')
    try:
        selected_option = int(input('\nIngrese la opción a seleccionar: '))
        if selected_option == 1:
            # Variables
            student_notes = []
            cant_notes = 0
            i = 0
            sum_notes = 0

            selected_option_message(opciones, selected_option)
            name = input(' Ingrese el nombre del estudiante: ')
            
            while True:
                try:
                    cant_notes = int(input(' Ingrese la cantidad de notas a ingresar: '))
                    if cant_notes <= 0 or cant_notes > 100:
                        error_message(selected_option)
                        print(f'\n¡¡ Por favor ingresar un numero entre 1 y 100 !!\n')
                    else:
                        print(f'{design*52}')
                        print(f' Ingrese notas entre 0 y 100\n ')
                        break
                        
                except ValueError:
                    print(f'\n ¡¡{error} Por favor ingresar un número valido!!\n')
            
            while i < cant_notes:
                try:
                    note = input(f' Ingresar nota {i+1}: ')
                    if float(note)< 0 or float(note) > 100:
                        print('Por favor ingresar una nota valida')
                    elif str(note[0]) == '-':
                        print('Por favor ingresar una nota valida')
                    else:
                        student_notes.append(note)
                        i+=1
                except ValueError:
                    print(F'La nota {note} no es valida.')
            # promedio = sum_notes / len(student_notes)
            
            # Ciclo for para recorrer la lista de notas y 
            for sum_number in student_notes:
                sum_notes += float(sum_number)
                promedio = (sum_notes / len(student_notes))
                
            state = 'aprobado' if promedio >= note_approved else 'reprobado' #Se usa un ternario el cual verifica la nota para ser aprobado
            save_student_and_notes(name, student_notes, students_and_notes, promedio, state)
            print(f'{design*52}\n')
            
        elif selected_option == 2:
            selected_option_message(opciones, selected_option)
            if len(students_and_notes) == 0:
                print('No hay estudiantes registrados! 🥺')
                print(f'\n{design*52}')
            else:
                print(f'\n{design*52}\n         Lista de Estudiantes registrados           \n{design_light*52}')
                for i, student in enumerate(students_and_notes, start=1):
                    print(f'{i}. Nombre: {student["name"]:<4} | Promedio: {student["prom"]:<4.2f} | Estado: {student["state"]:<4}')

                print(f'{design*52}')
                back_menu = input('\nIngrese un caracater para volver al menu o darle enter\n')   
                continue
                                
        elif selected_option == 3:
            selected_option_message(opciones, selected_option)
            
            if len(students_and_notes) == 0:
                print('No hay estudiantes registrados! 🥺')
                print(f'\n{design*52}')
                
            else:
                for i, student in enumerate(students_and_notes, start=1):
                    state = student['state']
                    if state == 'aprobado':
                        print(f'{i}. Nombre: {student["name"]:<4} | Promedio: {student["prom"]:<4.2f} | Estado: {student["state"]:<4}')
                    else:
                        print('   😨😨😨   No hay estudiantes aprobados   😨😨😨   ')
                        print(f'{design*52}\n')
                        continue
                    
                print(f'{design*52}')
                back_menu = input('\nIngrese un caracater para volver al menu o darle enter\n')   
                continue
        
        elif selected_option == 4:
            selected_option_message(opciones, selected_option)
            
            if len(students_and_notes) == 0:
                print('No hay estudiantes registrados! 🥺')
                print(f'\n{design*52}')
                
            else:
                for i, student in enumerate(students_and_notes, start=1):
                    state = student['state']
                    if state.lower() == 'reprobado':
                        print(f'{i}. Nombre: {student["name"]:<4} | Promedio: {student["prom"]:<4.2f} | Estado: {student["state"]:<4}')
                    else:
                        print('   🎊🎊🎊 No hay estudiantes reprobados :) 🎊🎊🎊   ')
                        print(f'{design*52}\n')
                        continue
                    print(f'{design*52}')
                    back_menu = input('\nIngrese un caracater para volver al menu o darle enter\n')   
                    continue
                
        elif selected_option == 5:
            selected_option_message(opciones, selected_option)
            
            print(len(students_and_notes))
            
# if len(students_and_notes) == 0:  # Verificamos si la lista está vacía
#     print('No hay estudiantes registrados! 🥺')
#     print(f'\n{design*52}')
                
# else:
# while True:
#     try:
#         prueba = input('Ingrese el numero desde el cual seria el limite: ')

#         # Validar el límite
#         if prueba[0] == '-' or int(prueba) < 0 or int(prueba) > 100:
#             print('Por favor ingresar un numero valido entre (0-100)')
#         else:
#             limite = int(prueba)  # Convertimos el valor de prueba a entero

#             print(f'{"ID.":<5} {"NOMBRE":<10} {"NOTAS":>15}\n')

#             found = False  # Para verificar si encontramos alguna nota válida
#             # Recorremos la lista de estudiantes
#             for i, student in enumerate(students_and_notes, start=1):
#                 name = student['name']
#                 notes_st = student['notes']

#                 # Filtrar las notas que son mayores que el límite
#                 filtered_notes = [note for note in notes_st if note > limite]

#                 # Si hay notas que pasan el filtro, las mostramos
#                 if filtered_notes:
#                     notes_str = ' | '.join(str(note) for note in filtered_notes)  # Unimos las notas con un delimitador
#                     print(f'{i:<5} {name:<10} {notes_str:>15}')
#                     found = True  # Encontramos al menos una nota válida

#             if not found:
#                 print(f'No se encontraron notas mayores a {limite} para ningún estudiante.')
#             break  # Salir del bucle ya que el proceso ha terminado

#     except ValueError:
#         print('Por favor, ingrese un valor válido.')
                
        elif selected_option == 6:
            selected_option_message(opciones, selected_option)
            print(f' La nota actual para ser aprobado es {note_approved} \n')
            while True:
                try:                    
                    new_note_approved = input(' Ingrese la nota promedio para aprobar: ')
                    if float(new_note_approved) == float(note_approved):
                        print(f' Esta ingresando el mismo promedio actual que es: {note_approved}')
                    elif float(new_note_approved) <= 0 or str(new_note_approved)[0] == '-':
                        print('\n Ingrese un número positivo por favor !')
                    else:
                        if len(students_and_notes) > 0:
                            edit_student_and_notes(students_and_notes, new_note_approved)
                        print(f' El promedio minimo para aprobar ha sido actualizado a: {new_note_approved}')
                        note_approved = new_note_approved
                        break
                except ValueError:
                    print(' Digitar un numero valido para el promedio')
        else:
            print(f'\nLa opcion: {selected_option} no es valida\nPor favor ingresar una opcion valida!')
            
    except ValueError:
        print('\nSeleccione una opción valida')
