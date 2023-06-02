from Packages.verificaUltimaPostagem import Postagem



stringUrlPolitecnico = "enderecoURL"
stringSeletorPolitecnico = 'seletor de tags'
stringCaminhoArquivoPoli = "caminho do arquivo"

stringUrlCt = "enderecoURL"
stringSeletorCt = 'seletor de tags'
stringCaminhoArquivoCT = "caminho do arquivo"

postagem = Postagem()
postagem.verificaUltimaPostagem(stringUrlPolitecnico,stringSeletorPolitecnico,stringCaminhoArquivoPoli)
postagem.verificaUltimaPostagem(stringUrlCt,stringSeletorCt,stringCaminhoArquivoCT)
