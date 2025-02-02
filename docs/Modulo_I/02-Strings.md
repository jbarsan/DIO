# 🐍 Python - Módulo I
## 🗒️ Strings e fatiamentos
### A Classe STRING
<p>A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.</p>

<p>Os métodos de string em Python são funções que executam operações em strings. Alguns exemplos de métodos de string são:</p>

Todos os métodos da classe String podem ser vista no seguinte endereço:
[String-methods](https://docs.python.org/pt-br/3.13/library/stdtypes.html#string-methods)

#### Métodos úteis
**Maiúscula, minúscula e título**
```python
curso = "pYtHon"

print(curso.upper())
>>> PYTHON

print(curso.lower())
>>> python

print(curso.title())
>>> Python
```

**Eliminando espaços em branco**
```python
curso = "   Python "

print(curso.strip())
>>> "Python"

print(curso.lstrip())
>>> "Python "

print(curso.rstrip())
>>> "   Python"
```

**Junções e centralização**
```python
curso = "Python"

print(curso.center(10, "#"))
>>> "##Python##"

print(".".join(curso))
>>> "P.y.t.h.o.n"
```

#### Interpolação de variáveis
<p>Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última é utilizando f strings.
A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas 2 últimas.
</p>

**Old style %**
```python
nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"


print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.
```

**Método format**
```python
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e estou matriculado no curso de Python.

```

**f-string**
```python
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.
```

**Formatar strings com f-string**
```python
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
>>> "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}")
>>> "Valor de PI:       3.14"
```

#### Fatiamento de strings
<p>Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [start: stop[, step]].</p>

**Exemplos:**
```python
nome = "Guilherme Arthur de Carvalho"

nome[0]
>>> "G"

nome[:9]
>>> "Guilherme"

nome[10:]
>>> "Arthur de Carvalho"

nome[10:16]
>>> "Arthur"

nome[10:16:2]
>>> "Atu"

nome[:]
>>> "Guilherme Arthur de Carvalho"

nome[::-1]
>>> "ohlavraC ed ruhtrA emrehliuG"
```

#### Strings múltiplas linhas
<p>Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.</p>

**Exemplos:**
```python
nome = "Guilherme"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""
>>> 

Olá meu nome é Guilherme,
Eu estou aprendendo Python


nome = "Guilherme"

mensagem = f'''
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
'''
>>> 

   Olá meu nome é Guilherme,
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.

```