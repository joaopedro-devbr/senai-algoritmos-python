from veiculo import Veiculo

class Carro(Veiculo):
   def __init__(self,marca=None,modelo=None,portas=0):
    super().__init__(marca,modelo)
    self.portas=portas
   def acelerar(self):
      print("Carro acelerando suavemente")