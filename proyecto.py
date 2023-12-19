class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def pina(self, objetivo):
        objetivo.vida -= 5
        print(f"{self.nombre} golpeó a {objetivo.nombre}")

    def patada(self, objetivo):
        objetivo.vida -= 10
        print(f"{self.nombre}pegó patada y tiene {self.vida}")

    def combo(self, objetivo):
        objetivo.vida -= 20
        print(f"{self.nombre}hizo combo y tiene {self.vida}")

    def fatality(self, objetivo):
        objetivo.vida -= 50
        print(f"{self.nombre}hizo fatality y tiene {self.vida}")


p1 = Personaje(input("nombre del jugador 1:"),50)

p2 = Personaje(input("nombre del jugador 2:"),50)

turno = 0
while True:
    if turno % 2 == 0:
        jugador_activo = p1
        objetivo = p2
    else:
        jugador_activo = p2
        objetivo = p1
    print(f"turno de {jugador_activo.nombre}")

    accion = input("ataque:1 pina , 2 patada , 3 combo , 4 fatality")

    if accion == "1":
        jugador_activo.pina(objetivo)
    elif accion == "2":
        jugador_activo.patada(objetivo)
    elif accion == "3":
        jugador_activo.combo(objetivo)
    elif accion == "4":
        jugador_activo.fatality(objetivo)

    print(f"Vida 1 = {p1.vida}")
    print(f"Vida 2 = {p2.vida}")
    turno += 1

    if p2.vida<=0:
        print(f"eljugador {p2.nombre} ha muerto")
        break