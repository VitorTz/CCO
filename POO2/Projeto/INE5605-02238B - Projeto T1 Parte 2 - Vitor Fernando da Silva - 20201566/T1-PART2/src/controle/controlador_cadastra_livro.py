from distutils.log import info
from src.limite.abstract_tela import TipoMensagem
from src.limite.tela_cadastra_livro import TelaCadastraLivro
from src.controle.abstract_controlador import AbstractControlador
from src.entidade.livro import Livro
from bs4 import BeautifulSoup
from requests_html import HTMLSession


class ErroAoBuscarInfoLivroException(Exception):

    def __init__(self, isbn: str) -> None:
        super().__init__(f"Não foi possível obter informações do livro de isbn {isbn}")


class LivroJaCadastradoException(Exception):

    def __init__(self, livro: str) -> None:
        super().__init__(f"Livro {livro} já cadastrado em sua conta.")


class ControladorCadastraLivro(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema,
            opcoes={
                "1": {"desc": "Cadastrar novo livro", "metodo": self.__opcao_cadastra}
            },
            nome_controlador="Livro"
        )
        self.__tela = TelaCadastraLivro()
        
    
    @property
    def tela(self) -> TelaCadastraLivro:
        return self.__tela
    
    def __pega_info_pelo_isbn(self, isbn, tentativas: list[bool] = []) -> dict:
        """Pega informações sobre o livro no site da amazon"""
        if len(tentativas) == 3:
            raise ErroAoBuscarInfoLivroException(isbn)
        try:
            s = HTMLSession()
            r = s.get(f"https://www.amazon.com.br/dp/{isbn}")            
            r.html.render(sleep=1)
            
            def pega_autor(r):
                soup = BeautifulSoup(r.html.html, "lxml")
                links = soup.select("span.author")
                for i, link in enumerate(links):
                    if "(Autor)" in link.text:
                        return link.text.split("(Autor)")[0].strip()
                
            def pega_editora_edicao(r):
                """
                O nome da editora vem junto com a edição,
                como no exemplo 'Suma; 1ª edição (27 maio 2016)',
                retorna um dicionário com a editora e a edição
                """
                i = r.html.xpath('//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]', first=True).text
                if ";" in i:
                    i = i.split(";")
                    return {
                        "editora": i[0],
                        "edicao": i[1]
                    }
                return {
                    "editora": i,
                    "edicao": "1ª edição"
                }
            autor = pega_autor(r)
            editora_e_edicao = pega_editora_edicao(r)
            titulo = r.html.xpath('//*[@id="productTitle"]', first=True).text        
            genero = r.html.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[5]/span/a', first=True).text

        except Exception as e:
            self.tela.mostra_msg(e)
            tentativas.append(False)
            self.wait(2)            
            return self.__pega_info_pelo_isbn(isbn)
        else:
            tentativas.clear()
            return {
                "titulo": titulo,
                "editora": editora_e_edicao["editora"],
                "edicao": editora_e_edicao["edicao"],
                "autor": autor,
                "genero": genero
            }

    def __opcao_cadastra(self):
        
        self.tela.limpa_terminal()
        self.tela.mostra_msg("Forneça informações sobre o livro", tipo_msg=TipoMensagem.TITULO)

        # Pega o usuário logado
        usuario = self.controlador_sistema.controlador_usuario.usuario_logado
        
        # Carrega os livros no acervo caso ainda não estejam carregados
        
        isbn = self.tela.pega_isbn()

        # Verifica se o livro já está cadastrado no acervo geral de livros
        livro_acervo: Livro | None = self.controlador_sistema.controlador_livro.pega_livro(lambda livro: livro.isbn == isbn)
   
        if livro_acervo and usuario.id in livro_acervo.vendedores.keys():
            raise LivroJaCadastradoException(livro_acervo.titulo)
        
        if livro_acervo is None:
            info_livro = self.__pega_info_pelo_isbn(isbn)
            livro_acervo = self.controlador_sistema.controlador_livro.add_livro(
                {
                    "isbn": isbn,
                    "titulo": info_livro["titulo"],
                    "autor": info_livro["autor"],
                    "editora": info_livro["editora"],
                    "edicao": info_livro["edicao"],
                    "genero": info_livro["genero"],
                    "vendedores": {}
                },
                retorna_livro=True
            )
     

        self.tela.mostra_msg("Informações encontradas:", tipo_msg=TipoMensagem.TITULO)    
        self.controlador_sistema.controlador_livro.tela.mostra_info_livro(livro_acervo.info_completa)
        
        # Pega qtd de exemplares na coleção do usuário e o preço do livro
        exemplares = self.tela.pega_exemplares()
        preco = self.tela.pega_preco_livro()

        # Adiciona preço e exemplares no acervo geral e no arcevo do usuário
        livro_acervo.vendedores[usuario.id] = {"preco": preco, "exemplares": exemplares}
        usuario.acervo[livro_acervo.isbn] = {"preco": preco, "exemplares": exemplares}

        # Salva as informações
        self.controlador_sistema.controlador_livro.salvar()
        self.controlador_sistema.controlador_usuario.salvar()
        
        self.tela.mostra_msg(f"Livro {livro_acervo.titulo} salvo com sucesso!", tipo_msg=TipoMensagem.TITULO)
        self.wait()