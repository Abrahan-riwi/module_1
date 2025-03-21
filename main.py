

def selected_option_message(options,selected_option):
    print(f'\n{design*52}')
    return print(f' Opcion seleccionada: ✅ {options[selected_option-1]}\n ')

def error_message(option):
    return print(f'❌ La opcion: { option } no es valida.')

def save_student_and_notes(name, notes, save_list, prom, state):
    save_list.append({
        'name': name,
        'notes': notes,
        'prom': prom,
        'state': state,
    })
    return print(f'\n ✅ El estudiante ha sido guardado correctamente')
    # return print(f'El estudiante: {name} y sus notas: {notes} han sido guardadas correctamente')

def save_notes(note, notes_list):
    notes_list.append(note)

opciones = [
    'Registrar estudiantes',
    'Estudiantes registrados',
    'Estudiantes Aprovados',
    'Estudiantes Reprovados',
    'Establecer nueva nota para aprovar',
    'Salir'
]

design = '='
error = '❌'
note_aproved = 60
notes = []
students_and_notes = []


print(design*48)
print(' Bienvenido al programa para calcular promedios ')
print(f'{design*48}\n')


while True:
    
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
                promedio = sum_notes / len(student_notes)
                
            state = 'aprovado' if promedio >= note_aproved else 'reprovado' #Se usa un ternario el cual verifica la nota para ser aprovado
            save_student_and_notes(name, student_notes, students_and_notes, promedio, state)
            print(f'{design*52}\n')
            
        elif selected_option == 2:
            selected_option_message(opciones, selected_option)
            if len(students_and_notes) == 0:
                print('No hay estudiantes registrados! 🥺')
                print(f'\n{design*52}')
            else:
                print(f'\n{design*52}\n         Lista de Estudiantes registrados           \n{'-'*52}')
                # print(f'{i}. {student["name"]>14} | Promedio: {student["prom"]:.2f>10} | Estado: {student["state"]>10}')
                for i, student in enumerate(students_and_notes, start=1):
                    # print(f'{i}. {student["name"]}')
                    # print(f'{i}. {student["name"]>14} | Promedio: {student["prom"]:.2f>10} | Estado: {student["state"]>10}')
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
                    if state == 'Reprovado':
                        print(f'{i}. Nombre: {student["name"]:<4} | Promedio: {student["prom"]:<4.2f} | Estado: {student["state"]:<4}')
                    else:
                        print('   🎊🎊🎊 No hay estudiantes reprovados :) 🎊🎊🎊   ')
                        print(f'{design*52}\n')
                        continue
                    print(f'{design*52}')
                    back_menu = input('\nIngrese un caracater para volver al menu o darle enter\n')   
                    continue
        
        elif selected_option == 4:
            selected_option_message(opciones, selected_option)
            break
        
        else:
            print(f'\nLa opcion: {selected_option} no es valida\nPor favor ingresar una opcion valida!')
            
    except ValueError:
        print('\nSeleccione una opción valida')
    

# while True:
#     try:
#         cant_notes = int(input('Ingrese la cantidad de notas a evaluar ( 0 a 10 ): '))
#         if cant_notes < 0 or cant_notes > 100:
#             print('')
#     except ValueError:
#         print('')