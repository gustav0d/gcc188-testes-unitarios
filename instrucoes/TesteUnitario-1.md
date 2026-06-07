
# Aula Prática: Teste Unitário com Python e PyUnit no VS Code

  

## 1. Objetivo da aula

  

Nesta aula prática, você irá aprender, passo a passo, como criar e executar testes unitários usando Python e o módulo `unittest`, também conhecido como PyUnit. Você pode usar outra linguagem de programação, mas o tutorial vai ensinar em Python. Fica por sua conta em aprender diante de outras linguagens. 

  



**Esta aula foi pensada para alunos que nunca fizeram testes automatizados antes.

  ### Essa aula deverá gerar artefatos pelo qual a entrega deles  será via link do seu GitHub, indicando que você fez a atividade. Se você usar IA para gerar o teste onde não deveria usar, pois a finalidade é aprender como funciona. *-O problema será totalmente seu-*

---

  

## 2. Pré-requisitos

  

Antes de começar, verifique se você tem instalado no computador:

  

- Python;

- Visual Studio Code;

- extensão Python no Visual Studio Code;

  

### 2.1 Verificando se o Python está instalado

  

Abra o terminal do seu computador.

  

No Windows, você pode usar:

  

- Prompt de Comando;

- PowerShell;

- terminal integrado do VS Code.

  

Digite o comando:

  

```bash

python  --version

```

  

Ou, em alguns computadores:

  

```bash

python3  --version

```

  

Se o Python estiver instalado corretamente, aparecerá algo parecido com:

  

```bash

Python  3.12.0

```

  

Caso apareça uma mensagem de erro, provavelmente o Python não está instalado ou não está configurado no PATH do sistema.

  

### Erro comum

  

Se aparecer algo como:

  

```bash

'python'  não  é  reconhecido  como  um  comando  interno

```

  

Isso significa que o computador não encontrou o Python.

  

### Como resolver

  

Instale o Python pelo site oficial:

  

```text

https://www.python.org/

```

  

Durante a instalação no Windows, marque a opção:

  

```text

Add Python to PATH

```

  

---

  

## 3. Conceitos iniciais

  

Antes de programar, vamos entender alguns conceitos importantes.

  

### 3.1 O que é teste de software?

  

Teste de software é uma forma de verificar se um programa está funcionando como esperado.

  

Por exemplo, imagine uma calculadora. Se você digitar:

  

```text

2 + 3

```

  

Espera-se que o resultado seja:

  

```text

5

```

  

Se a calculadora retornar `6`, existe um problema.

  

Testar software é justamente verificar esse tipo de comportamento.

  

---

  

### 3.2 O que é teste unitário?

  

Teste unitário é um teste feito em uma pequena parte do código.

  

Essa pequena parte geralmente é uma função, um método ou uma classe.

  

Exemplo:

  

```python

def  somar(a, b):

return a + b

```

  

Um teste unitário verificaria se essa função realmente soma corretamente:

  

```python

somar(2, 3) == 5

```

  

Ou seja, o teste verifica se uma parte pequena do programa funciona sozinha.

  

---

  

### 3.3 O que é PyUnit/unittest?

  

O `unittest` é uma biblioteca que já vem instalada junto com o Python.

  

Ela permite criar testes automatizados.

  

Também é conhecida como PyUnit, pois foi inspirada em ferramentas de teste como o JUnit, usado na linguagem Java.

  

Com `unittest`, podemos escrever testes como este:

  

```python

self.assertEqual(somar(2, 3), 5)

```

  

Esse comando verifica se o resultado da função `somar(2, 3)` é igual a `5`.

  

---

  

### 3.4 Por que testes automatizados são úteis?

  

Testes automatizados ajudam a:

  

- encontrar erros mais rapidamente;

- verificar se o código continua funcionando após mudanças;

- evitar que erros antigos voltem a acontecer;

- aumentar a confiança no código;

- documentar o comportamento esperado das funções.

  

Imagine que você altere uma função hoje. Com testes, você consegue verificar rapidamente se a alteração quebrou alguma parte do programa.

  

---

  

### 3.5 O que significa um teste passar ou falhar?

  

Um teste passa quando o resultado obtido é igual ao resultado esperado.

  

Exemplo:

  

```python

somar(2, 3)

```

  

Resultado esperado:

  

```text

5

```

  

Resultado obtido:

  

```text

5

```

  

Nesse caso, o teste passa.

  

