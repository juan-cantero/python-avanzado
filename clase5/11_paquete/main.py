from model.instancias import persona_1, persona_2, persona_3
from model.persona import Persona


def crear_instancia():
    persona_4 = Persona("Jorge", "Mendoza", 18)
    return persona_4


def listar_personas(instancia: Persona):
    personas = [persona_1, persona_2, persona_3, instancia]
    for persona in personas:
        print(persona.nombre_completo())


def main():
    instancia = crear_instancia()
    listar_personas(instancia)


if __name__ == "__main__":
    main()
