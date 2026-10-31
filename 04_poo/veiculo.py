class Veiculo:
    def __init__(self, marca=None, modelo=None):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("Acelerando")
