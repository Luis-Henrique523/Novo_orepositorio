class Sexualidade():
    
    sexo = 'Masculino'

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def mudar_sexo(cls, nova_identificacao):
        cls.sexo = nova_identificacao
        return nova_identificacao
    
a = Sexualidade('Victoria')
print(a.mudar_sexo('hetero'))
