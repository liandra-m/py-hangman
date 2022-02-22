# py-hangman

Esse foi um dos meus primeiros projetos em python.  
Para jogar, você precisará do python3 instalado, e basta usar "python3 hangman.py", mas você também pode passar alguns argumentos:  

### --help, -h
Mostra a mensagem de ajuda padrão gerada pelo argparse do python.

### --inputlist, -i
Usa uma lista externa para obter e sortear as palavras. O arquivo de texto deve ter uma palavra por linha.

### --length, -l
Length significa "tamanho", logo, com esse argumento você pode indicar para o programa o tamanho da palavra que quer.

### --language -L
Adicionei essa feature recente, especifica a linguagem a ser usada. Suportadas no momento: 'pt-BR', 'en-US'.

### --word, -w
Passando esse argumento você pode especificar a exata palavra a ser usada, o programa, então, pula direto para o jogo. É útil, quando se está jogando com outra pessoa, por exemplo.

### Exemplos:
python3 hangman.py -w exemplo      
python3 hangman.py --word guarda-chuva  
python3 hangman.py -i './palavras.txt'  
python3 hangman.py -i '/home/usuario/palavras.txt' -l 6  
python3 hangman.py -L 'pt-BR' -l 6