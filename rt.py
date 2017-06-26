from sympy import *
from mpmath import mp, svd
from sympy import Function, Symbol

# calc the pseudoinverse matrix by definition


def pseudoInv(A=Matrix([])):
    tran = A.transpose()
    res = (tran*A).inv()
    return res * tran

A=Matrix([
    [1,1,-1],
    [1,0,0],
    [0,1,1]
])

print A.row(1)

B=pseudoInv(A)

'''
# check:
print B
print A*B, B*A
'''

#try to solve the equation

t = Symbol('t')
x = Function('x')(t)
y = Function('y')(t)
z = Function('z')(t)
print x

F=[x(t),y(t),z(t)]
ode=[x(t).diff(t), y(t).diff(t), z(t).diff(t)]


#dsolve(X-B*X.diff())
