# IgemBiorreactor
##Program to model a Fed Batch reactor to produce Rsn-2
**@author: iGEM Math Group**

Producción de Rsn-2 fed-batch

"""

"""

Objectives:

1. Maximize the cell formation rate for constant cell mass yield
u = Umax
2. Mantain the substrate concentration as a value that the cell growth is constant
3. Feed is regulate to Mantain the substrate concentration constant

Assumptions:

1. Feed rate is constant:

Dv/Dt = F

Integrate between v = V0 and t = t1

V = V0 + F*t

2. We assume a quassy steady state, the substrate that enter is consumed:

[Sadd] = [Sconsumed]

3. We assume a sterilize inlet

X0 = 0

Biomass Balance:

d(VX)/dt = F*X0 - FX + rx*V

rx = U*X

Expan the derivated and symplify:

(dV/dt)*X = U*X*V

2. The biomass concentration is not changed with time, but the amount of biommas will keep
changing with time because the volume is changing

dX/dt = 0

dX/dt = d(X/V)/dt

Apply derivated of a division an rearange the equation

dXt/dt = rx

3. The substrate concentration is like the biomass balance:

dSt/dt = F*S0 + (U*Xt)/Yxs

"""

