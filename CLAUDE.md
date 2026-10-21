# Piscine Python — 42 (42x02a)

Repositório com as listas (módulos) da Piscine Python da 42. Cada módulo fica em
`modXX/` e cada exercício em `modXX/exN/`, um arquivo por exercício. Os subjects
(PDF), os anexos e as notas dos módulos ficam em `notes/`.

**Este é o repo pessoal do aluno (GitHub), não o repo de entrega.** O aluno
desenvolve aqui e depois copia os arquivos pedidos para os repositórios de
entrega da 42. Por isso, arquivos extras aqui (`main.py` e outros anexos da
intra, `notes/`, `CLAUDE.md`, `.venv` etc.) **não são problema**: não aponte isso
como erro. Na hora de copiar, só os arquivos pedidos em cada exercício vão para
a entrega. Estruturas que o subject exige "na raiz do repo" (mod05bis, mod06bis)
ficam aqui dentro de `modXX/`.

## Como o trabalho é avaliado

- Entrega via git, no repo de entrega da 42 (não este). Só o que está lá é
  avaliado, e devem ir **apenas** os arquivos pedidos.
- **Avaliação em pares (defesa)**: o aluno precisa explicar o que fez, como fez e
  o conceito por trás de cada exercício. O avaliador pode pedir para alterar ou
  estender o código ao vivo.
- Todos os subjects têm regras de uso de IA: só entregar código que o aluno
  entende e consegue defender. Por isso, **ao ajudar: explique o porquê, aponte
  problemas e deixe o aluno escrever/decidir**. Só escreva a solução completa se
  ele pedir explicitamente.
- **Comandos de terminal (git, pip, venv etc.): passe o comando e explique o que
  ele faz, mas não execute.** O aluno quer rodar sozinho para aprender. Comandos
  só de leitura para investigar (ler arquivo, `git status`, rodar
  flake8/mypy/script) podem ser executados.

## Regras gerais (valem para todos os módulos)

- Python 3.10+ (as máquinas da escola rodam CPython 3.10.12).
- `flake8` sem nenhum aviso (limite de 79 colunas, E501 é o mais comum).
- Type hints em **todas** as funções e métodos (incluindo `-> None` e
  `__init__`), verificados com `mypy`. Exceção: no mod00 eles são opcionais
  nos ex0–ex6.
- Nomes: classes em `PascalCase`, funções e variáveis em `snake_case`.
- Usar só as funções e imports listados em "Authorized" de cada exercício
  (keywords como `class`, `def`, `try`, `raise`, `with`, `yield` e o
  `if __name__ == "__main__":` são sempre permitidos, exceto no mod00, onde
  o `if __name__` é proibido).
- O programa nunca pode quebrar (exceto onde o subject pede um erro de propósito).
- O output dos exemplos não é cobrado caractere por caractere, mas a estrutura
  deve ser mantida.

## Ambiente local (igual ao da escola)

```bash
brew install python@3.10
python3.10 -m venv .venv          # .venv já está no .gitignore
source .venv/bin/activate
pip install "flake8==4.0.1" "mccabe==0.6.1" "pycodestyle==2.8.0" \
            "pyflakes==2.4.0" "mypy==0.942"
```

Checagem antes de entregar:

```bash
.venv/bin/flake8 mod01
.venv/bin/mypy mod01/exN/arquivo.py
```

## Módulos

Notas detalhadas de todos os módulos (regras específicas, proposta de cada
exercício, status, perguntas de defesa): [notes/MODULES.md](notes/MODULES.md).

| Módulo | Tema | Subject | Status |
|--------|------|---------|--------|
| 00 | Growing Code: fundamentos | [PDF](notes/42x02.python00.en.subject.pdf) + [main.py](notes/42x02.python00.main.py) | Concluído |
| 01 | Code Cultivation: POO | [PDF](notes/42x02.python01.en.subject.pdf) | **Em andamento** (ex3) |
| 02 | Garden Guardian: exceções | [PDF](notes/42x02.python02.en.subject.pdf) | Não iniciado |
| 03 | Data Quest: coleções | [PDF](notes/42x02.python03.en.subject.pdf) | Não iniciado |
| 04 | Data Archivist: arquivos | [PDF](notes/42x02.python04.en.subject.pdf) | Não iniciado |
| 05bis | The Codex: venv, pacotes, imports | [PDF](notes/42x02.python05bis.en.subject.pdf) | Não iniciado |
| 06bis | Code Nexus: ABC, polimorfismo, patterns | [PDF](notes/42x02.python06bis.en.subject.pdf) | Não iniciado |
| 07, 08 | — | **faltando** | — |
| 09 | Cosmic Data: Pydantic | [PDF](notes/42x02.python09.en.subject.pdf) + [tools](notes/42x02.python09data_generator.tar) | Não iniciado |

Arco geral: sintaxe → POO → exceções → coleções/generators → arquivos →
ambientes e pacotes → arquitetura abstrata e design patterns → validação com
Pydantic.

Antes de ajudar, leia em `notes/MODULES.md` a seção do módulo em que o aluno
está. Ao concluir um exercício, atualize o status lá e nesta tabela.
