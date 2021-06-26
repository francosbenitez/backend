class MyClass:
    x = 5
    
p1 = MyClass()
print(p1.x)

#%%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p2 = Person("John", 36)
print(p2.name)
print(p2.age)    

#%%
class Persona:
    def __init__(self, n):
        self.nombre = n 
        self.edad = 0
        
    def imprimir(self):
        print("Nombre: " + self.nombre)

p3 = Persona("Felipe")
print(p3.nombre)
print(p3.edad)

#%%
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def lastimar(self, pts):
        self.salud -= pts

a = Jugador(2, 3)    
b = Jugador(10, 20)
print(a.x, b.x)
print(a.y, b.y)

#%%
"""class Perro:
    genero="Canis"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def imprimir(self):
        return f"(self.nombre) tiene (self.edad) años."
    def ladrar(self, sonido):
        return f"(self.nombre) dice (sonido)."
    def __str__(self) -> st:
        return f"self.nombre) tiene (self.edad) años."
"""

"""
Una clase Cuenta (titular, saldo). Operaciones: depositar, extraer.
Una clase Banco (clientes: cliente1, cliente2, etc., razonSocial)
"""

class Cuenta:

    # Constructor
    # Método especial
    def __init__(self, nom):
        self.titular = nom # Atibuto de instancia
        self.saldo = 0

    # Métodos de instancia
    def depositar(self, importe):
        self.saldo += importe

    def extraer(self, importe):
        estado= True
        if importe>self.saldo:
            estado=False
        else:
            self.saldo -= importe  
        return estado

    # Método especial: str
    def __str__(self):
        return f"Titular: {self.titular} Saldo actual: {self.saldo}"

# Programa principal
cuenta1 = Cuenta("Ramiro")
print(cuenta1)
cuenta1.depositar(1000)
print(cuenta1)
cuenta1.extraer(500)
print(cuenta1)

class Banco:
    def __init__(self, nom):
        self.nombre = nom
        cuenta
        
#%%

    @property
    def saldo(self):
        return self._saldo
