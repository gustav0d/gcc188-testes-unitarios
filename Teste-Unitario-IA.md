
# Aula Prática: Usando IA para Gerar Cenários de Teste Unitário em Python

  

## 1. Objetivo da aula

  

Na aula anterior, você aprendeu a criar testes unitários usando Python, PyUnit/`unittest` e Visual Studio Code.

  

Nesta nova aula prática, você irá aprender como usar ferramentas de Inteligência Artificial, como ChatGPT, Copilot ou outras IAs generativas, para ajudar na criação de cenários de teste unitário.

  

O objetivo desta aula **não é substituir o raciocínio do programador**, mas usar a IA como apoio para:

  

- pensar em cenários de teste;

- identificar casos normais e casos extremos;

- sugerir entradas e saídas esperadas;

- melhorar testes já existentes;

- criar testes para exceções;

- encontrar possíveis casos esquecidos;

- automatizar parte da escrita dos testes unitários.

  

Ao final desta aula, você será capaz de:

  

- escrever prompts para pedir ajuda à IA na criação de testes;

- avaliar se os testes sugeridos pela IA fazem sentido;

- transformar cenários sugeridos em testes usando `unittest`;

- ampliar os testes da calculadora criada na aula anterior;

- testar casos normais, casos de borda e casos de erro;

- usar IA de forma crítica e responsável no desenvolvimento de software.

  

---

  

## 2. Pré-requisitos

  

Antes de começar, você precisa ter concluído ou entendido a aula anterior sobre teste unitário com Python e PyUnit.

  

Você também precisa ter:

  

- Python instalado;

- Visual Studio Code instalado;

- extensão Python instalada no VS Code;

- projeto da aula anterior criado;

- conhecimento básico sobre funções em Python;

- conhecimento básico sobre testes com `unittest`;

- acesso a alguma ferramenta de IA generativa.

  

Exemplos de ferramentas que podem ser usadas:

  

- ChatGPT;

- GitHub Copilot;

- Gemini;

- Claude;

- outras ferramentas semelhantes.

  

Nesta aula, os exemplos de prompt serão escritos de forma genérica, para que possam ser usados em diferentes ferramentas de IA.

  

---

  

## 3. Projeto base da aula anterior

  

Vamos continuar usando o projeto da aula anterior.

  

A estrutura inicial do projeto era:

  

```text

teste-unitario-python/

│

├── calculadora.py

├── test_calculadora.py

└── README.md

```

  



O arquivo `test_calculadora.py` continha testes usando `unittest`.

  

Nesta aula, vamos melhorar e ampliar esses testes com apoio da IA.

  

---

  

## 4. Antes de usar IA: o que são cenários de teste?

  

Um cenário de teste descreve uma situação que deve ser verificada.

  

Exemplo para a função `somar(a, b)`:

  

```text

Cenário: somar dois números positivos.

Entrada: 2 e 3.

Resultado esperado: 5.

```

  

Outro exemplo:

  

```text

Cenário: somar um número negativo com um número positivo.

Entrada: -2 e 5.

Resultado esperado: 3.

```

  

Um cenário de teste geralmente possui:

  
| Elemento | Exemplo |
| :--- | :--- |
| Função testada | `somar(a, b)` |
| Situação testada | soma de dois números positivos |
| Entrada | `2` e `3` |
| Resultado esperado | `5` |
| Tipo de teste | caso normal |

---

  

## 5. Tipos de cenários de teste unitário

  

Ao pedir ajuda para uma IA, é importante saber o que solicitar.

  

Vamos trabalhar com alguns tipos de cenário.

  

---

  

### 5.1 Caso normal

  

É o uso mais comum da função.

  

Exemplo:

  

```python

somar(2, 3)

```

  

Resultado esperado:

  

```text

5

```

  

---

  

### 5.2 Caso com valor zero

  

Testa se a função funciona corretamente com zero.

  

Exemplo:

  

```python

multiplicar(10, 0)

```

  

