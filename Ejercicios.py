# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 22:53:56 2020

@author: Arturo
"""

import random;

def TestDiccionarios():
    x={}
    y={}
    z={}
    
    x["recuento"]=3
    x["totalMinutos"]=57
    y["recuento"]=2
    y["totalMinutos"]=43
    z["lunes"]=x
    z["martes"]=y
    
    print(z)
    print(z["martes"]["totalMinutos"])

def CreaTiempos(cantidad):
    
    if cantidad<=0:
        return
    
    dias=["L","M","X","J","V","S","D"]
    
    tiempos = dict()
    for i in range (1,cantidad+1):
        dia = (dias[random.randrange(7)])
        tiempo = random.randrange(61)
        tiempos[i] = [dia, tiempo]
    
    # print(tiempos)
    
    return tiempos

TMP = CreaTiempos(10)

print(TMP)

totales=dict()

for registro in TMP:
    # print(TMP[registro][0])
    dia = TMP[registro][0]
    print("Dia ",dia)
    """
    if dia in totales.keys():
        totales[dia] = totales[dia] + 1
    else:
        totales[dia] = 1
    """
    totales[dia] = totales.get(dia,0) + 1
print("Totales ",totales)

TestDiccionarios()