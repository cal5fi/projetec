class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


lista_usuarios = [
    Usuario('Abade', 'raphaelabade10@gmail.com', '123'),
    Usuario('zGamezin', 'zgames@gmail.com', 'abc')
]

dict_usuarios = {usuario.email: usuario for usuario in lista_usuarios}


def buscar(email, senha):
    usuario = dict_usuarios.get(email)
    if usuario != None and usuario.senha == senha:
        return usuario
    else:
        return None


def buscar_por_email(email):
    return dict_usuarios.get(email, None)
