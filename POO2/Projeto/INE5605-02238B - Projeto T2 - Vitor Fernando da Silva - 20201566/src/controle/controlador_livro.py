from src.controle.abstract_controlador import AbstractControlador
from src.entidade.livro import Livro
from src.dao.livro_dao import LivroDAO
from src.limite.tela_livro import TelaLivro
from typing import Dict, List, Tuple
from bs4 import BeautifulSoup, element
import requests


class InformacaoNaoEncontradaException(Exception):

    def __init__(self, i: str) -> None:
        super().__init__(f"Informação não encontrada -> {i}")     


class ErroAoBuscarInfoLivroException(Exception):

    def __init__(self, isbn: str) -> None:
        super().__init__(f"Não foi possível obter informações do livro {isbn}")


class ControladorLivro(AbstractControlador):


    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        self.__tela = TelaLivro()
        self.__dao = LivroDAO()
    
    @property
    def tela(self) -> TelaLivro:
        return self.__tela 
    
    @property
    def dao(self) -> LivroDAO:
        return self.__dao 
    
    @property
    def dict_entidades(self) -> Dict:
        return {
            livro.titulo: livro for livro in self.dao.cache.values()
        }
    
    def __pega_info_livro_online(self, isbn: str, tentativas: List[bool] = []) -> Dict[str, str]:
        """Retorna informações básicas sobre o livro no site da amazon"""
        def get_html_txt(isbn: str) -> str:
            url = f"https://www.amazon.com.br/dp/{isbn}/"
            
            headers = { 
                "apikey": "3f2f5900-a17c-11ec-b160-618785c5b774"
            }

            params = (("url", url),)
            self.tela.log(f"Obtendo o html da página {url}")
            response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params);

            if response.status_code == 200:
                return response.text   
            raise InformacaoNaoEncontradaException(f"Html da página {url}")

        def get_genero(soup: BeautifulSoup) -> str:
            try:
                genero = soup.find(
                    "div", {"id": "wayfinding-breadcrumbs_feature_div"}
                ).find_all("li")[-1].text.strip()
                return genero
            except:
                return "Livro"
            
        def get_autor(soup: BeautifulSoup) -> str:
            tag: element.Tag or None = soup.find("div", {"class": "authorNameColumn"})
            if tag: return tag.text.strip()
            else:
                for link in soup.select("span.author"):
                    if "(Autor)" in link.text:
                        return link.text.split("(Autor)")[0].strip()
            raise InformacaoNaoEncontradaException("Autor")
        
        def get_editora_e_edicao(soup: BeautifulSoup) -> Tuple:
            try:
                tags = soup.find("div", {"id": "detailBullets_feature_div"})
                if tags:
                    i = tags.find_all("span")[2].text
                    if ";" in i: return i.split(";")
                    return i, "1 Edição"
                for tag in soup.find_all("div", {"class": "a-section rpi-attribute-content"}):
                    if "Editora" in tag.div.span.text:
                        return tag.find_all("span")[-1].text, "1 Edição"
            except Exception:
                raise InformacaoNaoEncontradaException("Editora e Edição")
        
        def get_titulo(soup) -> str:
            titulo = soup.find("span", {"id": "productTitle"})
            if titulo:
                return titulo.text.strip()
            raise InformacaoNaoEncontradaException("Titulo")
        
        try:
            soup = BeautifulSoup(get_html_txt(isbn), "lxml").body
            editora_edicao: Tuple[str, str] = get_editora_e_edicao(soup)
            return {
                "isbn": isbn,
                "titulo": get_titulo(soup),
                "genero": get_genero(soup),
                "autor": get_autor(soup),
                "editora": editora_edicao[0],
                "edicao": editora_edicao[1]
            }
        except Exception as e:
            self.tela.log(f"Erro, tentando novamente. {e}")
            tentativas.append(False)
            if len(tentativas) == 3:
                tentativas.clear()
                raise ErroAoBuscarInfoLivroException(isbn)
            self.wait(3)
            return self.__pega_info_livro_online(isbn)
        
    def get_livro_escolhido_na_listbox(self) -> Livro or None:
        """Mostra uma listbox com todos os livros do sistema e retorna o livro escolhido
        pelo usuário"""
        livros: Dict[str, Livro] = self.dao.get_dict_titulo_livro()
        livro_escolhido: Livro or None = self.tela.get_item_list_box(list(livros.keys()))
        return livros.get(livro_escolhido)

    def novo(self, retornar_entidade_criada: bool = False) -> Livro or None:
        isbn: str or None = self.tela.pega_isbn()
        if isbn:
            try:
                livro: Livro or None = self.dao.get_by_key(isbn)
                if livro is None:
                    self.tela.log("Livro não encontrado no sistema, obtendo informações online")
                    info_livro: Dict[str, str] = self.__pega_info_livro_online(isbn)
                    self.tela.log("Informações encontradas com sucesso!")
                    livro: Livro = Livro(
                        isbn,
                        info_livro["titulo"],
                        info_livro["autor"],
                        info_livro["editora"],
                        info_livro["edicao"],
                        info_livro["genero"]
                    )
                    self.dao.add(livro)
                    self.tela.update_list_box(list(self.dict_entidades.keys()))
                    self.tela.log(f"Livro {livro.key} adicionado ao sistema!")
                    self.tela.popup(f"Livro {livro.titulo} adicionado ao sistema!")
                else:
                    self.tela.log(f"Livro já cadastrado, livro = {livro.titulo}")
                    self.tela.popup(f"Livro já cadastrado, livro = {livro.titulo}")
                
                if retornar_entidade_criada:
                    return livro 

            except Exception as e:
                self.tela.popup(e)
    
    def editar(self, entidade_selecionada: Livro) -> None:
        self.tela.popup("Não é possível editar um livro do acervo")
