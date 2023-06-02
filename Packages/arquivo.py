class LeArquivo:

    def retornaTextoDentroDoArquivo(self, caminhoDoArquivo):
        self.arquivo = open(caminhoDoArquivo, "r")
        self.conteudoDoArquivo = self.arquivo.read()
        self.arquivo.close()
        return self.conteudoDoArquivo

    def escreveNoArquivo(self, string, caminhoDoArquivo):
        self.arquivo = open(caminhoDoArquivo,"w")
        self.arquivo.write(string)
        self.arquivo.close()