Resultado esperado:

  

```text

0

```

  

---

  

### 5.3 Caso com número negativo

  

Testa se a função funciona com valores negativos.

  

Exemplo:

  

```python

subtrair(-5, -2)

```

  

Resultado esperado:

  

```text

-3

```

  

---

  

### 5.4 Caso de borda

  

Caso de borda é uma situação limite.

  

Exemplo para uma lista:

  

```python

calcular_media([10])

```

  

Essa lista tem apenas um elemento.

  

Resultado esperado:

  

```text

10

```

  

---

  

### 5.5 Caso de erro ou exceção

  

Testa se a função se comporta corretamente quando recebe uma entrada inválida.

  

Exemplo:

  

```python

calcular_media([])

```

  

Como a lista está vazia, esperamos um erro.

  

Resultado esperado:

  

```text

ValueError

```

  

---

  

## 6. Por que usar IA para gerar cenários de teste?

  

A IA pode ajudar a lembrar cenários que o programador poderia esquecer.

  

Por exemplo, ao testar uma função de média, talvez o aluno pense apenas neste caso:

  

```python

calcular_media([10, 8, 6])

```

  

Mas a IA pode sugerir também:

  

- lista com um único número;

- lista com números negativos;

- lista com números decimais;

- lista vazia;

- lista com zeros;

- lista com valores mistos.

  

Isso ajuda a deixar os testes mais completos.

  

Porém, existe um cuidado importante:

  

> A IA pode errar. Por isso, todo teste sugerido precisa ser conferido pelo aluno.

  

Usar IA não significa aceitar tudo automaticamente.

  

O aluno deve perguntar:

  

- Esse cenário faz sentido?

- A entrada é válida?

- O resultado esperado está correto?

- Esse teste realmente verifica algo importante?

- O código gerado está compatível com o projeto?

  

---

  

## 7. Como escrever bons prompts para gerar testes

  

Um prompt é o pedido que você escreve para a IA.

  

Um prompt ruim é muito genérico.

  

Exemplo ruim:

  

```text

Faça testes para minha calculadora.

```

  

Esse prompt não informa detalhes suficientes.

  

Um prompt melhor seria:

  

```text

Tenho uma função Python chamada somar(a, b), que retorna a soma de dois números.

Gere cenários de teste unitário para essa função, incluindo casos normais, casos com zero e casos com números negativos.

Não gere o código ainda. Primeiro, liste apenas os cenários com entrada e resultado esperado.

```

  

Esse prompt é melhor porque informa:

  

- a linguagem;

- o nome da função;

- o comportamento esperado;

- os tipos de cenário desejados;

- o formato da resposta.

  

---

  

## 8. Modelo de prompt para gerar cenários de teste

  

Use o modelo abaixo sempre que quiser pedir cenários de teste para uma IA.

  

```text

Atue como um professor de Teste de Software.

  

Tenho a seguinte função Python:

  

[Cole aqui a função]

  

Quero criar testes unitários usando unittest.

  

Antes de gerar o código, liste cenários de teste para essa função.

  

Para cada cenário, informe:

- nome do cenário;

- entrada usada;

- resultado esperado;

- tipo do cenário: caso normal, caso de borda ou caso de erro.

  

Use linguagem simples, pois sou iniciante em testes unitários.

```

  

---

  

## 9. Exemplo 1: usando IA para gerar cenários para `somar(a, b)`

  

Vamos imaginar que queremos testar a função:

  

```python

def  somar(a, b):

return a + b

```

  

Podemos usar o seguinte prompt:

  

```text

Atue como um professor de Teste de Software.

  

Tenho a seguinte função Python:

  
  

def somar(a, b):

return a + b

  
  

Quero criar testes unitários usando unittest.

  

Antes de gerar o código, liste cenários de teste para essa função.

  

Para cada cenário, informe:

- nome do cenário;

- entrada usada;

- resultado esperado;

- tipo do cenário: caso normal, caso de borda ou caso de erro.

  

Use linguagem simples, pois sou iniciante em testes unitários.

```

  

