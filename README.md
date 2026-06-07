# Teste Unitário em Python

Atividade prática de testes unitários usando `unittest` - disciplina de Engenharia de Software (GCC188) na UFLA.

## Pré-requisitos

- Python 3.x
- VS Code (opcional)

## Como executar os testes

```bash
python -m unittest discover
```

## Modo interativo

Criei um `main.py` para facilitar a interação com a calculadora sem precisar ficar abrindo o Python manualmente. Dá pra testar cada função pelo terminal mesmo.

```bash
python main.py
```

Exemplo de uso:

```
--- Calculadora ---
  1. Somar
  2. Subtrair
  3. Multiplicar
  4. Dividir
  5. Potencia
  6. Media de lista
  0. Sair

Escolha uma opcao: 6
Digite os numeros separados por virgula: 4, 8, 15, 16, 23, 42
Resultado: 18.0
```

## Uso de IA para geração de cenários de teste

### Função escolhida

`dividir(a, b)`

### Prompt utilizado

> Estou fazendo uma atividade de testes unitários em Python com unittest. Tenho uma função chamada `dividir(a, b)` que retorna `a / b` sem tratar divisão por zero. Já tenho testes básicos cobrindo divisão exata, resultado decimal, negativo e numerador zero. Quais outros cenários de teste você sugere para cobrir casos de fronteira e combinações menos óbvias?

### Cenários sugeridos pela IA

| ID   | Cenário                        | Entrada        | Resultado esperado | Tipo       |
|------|--------------------------------|----------------|--------------------|------------|
| CT01 | Dividir por 1                  | a=9, b=1       | 9.0                | fronteira  |
| CT02 | Dividir por -1                 | a=9, b=-1      | -9.0               | fronteira  |
| CT03 | Dois negativos                 | a=-6, b=-2     | 3.0                | funcional  |
| CT04 | Divisão entre floats           | a=1.5, b=0.5   | 3.0                | funcional  |
| CT05 | Números grandes                | a=1000000, b=1000 | 1000.0          | fronteira  |
| CT06 | Dividir por zero               | a=5, b=0       | ZeroDivisionError  | exceção    |
| CT07 | Numerador float, divisor inteiro | a=5.0, b=2   | 2.5                | funcional  |

### Análise dos cenários

Aceitei CT01 a CT05 direto - eram casos que eu não tinha pensado, especialmente o de dois negativos e o de floats. O CT06 (divisão por zero) eu já tinha num método separado, então não duplicou. O CT07 eu deixei de fora porque o comportamento é idêntico ao caso decimal que já existe - não acrescentava cobertura real.

O ponto mais útil foi o CT04 (floats): a IA recomendou usar `assertAlmostEqual` no lugar de `assertEqual` pra evitar problema com precisão de ponto flutuante. Acabei aplicando isso em todos os casos do método novo.

### Código final dos testes

```python
def test_dividir_cenarios_ia(self):
    """Cenários gerados com IA para cobrir casos de fronteira e combinações menos óbvias."""
    casos = [
        (9, 1, 9.0),      # dividir por 1 retorna o proprio valor
        (9, -1, -9.0),    # dividir por -1 inverte o sinal
        (-6, -2, 3.0),    # dois negativos resultam em positivo
        (1.5, 0.5, 3.0),  # divisao entre floats
        (1_000_000, 1_000, 1_000.0),  # numeros grandes
    ]
    for a, b, esperado in casos:
        with self.subTest(a=a, b=b):
            self.assertAlmostEqual(dividir(a, b), esperado)
```

### Resultado da execução

```
test_dividir_cenarios_ia (test_calculadora.TestCalculadora.test_dividir_cenarios_ia)
Cenários gerados com IA para cobrir casos de fronteira e combinações menos óbvias. ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

## Estrutura

```
/
├── calculadora.py       # funções matemáticas
├── test_calculadora.py  # testes unitários
├── main.py              # interface interativa no terminal
└── README.md
```
