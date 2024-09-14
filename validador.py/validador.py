def validar_contraseña(contraseña):
   
#valida si 
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False
    especiales = "!@#$%^&*"

    if len(contraseña) < 8:
        return False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in especiales:
            tiene_especial = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial

contraseña = input("Ingrese su contraseña: ")
if validar_contraseña(contraseña):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")