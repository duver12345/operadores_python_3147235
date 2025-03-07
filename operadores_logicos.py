'''
Operadores logicos 
Los operadores logicos son:
and, or , not 
obede las tablas de verdad:

'''

op1 = False
op2 = True
op3 = op1 or op2
print(op3)

#Operador not  
op4 = not op1
print(op4)

'''
JERARQUIA DEFINITIVA DE OPERACIONES
1.              ()
2.              **
3.           *, /, %
4.             + , -
5.     >,<,!=, == , <= , >=
6.              NOT
7.              AND
8.              TRUE
'''
'''
NOTA: Si hay operaciones en el mismo nivel de jerarquia se empieza siempre de izquierda
'''
op1 = False
op2 = True
op3 = False
op4 = True

Resultado = not op1 and (op2 or op3 and not op1) and not op4 

print (Resultado)