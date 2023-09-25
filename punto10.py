distancia=float(input("ingrese distancia en KM "))
#las velocidades estabn en kilometros 
Vluz = 299.792
Vsonido = 1235 
V_SSC_Tuatara = 508 
Vbolt = 42

Tluz=float(distancia/Vluz)
print("El tiempo que le tomara a la luz es de " +str(Tluz))
Tsonido=float(distancia/Vsonido)
print("El tiempo que le tomara a el sonido es " +str(Tsonido))
Tssc_tuatara=float(distancia/V_SSC_Tuatara)
print("El tiempo que le tomara al SSC Tuatara es" +str(Tssc_tuatara))
Tbolt=float(distancia/Vbolt)
print("El tiempo que le tomara a usaint bolt es " +str(Tbolt))



