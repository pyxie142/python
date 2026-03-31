import math
ang = float(input("digite o ângulo que você deseja"))
seno = math.sin(math.radians (ang)) #os valores tem que ser em radianos então usamos o math.radians
cose = math.cos(math.radians (ang))
tang = math.tan(math.radians (ang))
print("O angulo de () tem seno de (:.2f}".format(ang, seno))
print("0 ângulo de {} tem coseno de (:.2f}".format(ang,cose))
print("O angulo de () tem tångente de (:.2f}".format(ang,tang))