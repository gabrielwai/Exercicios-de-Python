'''pessoas = ['Joao', 'Melissa', 33, 25, 'Jorje', 12]

for p in pessoas:
    print(p)

Dessa forma, mostra na tela todos os itens da lista'''
'''from operator import attrgetter, itemgetter
Student = list()
Student.append(['john', 'A', 15])
Student.append(['jane', 'B', 12])
Student.append(['dave', 'B', 10])
print(Student)
sorted(Student, key=attrgetter(0), reverse=False)'''

'''tupla = 1, 5, 7
print(tupla)
if 7 in tupla == False:
    print('Tem na tupla')'''

'''n = int(input('Digite um número float: '))
print(f'{n!a}')'''

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2], reverse= False))
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=attrgetter('age')))