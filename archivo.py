""" Desafíos con Validaciones de Cadenas
1 Verificación de Cadena Alfabética Objetivo: Crear una función que determine si una cadena está compuesta únicamente por 
letras mayúsculas y minúsculas (sin espacios, números ni símbolos).
Restricciones:
 Recorrer la cadena carácter por carácter.
 Comparar los caracteres con los valores ASCII para determinar si son letras.
 No se pueden usar métodos como .isalpha()."""


def funcion_letras(cadena):
    for i in range(len(cadena)):
        #if i == "abcdefghijklmnopqrstywxyz":
        if  "A" <= cadena[i]  <= "Z" or "a" <= cadena[i] <= "z":
             
            print(f"{cadena[i]} Es un string")
        else:
            print(f"{cadena[i]} No es un string")
cadenak = "aa456" 
opa = "elefante"
funcion_letras(cadenak) 
funcion_letras(opa)                      