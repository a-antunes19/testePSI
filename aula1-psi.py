#para CRIAR um ambiente virtual (venv) digitamos o seguinte comando: python -m venv nome-do-ambiente (por padrão utilizamos o nome "venv")
#para ATIVAR o ambiente virtual (venv) digitamos o seguinte comando: .\venv\Scripts\Activate.ps1 (para não haver erros, vamos passando os arquivos por meio do TAB)
#para DESATIVAR o ambiente virtual (venv) digitamos o seguinte comando: deactivate
#para REUTILIZAR os últimos comandos no terminal pressionamos a seta pra cima
#para LIMPAR O TERMINAL digitamos o comando: CTRL+L

#PACOTES (lembre-se de ativar o venv)
#para INSTALAR o pacotes digitamos o seguinte comando: pip install nomedopacote
#para CONGELAR o venv digitamos o seguinte comando: pip freeze
#para ENVIAR o venv digitamos o seguinte comando: pip freeze > arquivo.txt (por padrão utilizamos o nome "requirements.txt")
#para DESCONGELAR o venv digitamos o seguinte comando: pip install -r .\requirememts.txt
#para REMOVER um pacote: pip unistall nomedopacote
#para ATUALIZAR um pacote: pip --upgrade (...)

#CÓDIGO FONTE
#para ESCONDER os arquivos do venv fazemos um novo arquivo chamado ".gitignore" e dentro dele digitamos "venv" e salvamos

#para configurar o seu nome: git config --global user.name "Antônio Antunes"
#para configurar o seu email: git config --global user.email "antunesantonio91@gmail.com"
#para verificar se o seu nome e email deram certo: git config --list      +      seta para baixo   >>> para sair apertamos "q"
#para verificar se o seu commit deu certo digitamos: git log