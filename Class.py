class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        
    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')
        
    def mostrar_quartos(self):
        print(f'Esta casa tem {self.quartos} quartos')
    
    def mostrar_banheiros(self):
        print(f'Esta casa tem {self.banheiros} banheiros')
        
    def adicionar_quarto(self):
        print('Esta casa tem {self.quarto} quartos')
        
casa1 = Casa('Azul', 4, 3)
casa2 = Casa('Amarela', 6, 4)

print('\nCasa 1:')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa.adicionar_quarto()

print('\nCasa 2:')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()