Um teste falha quando o resultado obtido é diferente do esperado.

  

Exemplo:

  

```python

somar(2, 3)

```

  

Resultado esperado:

  

```text

5

```

  

Resultado obtido:

  

```text

6

```

  

Nesse caso, o teste falha.

  

---

  

## 4. Criação do projeto no VS Code

  

Agora vamos criar o projeto da aula prática.

  

### 4.1 Criando a pasta do projeto

  

Escolha um local no seu computador, como a Área de Trabalho ou a pasta Documentos.

  

Crie uma pasta chamada:

  

```text

teste-unitario-python

```

  

Essa será a pasta principal do projeto.

  

---

  

### 4.2 Abrindo a pasta no VS Code

  

Abra o Visual Studio Code.

  

Depois clique em:

  

```text

File > Open Folder

```

  

Ou, em português:

  

```text

Arquivo > Abrir Pasta

```

  

Selecione a pasta:

  

```text

teste-unitario-python

```

  

Clique em abrir.

  

---

  

### 4.3 Criando a estrutura inicial de arquivos

  

Dentro do VS Code, crie os seguintes arquivos:

  

```text

teste-unitario-python/

│

├── calculadora.py

├── test_calculadora.py

└── README.md

```

  

Explicação dos arquivos:

  


| Arquivo | Finalidade |
| :--- | :--- |
| `calculadora.py` | Arquivo com as funções da calculadora |
| `test_calculadora.py` | Arquivo com os testes unitários |
| `README.md` | Arquivo com a explicação do projeto |

  

---

  

## 5. Criando o primeiro código Python

  

Abra o arquivo `calculadora.py`.

  

Nele, vamos criar algumas funções simples de uma calculadora.

  

Digite o código abaixo:

  

```python

# calculadora.py

  
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números.

    Se o segundo número for zero, o Python irá gerar um erro.
    """
    return a / b

```

  

### 5.1 Explicando o código

  

A função `somar(a, b)` recebe dois valores e retorna a soma deles.

  

Exemplo:

  

```python

somar(2, 3)

```

  

Resultado:

  

```text

5

```

  

A função `subtrair(a, b)` recebe dois valores e retorna a subtração.

  

Exemplo:

  

```python

subtrair(10, 4)

```

  

Resultado:

  

```text

6

```

  

A função `multiplicar(a, b)` recebe dois valores e retorna a multiplicação.

  

Exemplo:

  

```python

multiplicar(3, 4)

```

  

Resultado:

  

```text

12

```

  

A função `dividir(a, b)` recebe dois valores e retorna a divisão.

  

Exemplo:

  

```python

dividir(10, 2)

```

  

Resultado:

  

```text

5.0

```

  

---

  

## 6. Criando os testes unitários

  

Agora vamos criar os testes.

  

Abra o arquivo `test_calculadora.py`.

  

Digite o código abaixo:

  

```python

# test_calculadora.py

import unittest

from calculadora import dividir, multiplicar, somar, subtrair


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_somar(self):
        """Testa se a função somar está funcionando corretamente."""
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        """Testa se a função subtrair está funcionando corretamente."""
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        """Testa se a função multiplicar está funcionando corretamente."""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        """Testa se a função dividir está funcionando corretamente."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        """Testa se a divisão por zero gera erro."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()

```

  

---

  

### 6.1 Explicando o código de teste

  

A primeira linha importa o módulo `unittest`:

  

```python

import unittest

```

  

Esse módulo será usado para criar e executar os testes.

  

Depois, importamos as funções do arquivo `calculadora.py`:

  

```python

from calculadora import somar, subtrair, multiplicar, dividir

```

  

Isso permite testar essas funções dentro do arquivo `test_calculadora.py`.

  

---

  

### 6.2 Criando uma classe de testes

  

Criamos uma classe chamada `TestCalculadora`:

  

```python

class  TestCalculadora(unittest.TestCase):

```

  

Essa classe herda de `unittest.TestCase`.

  

Isso significa que ela é uma classe de teste.

  

Dentro dela, criamos métodos de teste.

  

---

  

### 6.3 Por que os métodos começam com `test_`?

  

Observe este método:

  

```python

def  test_somar(self):

```

  

O nome começa com `test_`.

  

O `unittest` procura automaticamente métodos que começam com `test_`.

  

Se o método não começar com `test_`, ele não será reconhecido como teste.

  

Exemplo incorreto:

  

```python

def  somar_deve_funcionar(self):

```

  

