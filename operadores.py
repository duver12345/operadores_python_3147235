# Operadores en python
"""
Los operadores en python siguen el siguiente orden jerarquico
1.  (  )
2. **
3. / , *, %,
4. +, -
5. =
NOTA 1: Si hay operaciones en un mismo nivel de jerarquia, 
se resulven de izquiera a derecha
NOTA 2: Si hay parentesis dentro de parentesis se 
resuelve primero el parentesis interno"
""" 
a = 2
b = 3 
c = 7 
x = 5
h = 1
y = c / (x + 2)/(c * a - c + 1 - b * 2)
print(y) 
'''
OPERADORES RELACIONALES:
Las operaciones aritméticas resultan en un valor númerico
las operaciones relacionales resultan en un valor booleano:
True Falso (V, F , si o no)
Operadores Relacionales:
>, <, >=, <=, !=, ==
JERARQUIA DE OPERADORES 
(Incluyendo los relacionales)
1.     ()
2.     **
3.    *,/,%
4.     +,-
5. >, <, >=, <=, !=, ==
6.      =
'''