A IA poderia responder algo parecido com:

  
| Cenário | Entrada | Resultado esperado | Tipo |
| :--- | :--- | :--- | :--- |
| Somar dois positivos | `somar(2, 3)` | `5` | caso normal |
| Somar positivo com zero | `somar(5, 0)` | `5` | caso de borda |
| Somar dois zeros | `somar(0, 0)` | `0` | caso de borda |
| Somar negativo com positivo | `somar(-2, 5)` | `3` | caso normal |
| Somar dois negativos | `somar(-2, -3)` | `-5` | caso normal |

  

Agora podemos transformar esses cenários em testes.

  

```python

def  test_somar(self):

self.assertEqual(somar(2, 3), 5)

self.assertEqual(somar(5, 0), 5)

self.assertEqual(somar(0, 0), 0)

self.assertEqual(somar(-2, 5), 3)

self.assertEqual(somar(-2, -3), -5)

```

  

---

  

## 10. Exemplo 2: pedindo para a IA gerar código de teste

  

Depois de analisar os cenários, podemos pedir para a IA gerar o código.

  

Prompt:

  

```text

Agora transforme os cenários anteriores em testes unitários usando Python e unittest.

  

Considere que a função somar(a, b) está no arquivo calculadora.py.

  

Gere apenas o método de teste que deve ser colocado dentro da classe TestCalculadora.

```

  

Resposta esperada:

  

```python

def  test_somar(self):

self.assertEqual(somar(2, 3), 5)

self.assertEqual(somar(5, 0), 5)

self.assertEqual(somar(0, 0), 0)

self.assertEqual(somar(-2, 5), 3)

self.assertEqual(somar(-2, -3), -5)

```

  

Observe que a IA gerou apenas o método de teste, como foi solicitado.

  

Isso evita que ela recrie o arquivo inteiro sem necessidade.

  

---

  

## 11. Exemplo 3: usando IA para testar exceções

  

Agora vamos usar IA para pensar em testes para a função `calcular_media(lista)`.

  

Função:

  

```python

def  calcular_media(lista):

if  len(lista) == 0:

raise  ValueError("A lista não pode estar vazia.")

  

return  sum(lista) / len(lista)

```

  

Prompt:

  

```text

Tenho a seguinte função Python:

  
  

def calcular_media(lista):

if len(lista) == 0:

raise ValueError("A lista não pode estar vazia.")

  

return sum(lista) / len(lista)

  
  

Quero criar testes unitários usando unittest.

  

Liste cenários de teste para essa função, incluindo:

- lista com números inteiros;

- lista com números decimais;

- lista com números negativos;

- lista com apenas um elemento;

- lista vazia gerando ValueError.

  

Informe entrada, resultado esperado e tipo de cenário.

```

  

A IA poderia sugerir:

  


| Cenário | Entrada | Resultado esperado | Tipo |
| :--- | :--- | :--- | :--- |
| Média de inteiros | `` | `8` | caso normal |
| Média de decimais | `[2.5, 7.5]` | `5.0` | caso normal |
| Média com negativos | `[-2, -4, -6]` | `-4` | caso normal |
| Lista com um elemento | `` | `10` | caso de borda |
| Lista vazia | `[]` | `ValueError` | caso de erro |
  

Código de teste:

  

```python

def  test_calcular_media(self):

self.assertEqual(calcular_media([10, 8, 6]), 8)

self.assertEqual(calcular_media([2.5, 7.5]), 5.0)

self.assertEqual(calcular_media([-2, -4, -6]), -4)

self.assertEqual(calcular_media([10]), 10)

  
  

def  test_calcular_media_lista_vazia(self):

with  self.assertRaises(ValueError):

calcular_media([])

```

  

---

  

## 12. Melhorando os testes com `subTest`

  

Quando temos muitos casos parecidos, podemos usar `subTest`.

  

