#import math 
#nu = int (input("digite um numero "))
#raiz = math.sqrt(nu)
#print ("a raiz de {} é igual a {} " .format(nu,math.ceil(raiz)))
#print ("a raiz de {} é igual a {} " .format(nu,math.floor(raiz)))

# importando funcionalides especificas
from math import sqrt, ceil, floor
nu = int (input("digite numero "))
raiz = sqrt(nu)
print ("a raiz de {} é igual a {} " .format(nu,ceil(raiz)))