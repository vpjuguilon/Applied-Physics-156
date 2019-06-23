from numpy import array, pi, dot, diag, arange, sqrt, linspace, cos
from numpy.linalg import inv, eigvals, eig
from matplotlib.pyplot import plot, show, xlabel, ylabel
from cmath import polar, exp
from vpython import rate, sphere, vec


def displacement(S, T, q, w):
    z, p = polar(S*exp(1j*q - 1j*w*T))
    return abs(z)*cos(p)


time = linspace(0, 10, 100)
qmat = [pi]
f = 1
m1 = 0.4
m2 = 1
mode1 = []
s11 = []
s12 = []
s13 = []
s14 = []
mode2 = []
mode3 = []
mode4 = []

eigen1 = []
eigen2 = []
eigen3 = []
eigen4 = []

for q in qmat:
    matrix1 = [[2*f, -f, 0, -f*exp(-1j*q)],
            [-f, 2*f, -f, 0],
            [0, -f, 2*f, -f],
            [-f*exp(1j*q), 0, -f, 2*f]]
    mat1 = array(matrix1, complex)
    massmat = diag([m1, m1, m1, m2])
    mat2 = dot(inv(massmat), mat1)
    mode = 1                                       #MODES 1, 3, 2, 0
    mode1.append(sqrt(eig(mat2)[1][0][mode]))
    mode2.append(sqrt(eig(mat2)[1][1][mode]))
    mode3.append(sqrt(eig(mat2)[1][2][mode]))
    mode4.append(sqrt(eig(mat2)[1][3][mode]))

    eigen1.append(sqrt(abs(eigvals(mat2)[0])))
    eigen2.append(sqrt(abs(eigvals(mat2)[1])))
    eigen3.append(sqrt(abs(eigvals(mat2)[2])))
    eigen4.append(sqrt(abs(eigvals(mat2)[3])))



print(mode1)
print(mode2)
print(mode3)
print(mode4)

""""
displacement1 = displacement(mode1[0], t, 0, 2.24)
displacement2 = displacement(mode2[0], t, 0, 2.24)
displacement3 = displacement(mode3[0], t, 0, 2.24)
displacement4 = displacement(mode4[0], t, 0, 2.24)
"""
"""""
plot(t, displacement1, 'r-')
plot(t, displacement2, 'g.')
plot(t, displacement3, 'b.')
plot(t, displacement4, 'y-')
show()
"""

i, j = 0, 0  # Initial
mass1 = sphere(pos = vec(i, j, 0), radius = 0.5)
mass2 = sphere(pos = vec(i+5, j, 0), radius = 0.5)
mass3 = sphere(pos = vec(i+10, j, 0), radius = 0.5)
mass4 = sphere(pos = vec(i+15, j, 0), radius = 0.5)
t = 1
while True:
    t += 0.1
    rate(20)
    mass1.pos =  vec(i + displacement(mode1[0], t, 0, 2.24), 0,  0)
    mass2.pos = vec(i+5+ displacement(mode2[0], t, 0, 2.24), 0, 0)
    mass3.pos = vec(i+10+ displacement(mode3[0], t, 0, 2.24), 0, 0)
    mass4.pos = vec(i+15+ displacement(mode4[0], t, 0, 2.24), 0, 0)