O `subTest` permite testar várias entradas dentro do mesmo método, mas mostrando melhor qual caso falhou.

  

Exemplo sem `subTest`:

  

```python

def  test_somar(self):

self.assertEqual(somar(2, 3), 5)

self.assertEqual(somar(0, 0), 0)

self.assertEqual(somar(-2, 5), 3)

```

  

Exemplo com `subTest`:

  

```python

def  test_somar_com_varios_casos(self):

casos = [

(2, 3, 5),

(0, 0, 0),

(-2, 5, 3),

(-2, -3, -5),

]

  

for a, b, resultado_esperado in casos:

with  self.subTest(a=a, b=b):

self.assertEqual(somar(a, b), resultado_esperado)

```

  

### Explicação

  

A lista `casos` guarda várias combinações de teste.

  

Cada item possui:

  

```text

a, b, resultado esperado

```

  

O `for` percorre todos os casos.

  

O `subTest` ajuda a identificar qual entrada causou a falha.

  

---

  

## 13. Prompt para pedir testes usando `subTest`

  

Você pode pedir para a IA gerar testes usando `subTest`.

  

Prompt:

  

```text

Tenho a função Python somar(a, b).

  

Gere um método de teste usando unittest e subTest.

  

O teste deve verificar os seguintes casos:

- somar dois positivos;

- somar zero com zero;

- somar negativo com positivo;

- somar dois negativos.

  

Considere que a função já foi importada no arquivo de teste.

Gere apenas o método de teste.

```

  

Resposta esperada:

  

```python

def  test_somar_com_subtest(self):

casos = [

(2, 3, 5),

(0, 0, 0),

(-2, 5, 3),

(-2, -3, -5),

]

  

for a, b, esperado in casos:

with  self.subTest(a=a, b=b):

self.assertEqual(somar(a, b), esperado)

```

  

---

  

## 14. Atividade Prática 

  

Agora você irá usar IA para melhorar os testes do projeto.

  

### 14.1 Passo 1: escolha uma função

  

Escolha uma função do arquivo `calculadora.py`.

  

Sugestões:

  

-  `somar(a, b)`;

-  `subtrair(a, b)`;

-  `multiplicar(a, b)`;

-  `dividir(a, b)`;

-  `potencia(a, b)`;

-  `calcular_media(lista)`.

  

---

  

### 14.2 Passo 2: peça cenários para a IA

  

Use o prompt abaixo:

  

```text

Atue como um professor de Teste de Software.

  

Tenho a seguinte função Python:

  

[Cole aqui a função escolhida]

  

Quero criar testes unitários usando unittest.

  

Liste pelo menos 6 cenários de teste para essa função.

  

Para cada cenário, informe:

- nome do cenário;

- entrada;

- resultado esperado;

- tipo do cenário: caso normal, caso de borda ou caso de erro.

  

Não gere código ainda.

```

  

---

  

### 14.3 Passo 3: avalie os cenários gerados

  

Antes de copiar qualquer coisa, analise a resposta da IA.

  

Confira:

  

- os resultados esperados estão corretos?

- existe algum cenário repetido?

- existe algum cenário sem sentido?

- a IA inventou comportamento que a função não possui?

- existe algum caso importante faltando?

  

Se necessário, faça um novo pedido para a IA.

  

Exemplo:

  

```text

Revise os cenários anteriores.

Remova cenários repetidos e adicione casos de borda importantes.

Explique brevemente por que cada cenário é útil.

```

  

---

  

### 14.4 Passo 4: peça o código dos testes

  

Depois de aprovar os cenários, peça o código:

  

```text

Agora transforme os cenários aprovados em testes unitários usando Python e unittest.

  

Considere que a função já foi importada no arquivo test_calculadora.py.

  

Gere apenas o método de teste que deve ser colocado dentro da classe TestCalculadora.

Use nomes de métodos iniciando com test_.

```

  

---

  

