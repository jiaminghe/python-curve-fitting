import numpy as np # For data manipulation

#this equations are based on the supplemental information of doi: 10.1073/pnas.1908956116, one to four peaks variations were listed. 
def afano(omega, omega0,Gamma,q, int0, C, background):
    epsilon = (omega - omega0)/Gamma
    return background*omega + C + (int0*(q+epsilon)**2)/(1+epsilon**2)

def twofano(omega, omega01,Gamma1,q1, int01, C1, background1,omega02,Gamma2,q2, int02, C2, background2):
    epsilon1 = (omega - omega01)/Gamma1
    epsilon2 = (omega - omega02)/Gamma2
    return background1*omega + C1 + (int01*(q1+epsilon1)**2)/(1+epsilon1**2) + background2*omega + C2 + (int02*(q2+epsilon2)**2)/(1+epsilon2**2)

def threefano(omega,omega01,Gamma1,q1, int01, C1, background1,omega02,Gamma2,q2, int02, C2, background2,omega03,Gamma3,q3, int03, C3, background3):
    epsilon1 = (omega - omega01)/Gamma1
    epsilon2 = (omega - omega02)/Gamma2
    epsilon3 = (omega - omega03)/Gamma3
    return background1*omega + C1 + (int01*(q1+epsilon1)**2)/(1+epsilon1**2) + background2*omega + C2 + (int02*(q2+epsilon2)**2)/(1+epsilon2**2) + background3*omega + C3 + (int03*(q3+epsilon3)**2)/(1+epsilon3**2)

def fourfano(omega,omega01,Gamma1,q1, int01, C1, background1,omega02,Gamma2,q2, int02, C2, background2,omega03,Gamma3,q3, int03, C3, background3, omega04,Gamma4,q4, int04, C4, background4):
    epsilon1 = (omega - omega01)/Gamma1
    epsilon2 = (omega - omega02)/Gamma2
    epsilon3 = (omega - omega03)/Gamma3
    epsilon4 = (omega - omega04)/Gamma4
    return background1*omega + C1 + (int01*(q1+epsilon1)**2)/(1+epsilon1**2) + background2*omega + C2 + (int02*(q2+epsilon2)**2)/(1+epsilon2**2) + background3*omega + C3 + (int03*(q3+epsilon3)**2)/(1+epsilon3**2)+ C4 + (int04*(q4+epsilon4)**2)/(1+epsilon4**2)+background4*omega