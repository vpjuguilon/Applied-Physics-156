from sympy import Symbol, solve

vo = Symbol("vo")
vr = Symbol("vr")
ir = Symbol("ir")
ic = Symbol("ic")
il = Symbol("il")
r = Symbol("r")
omega = Symbol("omega")
c = Symbol("c")
l = Symbol("l")
eq1 = (ir*(r + 1/(omega*c*1j) + (omega*l*1j)) + vo - 1,
       vo*(omega*c*1j + 1/(omega*l*1j) + 1/r) - ir)


sol = solve(eq1, (vo, vr, ir, ic, il))
print(sol)
