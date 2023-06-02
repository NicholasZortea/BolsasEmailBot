from Packages.arquivo import LeArquivo
from Packages.Email import EnviaEmail
from Packages.Requests import Requisicao
class Postagem:
    def verificaUltimaPostagem(self, strURL, strSeletor, strCaminhoArquivo):
        leArquivo = LeArquivo()
        textoDentroDoArquivo = leArquivo.retornaTextoDentroDoArquivo(strCaminhoArquivo)
        requisicao = Requisicao()
        textoDoScrap = requisicao.selecionaUltimaBolsa(strURL, strSeletor)


        if textoDoScrap != textoDentroDoArquivo:
            print("A ultima postagem e diferente da armazenada no arquivo")
            enviaEmail = EnviaEmail()
            enviaEmail.enviaEmail(textoDoScrap)
            modificaArquivo = LeArquivo()
            modificaArquivo.escreveNoArquivo(textoDoScrap, strCaminhoArquivo)
        else:
            print("a ultima postagem ja esta no arquivo")

