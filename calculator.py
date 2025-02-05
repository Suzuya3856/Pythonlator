class Calculadora:
    """Criação de uma classe calculadora
    """
    
    def __init__(self,num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        
    def __str__(self):
        return f"{self.num_1}, {self.num_2}"
    
    def soma(self):
        """método que realiza a soma de um elemento com o outro
        """
        return self.num_1 + self.num_2
    
    def subtracao(self):
        """método que realiza a subtração de um elemento pelo outro
        """
        return self.num_1 - self.num_2
    
    def multiplicacao(self):
        """método que realiza a multiplicação de um elemento pelo outro
        """
        return self.num_1 * self.num_2
    
    def divisao(self):
        """método que realiza a divisão de um elemento pelo outro
        """
        return self.num_1/self.num_2