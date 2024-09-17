class Informacion():
        def mi_lista(self):
            lista_Nomperros =["Firulasis","coco","conor"]
            for x in lista_Nomperros:
                print(x)

        def mi_tupla(self):
            tupla_Razaperros =("chaochao","shit zu","pastor aleman")
            for x in tupla_Razaperros:
                print(x)

        def mi_conjunto(self):
            conjunto_marcacarros ={"ford","chevrolet","gmc"}
            for x in conjunto_marcacarros:
                print(x)

        def mi_diccionario(self):
            diccionario_animales ={
            "aracnido":"tarantula",
            "canino":"chihuahua",
            "anfibio":"rana"
            }
            for x,y in diccionario_animales.items():
                print(x,y)

# Creando e objeto

datos = Informacion()

print("\n""-----------------------------------------""\n")
print("LISTADO DE NOMBRE DE PERROS")
datos.mi_lista()

print("\n""-----------------------------------------""\n")
print("TUPLA DE RAZA DE PERROS")
datos.mi_tupla()

print("\n""-----------------------------------------""\n")
print("CONJUNTO DE MARCA DE CARROS")
datos.mi_conjunto()

print("\n""-----------------------------------------""\n")
print("DICCIONARIO DE TIPOS DE ANIMALES")
datos.mi_diccionario()

