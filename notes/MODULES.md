# Módulos da Piscine Python — notas

Um resumo por módulo: regras específicas, proposta de cada exercício, status e
perguntas de defesa. As regras gerais e o ambiente estão no `CLAUDE.md` da raiz.
Os links para PDFs são relativos a esta pasta (`notes/`).

- [Module 00 — Growing Code](#module-00--growing-code-python-fundamentals-through-garden-data)
- [Module 01 — Code Cultivation](#module-01--code-cultivation-object-oriented-garden-systems)
- [Module 02 — Garden Guardian](#module-02--garden-guardian-data-engineering-for-smart-agriculture)
- [Module 03 — Data Quest](#module-03--data-quest-mastering-python-collections)
- [Module 04 — Data Archivist](#module-04--data-archivist-digital-preservation-in-the-cyber-archives)
- [Module 05bis — The Codex](#module-05bis--the-codex-packages-environments-and-the-alchemists-toolchain)
- [Module 06bis — Code Nexus](#module-06bis--code-nexus-abstract-architecture-from-data-streams-to-battle-strategies)
- [Module 09 — Cosmic Data](#module-09--cosmic-data-discover-pydantic-models--validation)

Módulos 07 e 08: subject faltando.

---

## Module 00 — Growing Code: Python Fundamentals Through Garden Data

Subject: [42x02.python00.en.subject.pdf](42x02.python00.en.subject.pdf) (v3.0)
Testador: [42x02.python00.main.py](42x02.python00.main.py) (igual ao `mod00/main.py`)
Código: `mod00/exN/`

### Resumo

Primeiro contato com Python: expressões, variáveis, funções, `input`/`print`,
condicionais, laços e recursão, terminando com type hints.

Regras específicas deste módulo (diferentes de todos os outros):
- Cada arquivo contém **só a função pedida**, com o nome exato. **Proibido**
  usar `if __name__ == "__main__":`, chamar a função no próprio arquivo ou
  escrever código fora de funções.
- A função faz o input e o output diretamente.
- Não precisa validar entrada. Com número negativo ou inválido, o comportamento
  é indefinido.
- Type hints são **opcionais** nos ex0–ex6 e **obrigatórios** no ex7 (checar com
  mypy).
- Para testar, use o `main.py` fornecido: copie para a pasta do exercício (ou o
  exercício para a pasta do `main.py`) e rode `python3 main.py`. Ele importa o
  arquivo e chama a função. O `main.py` não faz parte da entrega.

### Exercícios

| Ex | Arquivo | Permitido | Conceito central |
|----|---------|-----------|------------------|
| 0 | `ex0/ft_hello_garden.py` | `print()` | Definir uma função |
| 1 | `ex1/ft_garden_name.py` | `input()`, `print()` | Ler entrada, f-string, mensagem fixa |
| 2 | `ex2/ft_plot_area.py` | `input()`, `int()`, `print()` | Converter `str` → `int`, aritmética (área) |
| 3 | `ex3/ft_harvest_total.py` | `input()`, `int()`, `print()` | Acumular valores (soma de 3 dias) |
| 4 | `ex4/ft_plant_age.py` | `input()`, `int()`, `print()` | `if`/`else` (estritamente > 60 dias → colher) |
| 5 | `ex5/ft_water_reminder.py` | `input()`, `int()`, `print()` | `if`/`else` (> 2 dias → regar) |
| 6 | `ex6/ft_count_harvest_iterative.py` e `_recursive.py` | `input()`, `int()`, `print()`, `range()`, funções auxiliares | O mesmo problema com laço e com recursão |
| 7 | `ex7/ft_seed_inventory.py` | `print()`, métodos de string | Type hints, `if`/`elif`/`else`, `str.capitalize()` |

Detalhes:
- **ex6**: as duas versões devem dar output idêntico. Na recursiva, vale uma
  função auxiliar aninhada, um parâmetro com valor padrão ou uma auxiliar
  separada.
- **ex7**: a assinatura deve ser exatamente
  `def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:`.
  Unidades: `packets` ("available"), `grams` ("total") e `area` ("covers X
  square meters"). Qualquer outra imprime **só** `Unknown unit type`.

### Status

Concluído. Conferido contra o subject em 2026-10-21: nomes de arquivos e
funções, regras e outputs batem. Nada pendente.

### Perguntas de defesa prováveis

O subject avisa: podem pedir para explicar o código, **seguir a execução passo a
passo** ou modificar a solução ao vivo.

- O que `input()` retorna? (Sempre `str`, por isso o `int()`.) E se digitar
  `"abc"`? (`ValueError`, mas aqui é comportamento indefinido.)
- Por que neste módulo não pode ter `if __name__ == "__main__"`? (O `main.py`
  importa o arquivo. Código solto rodaria no import.)
- ex4: por que `> 60` e não `>= 60`? (O subject diz "strictly more than 60".)
- ex6: como funciona a recursão? Qual é o caso base? Por que o `print` vem
  **depois** da chamada recursiva? (Para imprimir em ordem crescente: desce até
  1 e imprime voltando.) Quais os limites da recursão? (Profundidade máxima de
  ~1000 por padrão → `RecursionError`.)
- ex7: o que são type hints? O Python os impõe em execução? (Não, quem verifica
  é o `mypy`.)

---

## Module 01 — Code Cultivation: Object-Oriented Garden Systems

Subject: [42x02.python01.en.subject.pdf](42x02.python01.en.subject.pdf) (v3.2)
Código: `mod01/exN/`

### Resumo

Continuação do módulo 00. A ideia é construir, aos poucos, um sistema de
gerenciamento de jardim e aprender **Programação Orientada a Objetos** no
caminho. É uma única classe `Plant` que vai evoluindo: cada exercício **reaproveita
e melhora** a classe do anterior. A partir do ex1 é obrigatório usar classes.

Arco de aprendizado:
estrutura de programa → classe/objeto → métodos (comportamento) → construtor →
encapsulamento → herança → static/class methods, classes aninhadas e polimorfismo.

### Exercícios

| Ex | Arquivo | Permitido | Conceito central |
|----|---------|-----------|------------------|
| 0 | `ex0/ft_garden_intro.py` | `print()` | Ponto de entrada, `if __name__ == "__main__":`, shebang |
| 1 | `ex1/ft_garden_data.py` | `print()` | Classe como modelo, instância, atributos, método `show()` |
| 2 | `ex2/ft_plant_growth.py` | `print()`, `range()`, `round()` | Métodos que alteram o estado (`grow()`, `age()`) |
| 3 | `ex3/ft_plant_factory.py` | `print()`, `range()`, `round()` | Construtor `__init__`: instanciar e inicializar ao mesmo tempo |
| 4 | `ex4/ft_garden_security.py` | `print()`, `range()`, `round()` | Encapsulamento: getters/setters, validação, convenção `_protected` |
| 5 | `ex5/ft_plant_types.py` | + `super()` | Herança (`Flower`, `Tree`, `Vegetable`), `super()`, sobrescrita de métodos |
| 6 | `ex6/ft_garden_analytics.py` | + `staticmethod()`, `classmethod()` | Static/class methods, classe aninhada, cadeia de herança, polimorfismo |

#### Proposta de cada exercício

- **ex0 — Planting Your First Seed**: entender onde a execução começa. Guardar
  nome/altura/idade em variáveis e imprimir. Na defesa: explicar por que usar
  `if __name__ == "__main__":` (o código não roda quando o arquivo é
  *importado*, só quando é executado direto) e **adicionar o shebang ao vivo**
  (`#!/usr/bin/env python3` + `chmod +x` → `./ft_garden_intro.py`).
- **ex1 — Garden Data Organizer**: sair de "uma variável por dado" para uma classe
  `Plant` que serve de molde. Instanciar pelo menos 3 plantas, setar os atributos
  depois de criar e exibir com `show()`. Pergunta do subject: que problemas surgem
  com muitas plantas? (repetição, esquecer de setar algum atributo.)
- **ex2 — Plant Growth Simulator**: reaproveitar `Plant` e dar comportamento:
  `grow()` e `age()` como métodos. Simular 7 dias e exibir o crescimento total.
  Plantas diferentes podem crescer de jeitos diferentes (ex.: atributo de taxa).
- **ex3 — Plant Factory**: resolver o problema do ex1 com um construtor
  (`__init__`). A planta já nasce com nome, altura e idade e fica **pronta para
  usar** (por exemplo, `grow()`). Criar 5+ plantas e exibir. O `show()` deve
  poder ser usado **sem alteração** em relação aos exercícios anteriores.
- **ex4 — Garden Security System**: proteger os dados. Atributos "protegidos"
  (`self._height`, *não* `self.__height`/mangling), `get_height()`/`get_age()`,
  `set_height()`/`set_age()` que rejeitam valores negativos e imprimem o erro a
  partir da própria classe, mantendo o valor antigo (ou um padrão na criação).
- **ex5 — Specialized Plant Types**: herança. `Flower` (color, `bloom()`), `Tree`
  (trunk_diameter, `produce_shade()`), `Vegetable` (harvest_season,
  nutritional_value, que começa em 0 e sobe com `age()`/`grow()`). Usar `super()`
  no `__init__` e no `show()`. Nada de duplicar código comum.
- **ex6 — Garden Analytics**: juntar tudo. Static method (idade > 1 ano?), class
  method (planta "anônima": `Unknown plant`, 0.0cm, 0 dias), `Seed(Flower)` com
  número de sementes depois de florescer, classe aninhada de estatísticas
  (contagem de chamadas a grow/age/show, encapsulada), `Tree` conta
  `produce_shade()`, e uma função **fora das classes** que mostra as estatísticas
  de qualquer planta (polimorfismo).

### Status

- [x] ex0
- [x] ex1
- [x] ex2
- [ ] ex3 — feito, faltam ajustes (ver abaixo)
- [ ] ex4
- [ ] ex5
- [ ] ex6

#### Pendências de revisão do ex3 (2026-10-21)

1. A classe não tem `grow()`/`age()`. O subject pede que a planta fique pronta
   para `grow()` logo depois de criada, e diz "Improve your Plant class from the
   previous exercises". Trazer os métodos do ex2.
2. O `show()` foi alterado para incluir `"Created: "`. O subject diz que o
   `show()` deve ser usado **sem alteração**. Manter o formato do ex2
   (`Rose: 25.0cm, 30 days old`) e colocar o prefixo fora dele.
3. `__init__` sem `-> None`. O mypy 0.942 aceita, mas a regra é type hint em
   tudo.
4. Nomes `s_height`/`s_age`: depois de um `grow()` deixam de ser a altura
   "inicial". Cuidado: um atributo `self.age` esconderia o método `age()`
   (foi por isso que o ex2 usou `time`).

### Perguntas de defesa — ex3 (com gabarito)

1. **O que é `__init__` e quando ele é chamado?** É o método inicializador. O
   Python chama automaticamente logo depois de criar o objeto, quando você faz
   `Plant(...)`.
2. **O que é `self`?** É a referência para a instância que está sendo
   criada/usada. `self.name = name` grava o atributo *naquele* objeto.
3. **Qual a diferença entre o ex1 e o ex3?** No ex1 o objeto nasce vazio e os
   atributos são setados um a um (dá para esquecer algum → `AttributeError`). No
   ex3 o construtor obriga a passar tudo na criação.
4. **Diferença entre classe e instância?** Classe é o molde (`Plant`). Instância
   é cada objeto concreto (`plant1`, `plant2`), com seus próprios valores.
5. **E se eu chamar `Plant("Rose", 25)`?** `TypeError`: falta um argumento
   posicional obrigatório. (Daria para usar valores padrão: `s_age: int = 0`.)
6. **Por que `25` vira `25.0cm` na saída?** Por causa do format spec `:.1f` na
   f-string, que formata como float com 1 casa decimal.
7. **Por que passar `25` (int) funciona se o hint é `float`?** O mypy aceita
   `int` onde se espera `float` (promoção numérica). E type hints não são
   checados em tempo de execução.
8. **Como criar as 5 plantas sem repetir 5 linhas?** Lista de objetos + `for`:
   `for plant in plants: plant.show()`.
9. **Tarefa ao vivo provável:** "faça a Rose crescer 3 dias e mostre", ou
   "adicione uma sexta planta".

---

## Module 02 — Garden Guardian: Data Engineering for Smart Agriculture

Subject: [42x02.python02.en.subject.pdf](42x02.python02.en.subject.pdf) (v3.0)
Código: `mod02/exN/`

### Resumo

**Tratamento de exceções.** O tema é um pipeline de dados de sensores agrícolas
que não pode cair quando chega dado ruim. Todos os exercícios exigem
`try`/`except`. As keywords `try`, `except`, `finally` e `raise` e qualquer
exceção built-in (`ValueError`, `TypeError`, `ZeroDivisionError`,
`FileNotFoundError`, `KeyError`, `Exception`...) são liberadas. O programa
**nunca** pode crashar e deve mostrar tanto o caso normal quanto o caso de erro.

Arco: capturar → lançar → distinguir tipos → criar os próprios → limpar sempre
(`finally`).

### Exercícios

| Ex | Arquivo | Permitido | Conceito central |
|----|---------|-----------|------------------|
| 0 | `ex0/ft_first_exception.py` | `int()`, `print()` | `try`/`except`: capturar o erro do `int("abc")` |
| 1 | `ex1/ft_raise_exception.py` | `int()`, `print()` | `raise`: lançar erro quando o valor é válido mas fora da regra (0–40 °C) |
| 2 | `ex2/ft_different_errors.py` | `print()`, `open()`, `int()` | Tipos diferentes de exceção, vários `except`, tupla de exceções |
| 3 | `ex3/ft_custom_errors.py` | `print()` | Exceções customizadas com herança (`GardenError` → `PlantError`, `WaterError`) |
| 4 | `ex4/ft_finally_block.py` | `print()`, `str.capitalize()` | `finally`: cleanup que sempre acontece |

#### Proposta de cada exercício

- **ex0**: `input_temperature(temp_str)` converte com `int()` e retorna.
  `test_temperature()` testa `"25"` e `"abc"`, captura a falha, imprime a
  mensagem da exceção e mostra que o programa continuou. Os type hints das duas
  funções ficam por sua conta.
- **ex1**: a mesma função, agora com `raise` se a temperatura for < 0 ou > 40
  (limites incluídos como válidos), com mensagens "too hot"/"too cold". Testar
  também `"100"` e `"-50"`.
- **ex2**: `garden_operations(operation_number)` com código defeituoso de
  propósito: 0 → `ValueError`, 1 → `ZeroDivisionError`, 2 → `FileNotFoundError`,
  3 → `TypeError` (str + int), e qualquer outro número retorna normalmente.
  `test_error_types()` mostra cada erro, explica, continua e demonstra **vários
  tipos em um único `try`** (`except (ValueError, TypeError) as e:`). É proibido
  usar `type()`. O mypy vai reclamar do `TypeError`, e isso é esperado.
- **ex3**: `GardenError(Exception)`, `PlantError(GardenError)` e
  `WaterError(GardenError)`, cada uma com mensagem padrão se nenhuma for
  passada. Mostrar a captura específica e que `except GardenError` pega as
  filhas.
- **ex4**: `water_plant(plant_name)` lança `PlantError` (do ex3) se o nome não
  estiver capitalizado. `test_watering_system()` abre o sistema (print), rega
  várias plantas, no erro **para e volta ao main**, e o `finally` sempre fecha o
  sistema.

### Status

- [ ] ex0  - [ ] ex1  - [ ] ex2  - [ ] ex3  - [ ] ex4

### Perguntas de defesa (tiradas do subject)

- Por que o Python tem tipos diferentes de erro? Como capturar vários tipos com
  um único `try`?
- Quando criar o próprio tipo de erro em vez de usar um built-in? Como a herança
  ajuda a organizar os erros?
- Por que limpar recursos mesmo quando dá erro? Como o `finally` garante isso,
  inclusive com `return` dentro do `except`?
- Diferença entre `except Exception` e `except ValueError`. Por que evitar o
  `except:` puro?
- O que `raise` faz com o fluxo do programa? E o `as e`?

---

## Module 03 — Data Quest: Mastering Python Collections

Subject: [42x02.python03.en.subject.pdf](42x02.python03.en.subject.pdf) (v3.0)
Código: `mod03/exN/`

### Resumo

**Estruturas de dados.** O tema é análise de dados de jogos. Cada exercício
"libera" uma coleção nova: list → tuple → set → dict → generator →
comprehensions. Quando um exercício introduz uma estrutura, todos os métodos
dela passam a ser permitidos. `str`, `int` e `float` com todos os métodos são
sempre permitidos.

Regras extras deste módulo:
- Primeiro contato com `import` (`sys`, `math`, `random`, `typing`).
- **Proibido I/O de arquivo**: tudo em memória ou via `sys.argv`.
- As funções devem tratar exceções para não crashar.

Mensagem do foreword: "your data structure is your algorithm". Buscar algo numa
lista é O(n). Num set/dict (hash) é O(1) em média.

### Exercícios

| Ex | Arquivo | Permitido | Conceito central |
|----|---------|-----------|------------------|
| 0 | `ex0/ft_command_quest.py` | `sys`, `sys.argv`, `len()`, `print()` | Listas: ler `sys.argv` |
| 1 | `ex1/ft_score_analytics.py` | + `sum()`, `max()`, `min()` | Criar lista nova, validar com `try`/`except`, estatísticas |
| 2 | `ex2/ft_coordinate_system.py` | `math`, `math.sqrt()`, `input()`, `round()`, `print()` | Tuplas (imutáveis): coordenadas 3D, distância euclidiana |
| 3 | `ex3/ft_achievement_tracker.py` | `len()`, `print()`, `random.*`, `set()`, `union`/`intersection`/`difference` | Sets: unicidade e operações de conjunto |
| 4 | `ex4/ft_inventory_system.py` | `sys.argv`, `len()`, `print()`, `sum()`, `list()`, `round()`, `dict.keys/values/update` | Dicts: parsing `item:qtd`, percentuais, máx/mín |
| 5 | `ex5/ft_data_stream.py` | `next()`, `range()`, `len()`, `print()`, `typing.Generator`, `random.*` | Generators com `yield`: streams infinitos e sob demanda |
| 6 | `ex6/ft_data_alchemist.py` | `random.*`, `print()`, `len()`, `sum()`, `round()` | List e dict comprehensions |

#### Proposta de cada exercício

- **ex0**: mostrar o nome do programa, a quantidade e cada argumento.
  `sys.argv[0]` é o próprio script. Prepare-se para discutir formas de não
  repetir o nome do programa (slice `sys.argv[1:]`, índice começando em 1...).
- **ex1**: converter os argumentos em `int` dentro de `try`, descartar os
  inválidos com mensagem e calcular total, média, máximo, mínimo e range. Sem
  nenhum válido → mensagem de uso.
- **ex2**: `get_player_pos()` pede `x,y,z`, trata entrada ruim (sintaxe errada,
  valor não numérico com mensagem do erro) e repete até ser válida. Retorna uma
  tupla. Calcular a distância até a origem e entre os dois pontos.
- **ex3**: `gen_player_achievements()` sorteia um set de conquistas de uma lista
  grande. Para 4+ jogadores: todas as distintas (união), as comuns a todos
  (interseção), as exclusivas de cada um e as que faltam para cada um
  (diferença). Calibrar os tamanhos para os sets não ficarem vazios.
- **ex4**: parsear `item:qtd` de `sys.argv`, descartar sintaxe inválida, item
  repetido e quantidade não numérica. Mostrar o inventário, a lista de itens, o
  total, o % de cada item, o mais e o menos abundante (empate → o primeiro) e
  adicionar um item novo no fim.
- **ex5**: `gen_event()` infinito retornando tuplas `(nome, ação)` aleatórias.
  Exibir 1000 eventos. Montar uma lista de 10. `consume_event(lista)` sorteia,
  remove e faz `yield` até a lista esvaziar, usado direto no `for ... in ...`.
- **ex6**: lista de nomes com e sem maiúscula. Comprehension 1: todos
  capitalizados. Comprehension 2: só os que já eram capitalizados. Dict
  comprehension nome → score aleatório e outra só com os acima da média. Cada
  comprehension em uma linha (salvo se passar de 79 colunas).

### Status

- [ ] ex0  - [ ] ex1  - [ ] ex2  - [ ] ex3  - [ ] ex4  - [ ] ex5  - [ ] ex6

### Perguntas de defesa (tiradas do subject)

- Por que escolher list, tuple, set ou dict em cada caso? O que é "hashable" e
  por que tupla pode ser chave de dict e lista não?
- Tupla é imutável: o que isso significa na prática?
- Como o Python imprime um set vazio, e por quê? (`set()`, porque `{}` é um dict
  vazio.)
- O que é um generator e por que ele economiza memória? O que acontece quando
  ele se esgota? (`StopIteration`.) Qual a diferença entre `yield` e `return`?
- Comprehension vs. loop com `append`: quando usar cada um?

---

## Module 04 — Data Archivist: Digital Preservation in the Cyber Archives

Subject: [42x02.python04.en.subject.pdf](42x02.python04.en.subject.pdf) (v3.0)
Código: `mod04/exN/`

### Resumo

**Operações com arquivos e streams.** Abrir, ler, escrever e fechar arquivos,
usar os três canais padrão (stdin/stdout/stderr) e, no fim, o `with` (context
manager). Todas as falhas (arquivo inexistente, sem permissão) devem ser
tratadas sem crashar.

Regras extras deste módulo:
- `str`, `int`, `float`, `list`, `dict`, `set` e `tuple` com todos os métodos
  são permitidos.
- **`with` é proibido até o ex3.** Nos ex0–ex2 é preciso fechar o arquivo na mão
  (`close()`), o que combina com o `finally` do mod02.
- O output pode ter mensagens próprias, desde que a estrutura e a informação
  essencial sejam mantidas.

Para testar, crie um `ancient_fragment.txt` com as três linhas do exemplo. Para
o erro de permissão no Mac, use `/etc/master.passwd`.

### Exercícios

| Ex | Arquivo | Permitido | Conceito central |
|----|---------|-----------|------------------|
| 0 | `ex0/ft_ancient_text.py` | `sys.argv`, `len()`, `open()`, `typing.IO`, `read()`, `close()`, `print()` | Abrir/ler/fechar, tratar `FileNotFoundError` e `PermissionError` |
| 1 | `ex1/ft_archive_creation.py` | + `write()`, `input()` | Transformar o conteúdo e escrever em arquivo (modo `"w"`) |
| 2 | `ex2/ft_stream_management.py` | + `sys.stdin/stdout/stderr`, `readline()`, `flush()` (sem `input()`) | Erros no stderr, ler entrada do stdin |
| 3 | `ex3/ft_vault_security.py` | `open()`, `read()`, `write()`, `print()` | `with` (context manager); função que retorna `(bool, str)` |

#### Proposta de cada exercício

- **ex0**: recebe o nome do arquivo por argumento (sem argumento → `Usage`),
  abre, mostra o conteúdo como o `cat` (com cabeçalho e rodapé) e fecha. Pergunta
  do subject: qual o tipo retornado por `open()`? (`TextIOWrapper`, um objeto
  de arquivo, anotado como `typing.IO[str]`.)
- **ex1**: o mesmo, mais adicionar `#` no fim de cada linha, exibir o resultado,
  perguntar o nome do arquivo de saída (vazio → não salva) e criar ou
  sobrescrever o arquivo.
- **ex2**: as mensagens de erro vão para o **stderr** com o prefixo `[STDERR]`, e
  a entrada do usuário é lida **sem `input()`** (`sys.stdin.readline()`, com
  `sys.stdout.write` + `flush` para o prompt).
- **ex3**: `secure_archive(nome, ação opcional, conteúdo opcional)` lê ou escreve
  usando `with` e retorna `(True, conteúdo)`/`(True, "Content successfully
  written...")` ou `(False, mensagem de erro)`. A estrutura da função é
  conferida na defesa.

### Status

- [ ] ex0  - [ ] ex1  - [ ] ex2  - [ ] ex3

### Perguntas de defesa

- Por que fechar o arquivo? O que pode acontecer se não fechar?
- Diferença entre os modos `"r"`, `"w"` e `"a"`.
- O que são stdin, stdout e stderr? Por que mandar o erro para o stderr?
  (Testar com `python3 ft_stream_management.py foo 2>/dev/null`.)
- Por que o `flush()` é necessário antes de ler do stdin?
- Como o `with` funciona e por que ele é melhor que `open`/`close` na mão? Qual
  a relação com o `try`/`finally`?

---

## Module 05bis — The Codex: Packages, Environments and the Alchemist's Toolchain

Subject: [42x02.python05bis.en.subject.pdf](42x02.python05bis.en.subject.pdf) (v1.0)
Código: `mod05bis/`

### Resumo

**Ambientes virtuais, dependências, configuração por variáveis de ambiente e o
sistema de imports.** Os ex0–ex1 usam bibliotecas externas (pandas, numpy,
python-dotenv). Os ex2–ex4 são o oposto: só podem importar módulos que você
mesmo criou.

Regras extras deste módulo:
- Todos os built-ins são permitidos, **exceto `eval()` e `exec()`**.
- **Proibido mexer em `sys.path`.**
- Nos ex2–ex4, as funções são simples e retornam strings. O foco é o import.
- **Estrutura de pastas fixa, na raiz do repo de entrega** (aqui, a raiz do
  módulo, `mod05bis/`). Os ex0 e ex1 ficam em pastas próprias. Os ex2–ex4
  constroem um único pacote `alchemy/` e scripts na raiz:

```
ex0/  construct.py  loading.py  pyproject.toml  requirements.txt
ex1/  .env.example  .gitignore  oracle.py  requirements.txt
alchemy/  __init__.py  elements.py  potions.py
          transmutation/  __init__.py  recipes.py
          grimoire/  __init__.py  dark_spellbook.py  dark_validator.py
                     light_spellbook.py  light_validator.py
elements.py  ft_alembic_0.py  ft_alembic_1.py  ft_distillation_0.py
ft_transmutation_0.py  ft_kaboom_0.py  ft_kaboom_1.py
```

Não entregar venv nem `.env`. Na defesa podem pedir para criar um venv do zero.

### Exercícios

| Ex | Arquivos | Permitido | Conceito central |
|----|----------|-----------|------------------|
| 0 | `ex0/construct.py`, `loading.py`, `requirements.txt`, `pyproject.toml` | `os`, `sys`, `site`, `importlib`, pandas, numpy | Detectar venv; pip vs Poetry |
| 1 | `ex1/oracle.py`, `requirements.txt`, `.env.example`, `.gitignore` | `os`, `sys`, python-dotenv, arquivos | Configuração e segredos via env vars e `.env` |
| 2 | `elements.py`, `alchemy/__init__.py`, `alchemy/elements.py`, `ft_alembic_0/1.py` | built-ins + módulos próprios | `import x`, pacote, o que o `__init__.py` expõe |
| 3 | `alchemy/potions.py`, `alchemy/transmutation/`, `ft_distillation_0.py`, `ft_transmutation_0.py` | idem | `from x import y`, subpacotes, imports absolutos vs relativos |
| 4 | `alchemy/grimoire/`, `ft_kaboom_0/1.py` | idem | Import circular: uma versão que funciona e outra que quebra |

#### Proposta de cada exercício

- **ex0**: `construct.py` detecta se está num venv (`sys.prefix !=
  sys.base_prefix`), mostra o Python atual e o caminho dos site-packages, e fora
  do venv dá as instruções para criar um. `loading.py` importa pandas e numpy
  com `importlib`/`try`, mostra as versões, e se faltar algum mostra o comando
  de instalação para pip e para Poetry, sem crashar.
- **ex1**: `oracle.py` lê `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL` e
  `ZION_ENDPOINT` do ambiente/`.env` (python-dotenv). Se faltar configuração,
  usa padrões e avisa. Development e production precisam dar outputs visíveis
  diferentes. A variável de ambiente tem prioridade sobre o `.env`. O `.env`
  precisa estar no `ex1/.gitignore`.
- **ex2**: `alchemy/__init__.py` expõe `create_air` e **não** `create_earth`.
  `ft_alembic_1.py` mostra que `alchemy.create_earth()` dá `AttributeError` (o
  erro do mypy é esperado).
- **ex3**: `potions.py` combina elementos de dentro e de fora do pacote.
  `transmutation/recipes.py` precisa de pelo menos um import absoluto e um
  relativo.
- **ex4**: os pares spellbook ↔ validator dependem um do outro. A versão light
  resolve o ciclo (import dentro da função, mover o dado compartilhado para outro
  módulo, injeção por parâmetro...). A versão dark faz o import ingênuo no topo
  dos dois arquivos e **precisa** dar `ImportError` (partially initialized
  module). Não pode ser cópia renomeada do light.

### Status

- [ ] ex0  - [ ] ex1  - [ ] ex2  - [ ] ex3  - [ ] ex4

### Perguntas de defesa (tiradas do subject)

- O que um venv isola e o que ele **não** isola? Por que usar Poetry em vez de um
  `requirements.txt` simples? (`poetry.lock` fixa as versões resolvidas.)
- Por que uma variável de ambiente é melhor que uma constante no código para
  guardar segredo? O que continua inseguro?
- O `create_earth` existe em `alchemy/elements.py`, mas não é acessível via
  `import alchemy`. Nada foi escondido. Então o que o `__init__.py` mudou?
- Quando usar import absoluto e quando usar relativo?
- Os dois grimórios têm arquivos que dependem um do outro. Por que só um
  explode? Quais as alternativas para quebrar um ciclo?

---

## Module 06bis — Code Nexus: Abstract Architecture, from Data Streams to Battle Strategies

Subject: [42x02.python06bis.en.subject.pdf](42x02.python06bis.en.subject.pdf) (v1.0)
Código: `mod06bis/`

### Resumo

**Classes abstratas (ABC), sobrescrita de métodos, polimorfismo e design
patterns** (Protocol/duck typing, abstract factory, capability, strategy).
Primeiro um pipeline de dados (ex0–ex2), depois um "combat sandbox" de criaturas
(ex3–ex4).

Regras extras deste módulo:
- Imports permitidos: só `abc` e `typing`. Bibliotecas externas são proibidas.
- Todos os built-ins são permitidos, exceto `eval()` e `exec()`.
- **Pré-requisito: o mod05bis** (pacotes e `__init__.py`). Os ex3 e ex4 são
  pacotes que importam um ao outro, e o `__init__.py` é obrigatório.
- Estrutura fixa na raiz (aqui, `mod06bis/`):

```
data_processor.py  data_stream.py  data_pipeline.py
ex3/__init__.py (+ arquivos)   battle.py  capacitor.py
ex4/__init__.py (+ arquivos)   tournament.py
```

### Exercícios

| Ex | Arquivos | Conceito central |
|----|----------|------------------|
| 0 | `data_processor.py` | ABC `DataProcessor` com `validate`/`ingest` abstratos e `output` concreto; 3 subclasses |
| 1 | `data_stream.py` | `DataStream` roteia cada elemento para o processor certo (polimorfismo) |
| 2 | `data_pipeline.py` | `ExportPlugin(Protocol)`: plugins CSV/JSON por duck typing |
| 3 | `ex3/`, `battle.py`, `capacitor.py` | Abstract factory + capability (ABC que **não** herda de `Creature`) |
| 4 | `ex4/`, `tournament.py` | Strategy pattern com `isinstance` na capability |

#### Proposta de cada exercício

- **ex0**: `validate(self, data: Any) -> bool` tem a mesma assinatura em todas as
  classes. `ingest` tem assinatura específica em cada subclasse e lança exceção
  com dado inválido (o aviso do mypy é esperado). `output() -> tuple[int, str]`
  retira o item mais antigo (FIFO) junto com o índice dele. Numeric aceita
  int/float/listas, Text aceita str/listas, Log aceita dict[str, str]/listas.
- **ex1**: `register_processor`, `process_stream(list[Any])` (imprime erro quando
  nenhum processor aceita o elemento) e `print_processors_stats`.
- **ex2**: `ExportPlugin(Protocol)` com
  `process_output(self, data: list[tuple[int, str]]) -> None`, e
  `output_pipeline(nb, plugin)` no `DataStream`. CSV e JSON montados à mão (sem
  `import json`/`csv`).
- **ex3**: `Creature(ABC)` (name, type, `attack` abstrato, `describe` concreto),
  `Flameling` e `Pyrodon`, `TransformCapability(ABC)` com
  `transform`/`revert`, `Shiftling` e `Morphagon` herdando dos dois,
  `CreatureFactory(ABC)` com `create_base`/`create_evolved`, e `FlameFactory` e
  `TransformCreatureFactory`. **O pacote `ex3` expõe só as factories.**
- **ex4**: `BattleStrategy(ABC)` com `act`/`is_valid`, `NormalStrategy` (qualquer
  criatura) e `AggressiveStrategy` (só com capability: transform → attack →
  revert). Par inválido → exceção dedicada. O `tournament.py` faz todos contra
  todos e aborta se encontrar um par inválido.

### Status

- [ ] ex0  - [ ] ex1  - [ ] ex2  - [ ] ex3  - [ ] ex4

### Perguntas de defesa (tiradas do subject)

- Como o polimorfismo permite que o `DataStream` trate tipos diferentes sem
  conhecer as implementações? Quais as vantagens?
- ABC vs. Protocol: os dois restringem o que uma classe deve ter. Qual a
  diferença real e por que um sistema de plugins prefere o Protocol? (Herança
  nominal vs. tipagem estrutural.)
- O que quebraria se `transform`/`revert` ficassem na classe base `Creature`?
- O torneio nunca checa a família da criatura, mas cada uma luta de um jeito.
  Para onde foi essa decisão, e o que se ganha quando surge uma capability nova?
- Ao vivo: adicionar um novo tipo de dado, uma nova família ou uma nova
  estratégia.

---

## Module 09 — Cosmic Data: Discover Pydantic Models & Validation

Subject: [42x02.python09.en.subject.pdf](42x02.python09.en.subject.pdf) (v3.0)
Ferramentas: [42x02.python09data_generator.tar](42x02.python09data_generator.tar)
(`data_generator.py`, `data_exporter.py`)
Código: `mod09/exN/`

### Resumo

**Validação de dados com Pydantic 2.x**, com tema espacial: modelos básicos com
`Field` → regras de negócio com `@model_validator` → modelos aninhados.

Regras extras deste módulo:
- Obrigatório usar **venv** e **pip**. Pydantic **2.x** é obrigatório
  (`pip install "pydantic>=2,<3"`).
- Todos os built-ins são permitidos. Da stdlib, `json`, `csv`, `datetime`,
  `enum` etc. também.
- **Não usar `@validator` (Pydantic v1).** Usar `@model_validator(mode="after")`
  e retornar `self`.
- Documentar o raciocínio com comentários claros e nomes significativos (é pedido
  explicitamente neste módulo).
- O `.tar` traz geradores de dados de teste. Extraia em uma pasta separada e leia
  o código antes de rodar.

### Exercícios

| Ex | Arquivo | Conceito central |
|----|---------|------------------|
| 0 | `ex0/space_station.py` | `BaseModel` + `Field` (min/max length, ge/le), datetime, `Optional`, default |
| 1 | `ex1/alien_contact.py` | `Enum` + `@model_validator(mode="after")` com regras de negócio |
| 2 | `ex2/space_crew.py` | Modelos aninhados (`list[CrewMember]`) + validação entre campos |

#### Proposta de cada exercício

- **ex0**: `SpaceStation` com station_id (3–10), name (1–50), crew_size (1–20),
  power_level e oxygen_level (0–100), last_maintenance (datetime),
  is_operational (padrão True) e notes (opcional, ≤200). No `main()`: criar uma
  estação válida, exibir, tentar uma inválida (crew 21) e mostrar a mensagem do
  `ValidationError`.
- **ex1**: `ContactType` (radio/visual/physical/telepathic) e `AlienContact`.
  Regras do validator: ID começa com "AC", contato physical precisa estar
  verificado, telepathic precisa de ≥3 testemunhas e sinal > 7.0 precisa ter
  mensagem.
- **ex2**: `Rank` (cadet…commander), `CrewMember` e `SpaceMission` com crew de 1
  a 12 membros. Regras: ID começa com "M", ≥1 commander ou captain, missão > 365
  dias precisa de 50% da tripulação com 5+ anos de experiência, e todos ativos.

### Status

- [ ] ex0  - [ ] ex1  - [ ] ex2

### Perguntas de defesa (tiradas do subject)

- Como funciona a conversão automática de tipos do Pydantic? O que acontece ao
  passar uma string de data para um campo `datetime`?
- Diferença entre a validação de `Field` e a de `@model_validator`. Por que
  `mode="after"` e por que retornar `self`?
- Como o Pydantic valida modelos aninhados? O que acontece quando um
  `CrewMember` falha dentro de uma `SpaceMission`?
- Pydantic vs. o encapsulamento com getters/setters do mod01 ex4: o que muda?
