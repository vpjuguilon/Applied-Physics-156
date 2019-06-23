from numpy import array, exp, pi, dot, diag, arange, sqrt, linspace
from numpy.linalg import inv, eigvals
from matplotlib.pyplot import plot, show, xlabel, ylabel

a = 1       #length of unit cell/lattice constant
qmat = arange(4*pi/-a, 4*pi/a, 2*pi/(100*a))

k1 = 1
k2 = 1
k3 = 1
k4 = 1


m1 = 0.4
m2 = 0.4
m3 = 0.4
m4 = 0.4

eigen1 = []
eigen2 = []
eigen3 = []
eigen4 = []
mode1 = []
mode2 = []
mode3 = []
mode4 = []

for q in qmat:
    matrix1 = [[        (k4+k1),     -k1,       0, -(k4)*exp(-1j*q*a)],
               [            -k1, (k1+k2),     -k2,                  0],
               [              0,     -k2, (k2+k3),                -k3],
               [-k4*exp(1j*q*a),       0,     -k3,            (k3+k4)]]

    mat1 = array(matrix1, complex)
    massmat = diag([m1, m2, m3, m4])
    mat2 = dot(inv(massmat), mat1)

    eigen1.append(sqrt(abs(eigvals(mat2)[0])))
    eigen2.append(sqrt(abs(eigvals(mat2)[1])))
    eigen3.append(sqrt(abs(eigvals(mat2)[2])))
    eigen4.append(sqrt(abs(eigvals(mat2)[3])))

    mode1.append(sqrt(abs(eigvals(mat2)[0])))
    mode2.append(sqrt(abs(eigvals(mat2)[1])))
    mode3.append(sqrt(abs(eigvals(mat2)[2])))
    mode4.append(sqrt(abs(eigvals(mat2)[3])))

    """
    eigen1.append(sqrt(abs(eigvals(mat2)[0])))
    eigen2.append(sqrt(abs(eigvals(mat2)[1])))
    eigen3.append(sqrt(abs(eigvals(mat2)[2])))
    eigen4.append(sqrt(abs(eigvals(mat2)[3])))
    """

plot(qmat, eigen1, 'k.')
plot(qmat, eigen2, 'k.')
plot(qmat, eigen3, 'k.')
plot(qmat, eigen4, 'k.')
xlabel('q')
ylabel('omega')
show()

