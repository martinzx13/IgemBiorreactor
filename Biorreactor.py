
#Import Library

import  numpy as np
from scipy.integrate import solve_ivp as solt
import matplotlib.pyplot as plt

#Define the model

def modelRsn (t,C):

    Cs,Cp,Cx = C

    while Cs >= 0:
        #Velocidad de Crecimiento
        Ug     = (Umax*Cs)/(Ks + Cs)
        #Variation in volume
        V      = V0 + Q*t
        #Dilution Rate
        D      = Q/V
        #rate of Biommass production
        rg     = Ug*Cx
        #Velocidad Rxn substrate
        rs     = rg/Yxs
        #Volumetric flow rate
        F1     = (Csf - Cs)*Q
        #Arrangment of yield
        CxV    = ((Csf - Cs)*V + (Cs0 - Csf)*V0 + ((Cx0*V0)/Yxs))
        #Arrangment of production velocity
        rs     = (Ug)*CxV
        #rate of product production
        rp     = Ypx*rg
        #Velocidad biomass
        dCx_dt = (Ug - D)*Cx
        #Velocidad Rxn Sustrato
        dCs_dt = F1 - rs/V
        #Velocidad de Produccion
        dCp_dt = rp - (Cpf - Cp)

        return [dCs_dt,dCx_dt,dCp_dt]

#datos del problema

Q       = 0.166  # mol/s
Umax    = 0.2026 # h^-1
Ks      = 0.194 # g/L
V0      = 3  # L
Yxs     = 0.993
Csf     = 0.0525
Ypx     = 0.4106
Cpf     = 0.6418

#composiciones iniciales

Cs0 = 10
Cx0 = 0.01
Cp0 = 0

c_init  = np.array([Cs0,Cp0,Cx0])
t_lim   = (0 , 100)
t_array = np.linspace(0, 100)


sol     = solt(modelRsn,
                t_lim,
                c_init,
                t_eval=t_array)
                #method = 'Radau')

tiempo = sol.t
concentraciones = sol.y

###################################### Graficas ##################################

figure, axis = plt.subplots()

plt.plot(tiempo, concentraciones[0])
plt.plot(tiempo, concentraciones[1])
plt.plot(tiempo, concentraciones[2])

axis.legend(('Substrate','Biomass','Product'))
axis.set_xlabel('tiempo')
axis.set_ylabel('concentración')
