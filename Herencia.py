class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


    def hablar(self):
        print('hola, estoy hablando poco')
        pass

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    pass
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad) -> None:
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

    pass


roberto = Empleado('roberto', 43, 'peruano', 'Security', 1000)

roberto.hablar()