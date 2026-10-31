from carro import Carro
from moto import Moto
from veiculo import Veiculo


def main():
  veiculo=Veiculo("Genérica","Modelo x")
  carro = Carro("Toyota","Corolla",portas=4)
  moto=Moto("Honda","CBR")
  
  veiculo.acelerar()
  carro.acelerar()
  moto.acelerar()
  
if __name__ == "__main__":
  main()
  