### 14.5 Passo 5: cole o código no projeto

  

Abra o arquivo `test_calculadora.py`.

  

Cole o método gerado dentro da classe `TestCalculadora`.

  

Cuidado: não cole o método fora da classe.

  

Exemplo correto:

  

```python

class  TestCalculadora(unittest.TestCase):

  

def  test_somar(self):

self.assertEqual(somar(2, 3), 5)

```

  

Exemplo incorreto:

  

```python

class  TestCalculadora(unittest.TestCase):

pass

  
  

def  test_somar(self):

self.assertEqual(somar(2, 3), 5)

```

  

---

  

### 14.6 Passo 6: execute os testes

  

No terminal do VS Code, execute:

  

```bash

python  -m  unittest  discover

```

  

Se todos os testes passarem, aparecerá algo parecido com:

  

```bash

----------------------------------------------------------------------

Ran  10  tests  in  0.002s

  

OK

```

  

---

  

## 15. Atividade prática: criando testes para `dividir(a, b)` com IA

  

Agora vamos fazer uma atividade mais completa.

  

A função é:

  

```python

def  dividir(a, b):

return a / b

```

  

### 15.1 Primeiro prompt

  

Copie o prompt abaixo e envie para a ferramenta de IA:

  

```text

Atue como um professor de Teste de Software.

  

Tenho a seguinte função Python:

  
  

def dividir(a, b):

return a / b

  
  

Quero criar testes unitários usando unittest.

  

Liste cenários de teste para essa função, incluindo:

- divisão exata;

- divisão com resultado decimal;

- divisão de número negativo;

- divisão de zero por outro número;

- divisão por zero.

  

Para cada cenário, informe:

- nome do cenário;

- entrada;

- resultado esperado;

- tipo do cenário: caso normal, caso de borda ou caso de erro.

  

Não gere código ainda.

```

  

---

  

### 15.2 Cenários esperados

  

A resposta pode ser parecida com esta:

  
| Cenário | Entrada | Resultado esperado | Tipo |
| :--- | :--- | :--- | :--- |
| Divisão exata | `dividir(10, 2)` | `5` | caso normal |
| Divisão decimal | `dividir(5, 2)` | `2.5` | caso normal |
| Divisão com negativo | `dividir(-10, 2)` | `-5` | caso normal |
| Zero dividido por número | `dividir(0, 5)` | `0` | caso de borda |
| Divisão por zero | `dividir(10, 0)` | `ZeroDivisionError` | caso de erro |

  

---

  

### 15.3 Segundo prompt

  

Agora peça o código:

  

```text

Transforme os cenários anteriores em testes unitários usando Python e unittest.

  

Considere que a função dividir(a, b) já foi importada.

  

Gere apenas os métodos de teste para serem colocados dentro da classe TestCalculadora.

```

  

---

  
## 16. Verificando se a IA gerou um teste correto

  

Nem todo teste gerado pela IA é bom.

  

Veja alguns problemas comuns.

  

---

  

### 16.1 A IA pode inventar função que não existe

  

Exemplo ruim:

  

```python

self.assertEqual(calculadora.dividir_seguro(10, 0), None)

```

  

Problema:

  

A função `dividir_seguro` não existe no projeto.

  

Como corrigir:

  

Use apenas funções existentes, como:

  

```python

dividir(10, 0)

```

  

---

  

### 16.2 A IA pode assumir comportamento que não foi definido

  

Exemplo ruim:

  

```python

self.assertEqual(dividir(10, 0), "Erro")

```

  

Problema:

  

A função `dividir(a, b)` não retorna a string `"Erro"`.

  

Ela gera `ZeroDivisionError`.

  

Teste correto:

  

```python

with  self.assertRaises(ZeroDivisionError):

dividir(10, 0)

```

  

---

  

### 16.3 A IA pode esquecer imports

  

Exemplo:

  

```python

def  test_potencia(self):

self.assertEqual(potencia(2, 3), 8)

```

  