Esse método não seria executado automaticamente pelo `unittest`.

  

Exemplo correto:

  

```python

def  test_somar_deve_funcionar(self):

```

  

---

  

### 6.4 Usando `assertEqual`

  

O comando `assertEqual` verifica se dois valores são iguais.

  

Exemplo:

  

```python

self.assertEqual(somar(2, 3), 5)

```

  

Esse teste significa:

  

```text

Verifique se somar(2, 3) é igual a 5.

```

  

Se o resultado for `5`, o teste passa.

  

Se o resultado for diferente de `5`, o teste falha.

  

---

  

### 6.5 Testando exceções com `assertRaises`

  

Algumas situações devem gerar erro.

  

Por exemplo, dividir por zero não é permitido.

  

No Python, isso gera uma exceção chamada `ZeroDivisionError`.

  

Para testar esse comportamento, usamos:

  

```python

with  self.assertRaises(ZeroDivisionError):

dividir(10, 0)

```

  

Esse teste significa:

  

```text

Verifique se dividir(10, 0) gera um erro do tipo ZeroDivisionError.

```

  

Se o erro acontecer, o teste passa.

  

Se o erro não acontecer, o teste falha.

  

---

  

## 7. Executando os testes

  

Agora vamos executar os testes pelo terminal.

  

### 7.1 Abrindo o terminal no VS Code

  

No Visual Studio Code, clique em:

  

```text

Terminal > New Terminal

```

  

Ou, em português:

  

```text

Terminal > Novo Terminal

```

  

Um terminal será aberto na parte inferior da tela.

  

Verifique se o terminal está dentro da pasta do projeto.

  

Você deve estar em uma pasta parecida com:

  

```text

teste-unitario-python

```

  

---

  

### 7.2 Executando um arquivo específico de teste

  

Digite o comando:

  

```bash

python  -m  unittest  test_calculadora.py

```

  

Esse comando executa os testes que estão no arquivo `test_calculadora.py`.

  


| Parte do comando | Significado |
| :--- | :--- |
| `python` | Chama o interpretador Python |
| `-m unittest` | Executa o módulo `unittest` |
| `test_calculadora.py` | Indica o arquivo de testes que será executado |
  

---

  

### 7.3 Executando todos os testes automaticamente

  

Também podemos usar:

  

```bash

python  -m  unittest  discover

```

  

Esse comando procura automaticamente arquivos de teste no projeto.

  

Por padrão, o `unittest` procura arquivos que começam com `test`.

  

Exemplos:

  

```text

test_calculadora.py

test_usuario.py

test_produto.py

```

  

### Diferença simples

  

O comando abaixo executa um arquivo específico:

  

```bash

python  -m  unittest  test_calculadora.py

```

  

O comando abaixo procura e executa todos os testes encontrados no projeto:

  

```bash

python  -m  unittest  discover

```

  

---

  

## 8. Interpretando os resultados

  

Depois de executar os testes, o terminal mostrará o resultado.

  

---

  

### 8.1 Quando todos os testes passam

  

Se tudo estiver correto, você verá algo parecido com:

  

```bash

.....

----------------------------------------------------------------------

Ran  5  tests  in  0.001s

  

OK

```

  

Explicação:

  


| Resultado | Significado |
| :--- | :--- |
| `.....` | Cada ponto representa um teste que passou |
| `Ran 5 tests` | Foram executados 5 testes |
| `OK` | Todos os testes passaram |
  

---

  

### 8.2 Quando um teste falha

  

Agora imagine que alguém alterou a função `somar` de forma errada:

  

```python

def  somar(a, b):

return a - b

```

  

Ao executar os testes, pode aparecer algo parecido com:

  

```bash

F....

======================================================================

FAIL:  test_somar (test_calculadora.TestCalculadora)

----------------------------------------------------------------------

Traceback (most recent  call  last):

File  "test_calculadora.py",  line  15,  in  test_somar

self.assertEqual(somar(2,  3), 5)

AssertionError:  -1  !=  5

  

----------------------------------------------------------------------

Ran  5  tests  in  0.001s

  

FAILED (failures=1)

```

  

Explicação:

  


| Resultado | Significado |
| :--- | :--- |
| `F` | Um teste falhou |
| `FAIL` | O resultado obtido foi diferente do esperado |
| `AssertionError` | O teste esperava um valor, mas recebeu outro |
| `-1 != 5` | O resultado obtido foi `-1`, mas o esperado era `5` |

  

