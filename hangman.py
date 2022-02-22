#!/usr/bin/env python3

import argparse
import random
import subprocess
import sys
import unidecode

words = {'pt-BR': ['farinha', 'pássaro', 'igreja', 'maçã', 'banana', 'laranja', 'pera', 'mamão', 'graça', 'Deus', 'amor', 'vídeo','espada', 'livro','paralelo', 'linha', 'tempo', 'vida','triste', 'lírio'],
        'en-US': ['powder', 'church', 'banana', 'orange', 'apple', 'dummy', 'dictionary', 'umbrella', 'love', 'God', 'video', 'sword', 'spear', 'book', 'paralel', 'line', 'time', 'life', 'sadness', 'rose']
}

text={'en-US':{'e_directory_exception': "Couldn't acess file or directory. Please, make sure the path is right and you have the according permissions. \n",
                'e_generic_exception': 'Something happened, but I can determine error source. Aborting program. ',
                'e_word_length': ["Couldn't find word with ", " in the list.", "Press enter to choose an any length word, or type 'quit' to leave... \n"],
                'e_language_exception': 'Language not supported. Please, choose between pt-BR or en-US',
                't_attempts': 'Remaining attempts',
                't_find': "Type a letter to attempt, or more than one to guess whole word. type 'quit' at any moment, to leave... ",
                't_repeated': "Invalid attempt or you've already tried this letter. ",
                't_lose': "You lose! Good luck next time. The word was ",
                't_win': "Congratulations! You've won.",
                't_bye': "Ok, te vejo na próxima :)"
            },
    'pt-BR':{'e_directory_exception': "Não foi possível acessar arquivo ou diretório. Por favor, certifique-se de que o caminho está correto e você tem as permissões necessárias. \n",
                'e_generic_exception': 'Alguma coisa aconteceu, mas não consigo determinar a origem do erro. Abortando o programa. ',
                'e_word_length': ["Não foi possível encontrar palavra com ", " na lista.", " Pressione enter para escolher uma de qualquer tamanho, ou 'quit' para sair... \n"],
                'e_language_exception': 'Linguagem não suportada. Por favor, escolha entre pt-BR ou en-US',
                't_attempts': 'Tentativas restantes',
                't_find': "> Digite uma letra, ou mais de uma para tentar advinhar a palavra. Digite 'quit' a qualquer momento, para sair... ",
                't_repeated': "Tentativa inválida, ou você já tentou essa letra! ",
                't_lose': "Você perdeu! Boa sorte da próxima vez. A palavra era ",
                't_win': "Parabéns! Você ganhou.",
                't_bye': "Ok, see u next time :)"
    }
}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', default='*', help="Choose word to be choosen length, if not set will be any.")
    parser.add_argument('-w', '--word', help="Set a specific word.")
    parser.add_argument('-i', '--inputlist', help="Specify a file containing words to choose from, one per line.")
    parser.add_argument('-L', '--language', default='en-US', choices=['pt-BR', 'en-US'], help="Specify language to be use. Supported at the moment: pt-BR, en-US.")
    return parser.parse_args()


def gen_word(input_list):
    global args
    global text
    global words
    choosen_word = ''
    if input_list:
        try:
            with open(args.inputlist) as ilist:
                data = ilist.read()
                words = [w for w in data.replace(' ','').splitlines() if w != '']
        except (IsADirectoryError, FileNotFoundError):
            wait = input(text[args.language]['e_directory_exception'])
            if wait == 'quit':
                exit()
        except:
            print(text[args.language]['e_generic_exception'])
            exit()

    if args.length != '*':
        try:
            length = int(args.length)
            possible = False
            for w in words[args.language]:
                if len(w) == length:
                    possible = True
            if possible == False:
                raise(ValueError)
            else:
                while len(choosen_word) != length:
                    choosen_word = random.choice(words[args.language])

        except ValueError:
            print(text[args.language]['e_word_length'][0] + str(length) + text[args.language]['e_word_length'][1])
            wait = input(text[args.language]['e_word_length'][2])
            if wait == 'quit':
                exit()
            choosen_word = random.choice(words[args.language])
            
    else:
        choosen_word = random.choice(words[args.language])

    return choosen_word.lower()


def show():
    if sys.platform == 'win32':
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

    life_hash = ['#' for l in range(life)]
    print(text[args.language]['t_attempts'] + ' '.join(life_hash))
    print(f"{' '.join(list_word)} \n")


def game():
    global life
    global list_word
    global args
    hit_letters = []
    message = ''
    print(args.language)
    word_alt = word.lower()
    guess = ''
    while ''.join(list_word) != word and life > 0:
        show()
        print(message)
        guess = input(text[args.language]['t_find'])
        guess = guess.lower()
        message = ''

        if guess == 'quit':
            break
        elif len(guess) > 1 and guess != 'quit' and ' ' not in guess and guess !='' and guess != '\n':
            if unidecode.unidecode(guess) == unidecode.unidecode(word):
                list_word = [l for l in word]
                break
            else:
                life = 0

        else:
            if guess not in hit_letters and ' ' not in guess and guess !='' and guess != '\n':
                hit_letters.append(guess)
                if guess in word_alt:
                    for char in word_alt:
                        if unidecode.unidecode(char) == unidecode.unidecode(guess):
                            list_word[word_alt.index(char)] = char
                            word_alt = word_alt.replace(char, 'X', 1)

                else:
                    life -= 1
            else:
                message = text[args.language]['t_repeated']
    
    show()
    if life == 0:
        print(text[args.language]['t_lose'] + word)
    elif guess == 'quit':
        print(text[args.language]['t_bye'])
    else:
        print(text[args.language]['t_win'])


life = 5
args = get_args()

if not args.word:
    input_list = False
    if args.inputlist:
        input_list = True
    word = gen_word(input_list)
else:
    word = args.word
        
list_word = ['_' for a in word]
game()