Se a função `potencia` não foi importada, ocorrerá erro.

  

Confira se no início do arquivo existe algo como:

  

```python

from calculadora import potencia

```

  

Ou:

  

```python

from calculadora import somar, subtrair, multiplicar, dividir, potencia

```

  

---

  

### 16.4 A IA pode gerar teste fora do padrão do `unittest`

  

Exemplo ruim:

  

```python

def  deve_somar_dois_numeros(self):

self.assertEqual(somar(2, 3), 5)

```

  

Problema:

  

O método não começa com `test_`.

  

Correção:

  

```python

def  test_deve_somar_dois_numeros(self):

self.assertEqual(somar(2, 3), 5)

```

  

---

  

## 17. Prompt para revisar testes gerados

  

Depois que a IA gerar um teste, você pode pedir para ela revisar.

  

Use este prompt:

  

```text

Revise os testes unitários abaixo.

  

Verifique:

- se os métodos começam com test_;

- se os resultados esperados estão corretos;

- se há testes repetidos;

- se existem cenários importantes faltando;

- se há erro de importação;

- se os testes estão compatíveis com unittest.

  

Código:

  

[Cole aqui o código dos testes]

  

Explique os problemas encontrados em linguagem simples e sugira correções.

```

  

---

  

## 18. Criando uma tabela de planejamento de testes com IA

  

Antes de escrever código, é uma boa prática organizar os cenários em uma tabela.

  

Você pode pedir para a IA criar uma tabela.

  

Prompt:

  

```text

Crie uma tabela de planejamento de testes para a função abaixo:

  

[Cole aqui a função]

  

A tabela deve conter as colunas:

- ID do teste;

- cenário;

- entrada;

- resultado esperado;

- tipo de cenário;

- observação.

  

Não gere código ainda.

```

  

Exemplo de tabela:

  


| ID | Cenário | Entrada | Resultado esperado | Tipo | Observação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T01 | Somar dois positivos | `somar(2, 3)` | `5` | normal | caso básico |
| T02 | Somar com zero | `somar(5, 0)` | `5` | borda | verifica elemento neutro |
| T03 | Somar negativos | `somar(-2, -3)` | `-5` | normal | verifica sinal negativo |

  

Essa tabela pode ser colocada no README do projeto.

  

---

  

## 19. Atualizando o arquivo de testes completo

  

Depois de usar IA para melhorar os testes, o arquivo `test_calculadora.py` pode ficar assim:

  

```python

# test_calculadora.py

  

import unittest

  

from calculadora import (

somar,

subtrair,

multiplicar,

dividir,

potencia,

calcular_media,

)

  
  

class  TestCalculadora(unittest.TestCase):

  

def  test_somar_com_varios_casos(self):

casos = [

(2, 3, 5),

(5, 0, 5),

(0, 0, 0),

(-2, 5, 3),

(-2, -3, -5),

]

  

for a, b, esperado in casos:

with  self.subTest(a=a, b=b):

self.assertEqual(somar(a, b), esperado)

  

def  test_subtrair_com_varios_casos(self):

casos = [

(10, 5, 5),

(5, 10, -5),

(0, 0, 0),

(-5, -2, -3),

]

  

for a, b, esperado in casos:

with  self.subTest(a=a, b=b):

self.assertEqual(subtrair(a, b), esperado)

  

def  test_multiplicar_com_varios_casos(self):

casos = [

(3, 4, 12),

(5, 0, 0),

(-2, 3, -6),

(-2, -3, 6),

]

  

for a, b, esperado in casos:

with  self.subTest(a=a, b=b):

self.assertEqual(multiplicar(a, b), esperado)

  

def  test_dividir_com_varios_casos(self):

casos = [

(10, 2, 5),

(5, 2, 2.5),

(-10, 2, -5),

(0, 5, 0),

]

  

for a, b, esperado in casos:

with  self.subTest(a=a, b=b):

self.assertEqual(dividir(a, b), esperado)

  

def  test_dividir_por_zero(self):

with  self.assertRaises(ZeroDivisionError):

dividir(10, 0)

  

def  test_potencia_com_varios_casos(self):

casos = [

(2, 3, 8),

(5, 0, 1),

(10, 2, 100),

(2, -1, 0.5),

]

  

for a, b, esperado in casos:

with  self.subTest(a=a, b=b):

self.assertEqual(potencia(a, b), esperado)

  

def  test_calcular_media_com_varios_casos(self):

casos = [

([10, 8, 6], 8),

([2.5, 7.5], 5.0),

([-2, -4, -6], -4),

([10], 10),

([0, 0, 0], 0),

]

  

for lista, esperado in casos:

with  self.subTest(lista=lista):

self.assertEqual(calcular_media(lista), esperado)

  

def  test_calcular_media_lista_vazia(self):

with  self.assertRaises(ValueError):

calcular_media([])

  
  

if  __name__ == "__main__":

unittest.main()

```

  