---

  

### 8.3 Quando ocorre um erro no código

  

Um erro é diferente de uma falha.

  

A falha acontece quando o código roda, mas retorna um valor errado.

  

O erro acontece quando o código nem consegue executar corretamente.

  

Exemplo de erro no código:

  

```python

def  dividir(a, b):

return a / c

```

  

Nesse caso, a variável `c` não existe.

  

Ao executar os testes, pode aparecer algo parecido com:

  

```bash

E....

======================================================================

ERROR:  test_dividir (test_calculadora.TestCalculadora)

----------------------------------------------------------------------

Traceback (most recent  call  last):

File  "test_calculadora.py",  line  35,  in  test_dividir

self.assertEqual(dividir(10,  2), 5)

File  "calculadora.py",  line  24,  in  dividir

return  a  /  c

NameError:  name  'c'  is  not  defined

  

----------------------------------------------------------------------

Ran  5  tests  in  0.001s

  

FAILED (errors=1)

```

  

Explicação:

  


| Resultado | Significado |
| :--- | :--- |
| `E` | Ocorreu um erro |
| `ERROR` | O código quebrou durante a execução |
| `NameError` | Algum nome usado no código não foi encontrado |
| `name 'c' is not defined` | A variável `c` não existe |

  

---

  

### 8.4 Diferença entre OK, FAIL e ERROR

  


| Resultado | Significado |
| :--- | :--- |
| `OK` | Todos os testes passaram |
| `FAIL` | O teste executou, mas o resultado foi diferente do esperado |
| `ERROR` | O código gerou um erro durante a execução |

  

---

  

## 9. Atividade prática guiada

  

Agora é sua vez.

  

Você deverá adicionar uma nova função chamada `potencia(a, b)`.

  

Essa função deve calcular a potência de um número.

  

Exemplo:

  

```python

potencia(2, 3)

```

  

Resultado esperado:

  

```text

8

```

  

Porque:

  

```text

2 elevado a 3 = 2 * 2 * 2 = 8

```

  

---

  

### 9.1 Passo 1: adicionar a função no arquivo `calculadora.py`

  

Abra o arquivo `calculadora.py`.

  

Adicione uma nova função chamada:

  

```python

potencia(a, b)

```

  

Essa função deve receber dois valores:

  

-  `a`: base;

-  `b`: expoente.

  

Por enquanto, tente implementar sozinho.

  

Dica:

  

Em Python, o operador de potência é:

  

```python

**

```

  

Exemplo:

  

```python

2 ** 3

```

  

Resultado:

  

```text

8

```

  

---

  

### 9.2 Passo 2: importar a função no arquivo de teste

  

Abra o arquivo `test_calculadora.py`.

  

Na linha de importação, adicione a função `potencia`.

  

A linha atual é:

  

```python

from calculadora import somar, subtrair, multiplicar, dividir

```

  

Você deverá alterá-la para importar também a nova função.

  

---

  

### 9.3 Passo 3: criar testes para a função `potencia`

  

Dentro da classe `TestCalculadora`, crie um novo método de teste.

  

Lembre-se: o nome do método deve começar com `test_`.

  

Sugestão de nome:

  

```python

def  test_potencia(self):

```

  

Crie testes para verificar:

  

-  `potencia(2, 3)` deve retornar `8`;

-  `potencia(5, 0)` deve retornar `1`;

-  `potencia(10, 2)` deve retornar `100`.

  

---

  

### 9.4 Passo 4: executar os testes

  

No terminal, execute:

  

```bash

python  -m  unittest  test_calculadora.py

```

  

Ou:

  

```bash

python  -m  unittest  discover

```

  

Verifique se todos os testes passaram.

  

---

  

### 9.5 Passo 5: corrigir possíveis erros

  

Se algum teste falhar, leia a mensagem com atenção.

  

Pergunte-se:

  

- O nome da função está correto?

- A função foi importada corretamente?

- O método de teste começa com `test_`?

- O resultado esperado está correto?

- A função está retornando o valor certo?

  

---

  


  

## 10. Desafio extra

  

Se você terminou a atividade anterior, faça o desafio extra.

  

Crie uma função chamada:

  

```python

calcular_media(lista)

```

  

Essa função deve receber uma lista de números e retornar a média.

  

Exemplo:

  

```python

calcular_media([10, 8, 6])

```

  

Resultado esperado:

  

```text

8

```

  

