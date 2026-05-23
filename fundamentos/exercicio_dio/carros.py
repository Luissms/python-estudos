from datetime import datetime
from typing import List, Optional


class Carro:
    """Classe que representa um carro no inventário"""
    
    def __init__(self, id: int, marca: str, modelo: str, ano: int, preco: float, quantidade: int):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.quantidade = quantidade
    
    def __str__(self):
        return f"ID: {self.id} | {self.ano} {self.marca} {self.modelo} | R$ {self.preco:.2f} | Estoque: {self.quantidade}"


class Venda:
    """Classe que registra uma venda de carro"""
    
    def __init__(self, id: int, carro: Carro, quantidade: int, valor_total: float):
        self.id = id
        self.carro = carro
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.data_venda = datetime.now()
    
    def __str__(self):
        return f"ID: {self.id} | {self.carro.marca} {self.carro.modelo} | Qtd: {self.quantidade} | Total: R$ {self.valor_total:.2f} | Data: {self.data_venda.strftime('%d/%m/%Y %H:%M')}"


class Concessionaria:
    """Classe que representa uma concessionária de carros"""
    
    def __init__(self, nome: str):
        self.nome = nome
        self.carros: List[Carro] = []
        self.vendas: List[Venda] = []
        self.proximo_id_carro = 1
        self.proximo_id_venda = 1
    
    def adicionar_carro(self, marca: str, modelo: str, ano: int, preco: float, quantidade: int) -> bool:
        """Adiciona um novo carro ao inventário"""
        if preco <= 0 or quantidade < 0 or ano < 1886:
            print("❌ Erro: Dados inválidos do carro!")
            return False
        
        novo_carro = Carro(self.proximo_id_carro, marca, modelo, ano, preco, quantidade)
        self.carros.append(novo_carro)
        self.proximo_id_carro += 1
        print(f"✅ Carro '{marca} {modelo}' adicionado com sucesso!")
        return True
    
    def listar_carros(self) -> None:
        """Lista todos os carros disponíveis"""
        if not self.carros:
            print("📋 Nenhum carro cadastrado no inventário.")
            return
        
        print("\n" + "="*80)
        print(f"{'INVENTÁRIO DE CARROS - ' + self.nome:^80}")
        print("="*80)
        for carro in self.carros:
            print(carro)
        print("="*80 + "\n")
    
    def buscar_carro(self, id: int) -> Optional[Carro]:
        """Busca um carro pelo ID"""
        for carro in self.carros:
            if carro.id == id:
                return carro
        return None
    
    def vender_carro(self, id_carro: int, quantidade: int) -> bool:
        """Realiza a venda de um carro"""
        carro = self.buscar_carro(id_carro)
        
        if not carro:
            print(f"❌ Erro: Carro com ID {id_carro} não encontrado!")
            return False
        
        if quantidade <= 0:
            print("❌ Erro: Quantidade deve ser maior que zero!")
            return False
        
        if carro.quantidade < quantidade:
            print(f"❌ Erro: Estoque insuficiente! Disponível: {carro.quantidade}")
            return False
        
        valor_total = carro.preco * quantidade
        nova_venda = Venda(self.proximo_id_venda, carro, quantidade, valor_total)
        self.vendas.append(nova_venda)
        carro.quantidade -= quantidade
        self.proximo_id_venda += 1
        
        print(f"✅ Venda realizada com sucesso!")
        print(f"   {carro.marca} {carro.modelo} | Qtd: {quantidade} | Total: R$ {valor_total:.2f}")
        return True
    
    def listar_vendas(self) -> None:
        """Lista todas as vendas realizadas"""
        if not self.vendas:
            print("📋 Nenhuma venda realizada ainda.")
            return
        
        print("\n" + "="*80)
        print(f"{'HISTÓRICO DE VENDAS - ' + self.nome:^80}")
        print("="*80)
        for venda in self.vendas:
            print(venda)
        print("="*80 + "\n")
    
    def gerar_relatorio(self) -> None:
        """Gera um relatório de vendas"""
        if not self.vendas:
            print("📊 Nenhuma venda para gerar relatório.")
            return
        
        total_vendido = sum(venda.valor_total for venda in self.vendas)
        quantidade_vendida = sum(venda.quantidade for venda in self.vendas)
        
        print("\n" + "="*80)
        print(f"{'RELATÓRIO DE VENDAS - ' + self.nome:^80}")
        print("="*80)
        print(f"Total de vendas: {len(self.vendas)}")
        print(f"Quantidade de carros vendidos: {quantidade_vendida}")
        print(f"Valor total em vendas: R$ {total_vendido:.2f}")
        print(f"Ticket médio: R$ {total_vendido / len(self.vendas):.2f}")
        print("="*80 + "\n")


def menu_principal():
    """Exibe o menu principal da aplicação"""
    concessionaria = Concessionaria("AutoMax")
    
    # Dados iniciais
    concessionaria.adicionar_carro("Toyota", "Corolla", 2023, 120000.00, 5)
    concessionaria.adicionar_carro("Honda", "Civic", 2023, 130000.00, 3)
    concessionaria.adicionar_carro("Volkswagen", "Gol", 2022, 90000.00, 8)
    concessionaria.adicionar_carro("Ford", "Focus", 2023, 125000.00, 4)
    concessionaria.adicionar_carro("Hyundai", "HB20", 2023, 85000.00, 6)
    
    while True:
        print("\n" + "="*50)
        print(f"{'CONCESSIONÁRIA ' + concessionaria.nome:^50}")
        print("="*50)
        print("1. Listar carros disponíveis")
        print("2. Vender carro")
        print("3. Listar vendas realizadas")
        print("4. Gerar relatório de vendas")
        print("5. Adicionar novo carro")
        print("6. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            concessionaria.listar_carros()
        
        elif opcao == "2":
            try:
                id_carro = int(input("Digite o ID do carro: "))
                quantidade = int(input("Digite a quantidade: "))
                concessionaria.vender_carro(id_carro, quantidade)
            except ValueError:
                print("❌ Erro: Entrada inválida!")
        
        elif opcao == "3":
            concessionaria.listar_vendas()
        
        elif opcao == "4":
            concessionaria.gerar_relatorio()
        
        elif opcao == "5":
            try:
                marca = input("Marca do carro: ").strip()
                modelo = input("Modelo: ").strip()
                ano = int(input("Ano: "))
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                concessionaria.adicionar_carro(marca, modelo, ano, preco, quantidade)
            except ValueError:
                print("❌ Erro: Entrada inválida!")
        
        elif opcao == "6":
            print("👋 Até logo!")
            break
        
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()
