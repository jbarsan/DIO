# 🐍 Python - Módulo I
## 🗒️ Tipos de operadores em Python
### ➕ Operadores aritméticos
**O que são?**
- Os operadores aritméticos executam operações matemáticas, como adição, subtração com operandos.

| Aulas | Resumo |
| ----- | ------ |
| Operadores aritméticos | |
| Adição: | ``` print(1 + 1) ``` |
| Subtração: | ``` print(10 - 2) ``` |
| Multiplicação: |  ``` print(4 * 3) ``` |
| Divisão: |  ``` print(12 / 3) ``` |
| Divisão inteira: |  ``` print(12 // 2) ``` Retorna somente a parte inteira da divisão|
| Módulo: | ``` print(10 % 3) ``` Retorna o resto da divisão |
| Exponenciação: |  ``` print(2 ** 3) ``` 2 elevado a 3 |

### 🪩 Precedência dos operadores aritméticos
- Parênteses;
- Expoentes;
- Multiplicações e Divisões (da esquerda para a direita);
- Somas e subtrações (da esquerda para a direita).

### 🪩 Operadores de comparação
**O que são?**
- São operadores utilizados para comparar dois valores.

| Descrição | Operador |
| --------- | -------- |
| Igualdade | ``` == ``` |
| Diferença | ``` != ``` |
| Maior que, Maior ou igual | ``` > ```, ``` >= ``` |
| Menor que, Menor ou igual | ``` < ```, ``` <= ``` |

### 🪩 Operadores de atribuição
**O que são?**
- São operadores utilizados para definir o valor inicial ou sobrescrever o valor de uma variável.

| Descrição | Operador | Exemplos |
| --------- | -------- | -------- |
| Atribuição simples | ``` = ``` | valor = 500 |
| Atribuição com adição | ``` += ``` | valor += 200 |
| Atribuição com subtração | ``` -= ``` | valor -= 100 |
| Atribuição com multiplicação | ``` *= ``` | valor *= 2 |
| Atrbiuição com divisão | ``` /= ``` | valor /= 5 |
| Atribuição com módulo | ``` %= ``` | valor %= 8 |
| Atribuição com exponenciação | ``` **= ``` | valor **= 2 |

### 🪩 Operadores lógicos
**O que são?**
- São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:
op_comparacao + op_logico + op_comparacao… N …

| Descrição | Operador |
| --------- | -------- |
| Operador E | ```and``` |
| Operador OU | ``` or ``` | 1000 >= 200 or 200 <= 100 == True |
| Operador Negação | ``` not ``` | not 1000 > 1500 == True |
| Parênteses | ``` () ``` | (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) == True|

**Exemplo Operador E:**
```python
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
>>> False
```
**Exemplo Operador OU:**
```python
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
>>> True
```
**Exemplo Operador NEGAÇÃO:**
```python
contatos_emergencia = []

not 1000 > 1500
>>> True

not contatos_emergencia
>>> True

not "saque 1500;"
>>> False

not ""
>>> True
```
**Exemplo PARÊNTESES:**
```python
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
>>> True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
>>> True
```

### 🪩 Operadores de identidade
**O que são?**
- São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

| Descrição | Operador |
| --------- | -------- |
| Verifica se dois objetos são o mesmo objeto na memória | ``` is ``` | 
| Verifica se dois objetos não são o mesmo objeto na memória | ``` is not ``` |

**Exemplo:**

```python
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
>>> True

curso is not nome_curso
>>> False

saldo is limite
>>> True
```

### 🪩 Operadores de associação
**O que são?**
- São operadores utilizados para verificar se um objeto está presente em uma sequência.

| Descrição | Operador |
| --------- | -------- |
| "Está contido em" | ``` in ``` | 
| "Não está contido em" | ``` not in ``` |

**Exemplos:**

```python
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
>>> True

"maçã" not in frutas
>>> True

200 in saques
>>> False
```

## 🗒️ Estruturas condicionais
<p>A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.
</p>

