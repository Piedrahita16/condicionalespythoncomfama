#Toda lista se debe escribir en PLURAL 
arboles=['ceiba','yarumo','manzano','guyacan']
municipios=["Medellin","titiribi","Caronina del principe"]
hectareasembradas=[2500,500,1200]
lluviasMayoresA500=[False,True,True]

#Recorriendo un arreglo 
#Acceder DE UNA FORMA DINAMICA  al contenido de un arreglo 
#ES RECRRRERLO DEBO UTLIZAR UN CICLO O UN BUCLE O LOOP 

#Ciclo while(mientras)
'''contador=0 
while contador<10:
    contador=contador+1
    print("Estoy triunfando.....")'''

#Ciclo for (para)
'''for variableiteradora in range(1,301,2): 
    print(variableiteradora)'''

#Recorrer dinamicamente un arreglo usando un FOREACH (PARA CADA UNO)
for arbol in arboles:   
    print(arbol)

for municipio in municipios:
    print(municipio)
