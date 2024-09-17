print("\n")
print("Vercion 2 del constructor")
class Perros :
        # Funcion contructor
    def __init__ (self,color,edad):
            self.color=color
            self.edad=edad

            # Funciones creadas para le usuarios
    def muerde(self):
        print(f"chale el perro me mordio")
            
    def chatperro(self,mensaje):
        print(f"chat perro: {mensaje}")
            
    def chatperra(self,mensajepe):
        print(f"chat perra: {mensajepe}")
            
    def datos(self):
        print(f"chale el perro me mordio {self.color}, edad: {self.edad}")
#crear el objeto
chihuas = Perros("negro",2)
# LLamar a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperro("¿quiere ser mi guuaguuuau?")


