class CrudeSimples:
    def __init__(self):
        self.dados = {}  # Dicionário para armazenar os dados
        self.proximo_id = 1
    
    def criar(self, nome, idade):
        """Create - Adiciona um novo registro"""
        item = {
            'id': self.proximo_id,
            'nome': nome,
            'idade': idade
        }
        self.dados[self.proximo_id] = item
        self.proximo_id += 1
        return item
    
    def listar_todos(self):
        """Read - Lista todos os registros"""
        return list(self.dados.values())
    
    def buscar_por_id(self, id):
        """Read - Busca um registro específico"""
        return self.dados.get(id)
    
    def atualizar(self, id, nome=None, idade=None):
        """Update - Atualiza um registro existente"""
        if id in self.dados:
            if nome:
                self.dados[id]['nome'] = nome
            if idade:
                self.dados[id]['idade'] = idade
            return self.dados[id]
        return None
    
    def deletar(self, id):
        """Delete - Remove um registro"""
        if id in self.dados:
            return self.dados.pop(id)
        return None

# Exemplo de uso
crude = CrudeSimples()

# CREATE
print("1. Criando registros:")
pessoa1 = crude.criar("João", 25)
pessoa2 = crude.criar("Maria", 30)
print(f"Registros criados: {pessoa1}, {pessoa2}")

# READ
print("\n2. Listando todos:")
print(crude.listar_todos())

print("\n3. Buscando por ID 1:")
print(crude.buscar_por_id(1))

# UPDATE
print("\n4. Atualizando registro ID 1:")
crude.atualizar(1, nome="João Silva", idade=26)
print(crude.buscar_por_id(1))

# DELETE
print("\n5. Deletando registro ID 2:")
deletado = crude.deletar(2)
print(f"Deletado: {deletado}")
print(f"Registros restantes: {crude.listar_todos()}")