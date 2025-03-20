import os
os.system('clear')

students_and_notes = []

while True:
    cant_notes = 0
    notes = []
    name_student = ''
    promedio = 0
    
    
    name_student = input('Ingrese el nombre del estudiante: ')
    # Validar que ingrese un numero valido
    while True:
        try:
            cant_notes = int(input('Ingrese la cantidad de notas a evaluar: '))
            
            if cant_notes < 0 or cant_notes > 100:
                print('Ingrese un número valido entre 0 y 100')
            else:
                break
            
        except ValueError:
            print('Por favor ingresar un número valido')
    
    i = 0
    while i < cant_notes:
        try:
            note = float(input(f'Ingrese la nota {i+1}: '))
            
            if note < 0 or note > 100:
                print('Ingrese un número valido entre 0 y 100')
            else:
                notes.append(note)
            
        except ValueError:
            print('Por favor ingresar un número valido')
            
        i+=1
    
    
    students_and_notes.append({
        'name': name_student,
        'notes': notes,
    })
        
    print(f'Array {students_and_notes}')
    
    for student in students_and_notes:
        nick = student['name']
        promedio = 0
        notas_st = student['notes']
        for n in notas_st:
            promedio+=n
            
        print(f'El estudiante: {nick} tiene un promedio de { promedio / len(notas_st)}')
        
        
        