### 🪩 Identação e blocos
**Utilizando espaços**
<p>Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.</p>

**Bloco em Python:**
```python
def sacar(self, valor: float) -> None:  # início do bloco do método
    if self.saldo >= valor:  # início do bloco do if
        self.saldo -= valor
    
    # fim do bloco do if

# fim do bloco do método
```

**Não funciona em Python:**
```python
def sacar(self, valor: float) -> None:  # início do bloco do método
if self.saldo >= valor:  # início do bloco do if    
self.saldo -= valor
# fim do bloco do if
# fim do bloco do método
```

### 🪩 Estrutura condicinal: if / if-else / elif
#### if
<p>Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.</p>

**Exemplos:**
```python
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo <= saque:
    print("Saldo insuficiente!")
```
#### if/else
<p>Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado.</p>

**Exemplos:**
```python
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")
```
#### if/else/elif
<p>Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.</p>

**Exemplos:**
```python
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
 # ...
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")
```

#### if aninhado
<p>Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.</p>

**Exemplos:**
```python
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
```

#### if ternário
<p>O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.</p>

**Exemplos:**
```python
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
```
## 🗒️ Estruturas de repetição
<p>São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.</p>

### 🪩 for
<p>O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.</p>

**Exemplo for:**
```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()  # adiciona uma quebra de linha
```
**Exemplo for/else:**
```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha
```
### 🪩 Função built-in range
<p>Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido:</p>

<em>i, i+1, i+2, i+3, ..., j-1.</em>

<p>Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.</p>

**Exemplo range:**
```python
# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4))
>>> [0, 1, 2, 3]
```

**Exemplo range com for:**
```python
for numero in range(0, 11):
    print(numero, end=" ")

>>> 0 1 2 3 4 5 6 7 8 9 10

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

>>> 0 5 10 15 20 25 30 35 40 45 50
```

### 🪩 while
<p>O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.</p>

**Exemplo while:**
```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
```

**Exemplo while/else:**
```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
 print("Obrigado por usar nosso sistema bancário, até logo!")
```

### 🪩 break
<p>É uma palavra reservada que interrompe a execução de um loop de repetição. O break é usado quando uma condição externa é acionada, permitindo que o programa continue a execução a partir da próxima linha de código.

**Exemplos break com for:**
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(f"Analisando o número: {numero}")
    if numero == 5:
        print("Número 5 encontrado! Interrompendo o loop.")
        break
    print(f"Número {numero} não é 5. ")
print("Loop encerrado.")
```

```python
for numero in range(100):
    if numero == 10:
        break
    print(numero)
```

**Exemplos break com while:**
```python
while True:
    line = input('> ')
    if line == 'done':
        break
  print(line)
  print('Done! ')
```

```python
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    
    print(numero)
```

### 🪩 continue
<p>É uma palavra reservada que permite ignorar parte de um loop e continuar com o próximo valor. Ela pode ser usada em conjunto com os loops for e while para tornar os programas mais eficientes e legíveis.</p>

**Exemplo continue com for:**
```python
for num in range(5):
    if num == 3:
        print("Encontrei o 3")
        # Executa o continue, pulando para o próximo laço
        continue
    else:
        print(num)

    print("Estou abaixo do IF")
```

**Exemplo continue com while:**
```python
num = 0
while num < 5:
    num += 1

    if num == 3:
        continue
        
    print(num)
```

### 🪩 pass
<p>O pass nada mais é que uma forma de fazer um código que não realiza operação nenhuma.</p>
<p>Como os escopos de Classes, Funções, If/Else e loops for/while são definidos pela indentação do código (e não por chaves {} como geralmente se vê em outras linguagens de programação), usamos o pass para dizer ao Python que o bloco de código está vazio.</p>

**Exemplos:**
```python
for item in range(5000):
    pass

while False:
    pass

class Classe:
    pass

if True:
    pass
else:
    pass

def funcao():
    pass
```