---

  

## 20. Executando os testes novamente

  

Depois de atualizar o arquivo, execute:

  

```bash

python  -m  unittest  discover

```

  

Se tudo estiver correto, a saída será parecida com:

  

```bash

----------------------------------------------------------------------

Ran  8  tests  in  0.002s

  

OK

```

  

A quantidade de testes pode variar de acordo com o número de métodos criados.

  

---

  

## 21. Atividade final

  

Agora cada aluno deverá escolher uma das funções do projeto e usar IA para apoiar a criação de testes.

  

### O que entregar

  

Cada aluno deverá entregar:

  

1. a função escolhida;

2. o prompt usado para pedir cenários à IA;

3. a tabela de cenários gerada;

4. uma análise dizendo quais cenários foram aceitos, alterados ou removidos;

5. o código final dos testes em `unittest`;

6. uma captura ou cópia da saída do terminal mostrando os testes executados;

7. o link do repositório no GitHub. Sendo o mesmo repositório da atividade anterior, mas com os arquivos separados. 

  

---

  

## 22. Modelo de registro da atividade no README

  

Copie o modelo abaixo para documentar sua atividade.

  

```markdown

## Uso de IA para geração de cenários de teste

  

### Função escolhida

  

`dividir(a, b)`

  

### Prompt utilizado

  

```text

Cole aqui o prompt usado na ferramenta de IA.

```

  

### Cenários sugeridos pela IA

  


| ID | Cenário | Entrada | Resultado esperado | Tipo |
| :--- | :--- | :--- | :--- | :--- |
| T01 | Divisão exata | `dividir(10, 2)` | `5` | normal |
| T02 | Divisão decimal | `dividir(5, 2)` | `2.5` | normal |
| T03 | Divisão por zero | `dividir(10, 0)` | `ZeroDivisionError` | erro |

  

### Análise dos cenários

  

Descreva aqui quais cenários você aceitou, removeu ou alterou.

  

### Código final dos testes

  

```python

def  test_dividir_por_zero(self):

with  self.assertRaises(ZeroDivisionError):

dividir(10, 0)

```

  

### Resultado da execução

  

```bash

python  -m  unittest  discover

```

  

Saída obtida:

  

```bash

----------------------------------------------------------------------

Ran  8  tests  in  0.002s

  

OK

```

```

  

---

  


  

## 24. Checklist final

  

Antes de entregar, confira:

  

- [ ] escolhi uma função para testar;

- [ ] escrevi um prompt claro para a IA;

- [ ] pedi cenários antes de pedir código;

- [ ] analisei os cenários sugeridos;

- [ ] removi ou corrigi cenários ruins;

- [ ] gerei testes usando `unittest`;

- [ ] conferi se os métodos começam com `test_`;

- [ ] executei os testes no terminal;

- [ ] corrigi erros encontrados;

- [ ] documentei o uso da IA no README;

- [ ] subi o projeto para o GitHub.

  

---

  

