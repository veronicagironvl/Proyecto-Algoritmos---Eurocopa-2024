class Equipo:
    def __init__(self, id, nombre, codigo, grupo):
        self.id = id
        self.nombre = nombre
        self.codigo = codigo
        self.grupo = grupo
        
    def __str__(self):
        return f'{self.nombre} ({self.codigo}) - Grupo {self.grupo}'
    