from bs4 import BeautifulSoup
from urllib import request
class Requisicao:


    def retornaHTML(self, stringUrl):
        htmlRetornado = request.urlopen(stringUrl)
        stringHtml = htmlRetornado.read()
        stringHtml = stringHtml.decode("utf8")
        htmlRetornado.close()
        return stringHtml

    def selecionaUltimaBolsa(self, stringUrl, stringSeletor):
        htmlParseado = BeautifulSoup(self.retornaHTML(stringUrl),'html.parser')
        ultimaPostagem = htmlParseado.select_one(stringSeletor) #encontra o titulo da postagem dentro destas tags
        ultimaPostagem = ultimaPostagem['alt'] #seleciona o texto dentro do atributo alt dentro da ultima postagem
        return ultimaPostagem