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

## Estrutura

```
/
├── calculadora.py       # funções matemáticas
├── test_calculadora.py  # testes unitários
├── main.py              # interface interativa no terminal
└── README.md
```
