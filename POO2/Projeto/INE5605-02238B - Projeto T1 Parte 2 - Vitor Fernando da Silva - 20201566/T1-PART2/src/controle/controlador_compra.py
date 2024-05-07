from src.entidade.item_carrinho import ItemCarrinho
from src.limite.abstract_tela import TipoMensagem
from src.controle.abstract_controlador import AbstractControlador
from src.entidade.compra import Compra
from src.limite.tela_compra import TelaCompra
from pathlib import Path


class FormaPagamentoNaoDefinidaException(Exception):

    def __init__(self) -> None:
        super().__init__("Escolha uma forma de pagamento para poder efetivar a compra")


class ControladorCompra(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema,
            opcoes={
                "1": {"desc": "Efetuar compra", "metodo": self.__opcao_efetuar_compra}
            },
            nome_controlador="Compra"
        )
        self.__tela = TelaCompra()
        self.__compras: list[Compra] = []
        self.__path_arquivo_compras = Path("db/compras.json")
        for compra in self.le_json(self.__path_arquivo_compras):
            self.add_compra(compra)
    
    @property
    def tela(self) -> TelaCompra:
        return self.__tela

    def add_compra(self, info_compra: dict | Compra) -> None:
        if isinstance(info_compra, Compra):
            self.__compras.append(info_compra)
        else:
            self.__compras.append(
                Compra(
                    info_compra["id_compra"],
                    info_compra["id_comprador"],
                    info_compra["valor_total"],
                    info_compra["metodo_pagamento"],
                    info_compra["itens"]
                )
            )
    
    def salvar(self):
        self.salva_json([compra.info_completa for compra in self.__compras], self.__path_arquivo_compras)

    def __escolher_metodo_pagamento(self) -> str:
        self.tela.mostra_msg("Forneça o método de pagamento", tipo_msg=TipoMensagem.TITULO)
        metodo_pagamento = {
            "1": "Boleto",
            "2": "Cartão",
            "3": "Depósito"
        }
            
        metodo_pagamento_escolhido = self.tela.pega_resposta(metodo_pagamento)
        return metodo_pagamento[metodo_pagamento_escolhido]

    def __remover_exemplar_acervo(self, info_acervo, id):
        exemplares = int(info_acervo[id]["exemplares"])
        if exemplares - 1 <= 0:
            del info_acervo[id]
        else:
            info_acervo[id]["exemplares"] = str(exemplares - 1)
    
    def __remover_livro_acervo_usuario(self, item: ItemCarrinho):
        vendedor = self.controlador_sistema.controlador_usuario.pega_usuario(
            lambda usuario: usuario.id == item.id_vendedor
        )
        self.__remover_exemplar_acervo(vendedor.acervo, item.livro.isbn)
    
    def __remover_exemplar_livro_acervo_geral(self, item: ItemCarrinho) -> None:
        """Acessa o acervo geral de livros e remove uma unidade"""
        livro = item.livro 
        self.__remover_exemplar_acervo(
            livro.vendedores, item.id_vendedor
            )


    def __opcao_efetuar_compra(self) -> None:
        """Remove os exemplares comprados do acervo dos vendedores e do acervo geral e 
        salva as informações da compra"""
        
        self.tela.limpa_terminal()
        usuario = self.controlador_sistema.controlador_usuario.usuario_logado
        
        metodo_pagamento = self.__escolher_metodo_pagamento()
        valor_compra = self.controlador_sistema.controlador_carrinho.valor_total_carrinho
        id_comprador = usuario.id
        id_compra = str(len(self.__compras) + 1)
        
        # Guarda o o id do vendedor e o valor de cada livro da compra
        itens_comprados = {}
        
        # Adiciona os livros da compra no dicionário itens_comprados
        # e remove os livros do acervo dos vendedores
        for item in self.controlador_sistema.controlador_carrinho.itens_carrinho:
            # Remove o exemplar comprado do acervo do vendedor
            self.__remover_livro_acervo_usuario(item) 
            # Remove o exemplar do vendedor do acervo geral 
            self.__remover_exemplar_livro_acervo_geral(item)
            # Adiciona a informação ao dicionário
            self.controlador_sistema.controlador_relatorio.add_venda(
                item.id_vendedor,
                item.preco
            )
            itens_comprados.update(item.info_completa)

        # Instância a compra
        compra = Compra(
                id_compra,
                id_comprador,
                valor_compra,
                metodo_pagamento,
                itens_comprados
            )
        
        # Adicona a compra ao sistema
        self.add_compra(
            compra
        )

        # Salva a compra no sistema
        self.salvar()
        
        # Salva as alterações feitas no acervo dos vendedores e no acervo geral
        self.controlador_sistema.controlador_usuario.salvar()
        self.controlador_sistema.controlador_livro.salvar()
        
        self.controlador_sistema.controlador_carrinho.limpa_carrinho()
        self.tela.mostra_msg("Compra efetuada com sucesso!", tipo_msg=TipoMensagem.TITULO)
        self.wait()
        