Porque:

  

```text

(10 + 8 + 6) / 3 = 8

```

  

---

  

### 10.1 O que você deve fazer

  

No arquivo `calculadora.py`, crie a função:

  

```python

calcular_media(lista)

```

  

No arquivo `test_calculadora.py`, crie testes para:

  

- lista com números inteiros;

- lista com números decimais;

- lista com apenas um número;

- lista vazia.

  

---

  

### 10.2 Decisão importante

  

O que deve acontecer se a lista estiver vazia?

  

Exemplo:

  

```python

calcular_media([])

```

  

Existem algumas possibilidades:

  

1. retornar `0`;

2. retornar `None`;

3. gerar um erro.

  

Nesta aula, vamos escolher a terceira opção: gerar um erro.

  

Para isso, podemos lançar uma exceção do tipo `ValueError`.

  

---

  

## 11. Organização final do repositório

  

Ao final da aula, o projeto deverá estar organizado assim:

  

```text

teste-unitario-python/

│

├── calculadora.py

├── test_calculadora.py

└── README.md

```


  

O arquivo `README.md` terá a explicação do projeto.

  

---

  

## 12. Como enviar para o GitHub

  

Agora vamos ver como enviar o projeto para o GitHub.

  

---

  

### 12.1 Criando um repositório no GitHub

  

Acesse o GitHub:

  

```text

https://github.com/

```

  

Faça login na sua conta.

  

Clique em:

  

```text

New repository

```

  

Ou:

  

```text

Novo repositório

```

  

Escolha um nome para o repositório, por exemplo:

  

```text

teste-unitario-python

```

  

Depois clique em criar repositório.

  

---

  

### 12.2 Inicializando o Git no projeto

  

No terminal do VS Code, dentro da pasta do projeto, digite:

  

```bash

git  init

```

  

Esse comando cria um repositório Git local dentro da pasta do projeto.

  

---

  

### 12.3 Adicionando os arquivos

  

Digite:

  

```bash

git  add  .

```

  

Esse comando adiciona todos os arquivos do projeto para serem versionados.

  

O ponto `.` significa “todos os arquivos da pasta atual”.

  

---

  

### 12.4 Criando o primeiro commit

  

Digite:

  

```bash

git  commit  -m  "Aula prática de teste unitário com Python"

```

  

Esse comando cria um registro das alterações feitas no projeto.

  

A mensagem entre aspas descreve o que foi feito.

  

---

  

### 12.5 Definindo a branch principal

  

Digite:

  

```bash

git  branch  -M  main

```

  

Esse comando define o nome da branch principal como `main`.

  

---

  

### 12.6 Conectando o projeto local ao GitHub

  

No GitHub, copie a URL do repositório criado.

  

Ela será parecida com:

  

```text

https://github.com/seu-usuario/teste-unitario-python.git

```

  

Depois, no terminal, digite:

  

```bash

git  remote  add  origin  URL_DO_REPOSITORIO

```

  

Importante: substitua `URL_DO_REPOSITORIO` pela URL real do seu repositório.

  

Exemplo:

  

```bash

git  remote  add  origin  https://github.com/seu-usuario/teste-unitario-python.git

```

  

---

  

### 12.7 Enviando o projeto para o GitHub

  

Digite:

  

```bash

git  push  -u  origin  main

```

  

Esse comando envia os arquivos do seu computador para o GitHub.

  

---

  

### Erro comum

  

Pode aparecer uma mensagem pedindo login no GitHub.

  

### Como resolver

  

Siga as instruções que aparecerem na tela.

  

Em alguns casos, será necessário autenticar usando o navegador ou um token de acesso.

  

---

  

## 13. Checklist final

  

Antes de finalizar, confira se você concluiu todos os itens:

  

- [ ] Python instalado;

- [ ] Visual Studio Code instalado;

- [ ] extensão Python instalada no VS Code;

- [ ] pasta do projeto criada;

- [ ] arquivo `calculadora.py` criado;

- [ ] arquivo `test_calculadora.py` criado;

- [ ] funções da calculadora implementadas;

- [ ] testes unitários implementados;

- [ ] testes executados pelo terminal;

- [ ] testes passando;

- [ ] atividade prática da função `potencia(a, b)` concluída;

- [ ] desafio extra realizado, se solicitado;

- [ ] arquivo `README.md` criado;

- [ ] repositório criado no GitHub;

- [ ] projeto enviado para o GitHub.

  

---

  

