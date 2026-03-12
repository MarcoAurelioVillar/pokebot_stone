# Robo Pokemon

Template em Python para automacao de jogos com foco em arquitetura limpa, modularidade e evolucao por plugins.

## Visao Geral

O projeto separa responsabilidades em camadas e permite evoluir bots por jogo sem acoplar regras de negocio com infraestrutura (input, captura de tela, logging, configuracao).

Estado atual:
- `game_a`: implementacao funcional de exemplo
- `game_battle`: placeholder para nova implementacao

## Arquitetura

A aplicacao segue uma arquitetura em camadas:

- `app`: ponto de entrada (CLI)
- `core`: regras centrais reutilizaveis (engine e maquina de estados)
- `infra`: adaptadores tecnicos (config, logger, input, window/capture)
- `games`: plugins por jogo (detectors, actions, bot)

### Diagrama (alto nivel)

```text
+-------------------+
|   app/cli.py      |
|  (comandos CLI)   |
+---------+---------+
          |
          v
+-------------------+
|  games/<plugin>   |
|  build_bot()      |
+---------+---------+
          |
          v
+-------------------+
|   core/BotEngine  |
| detect -> fsm ->  |
| act (loop ticks)  |
+----+----------+---+
     |          |
     v          v
+---------+  +----------------+
|  core   |  |     infra      |
|  FSM    |  | input/logger/  |
| states  |  | config/capture |
+---------+  +----------------+
```

### Fluxo de execucao

1. CLI recebe comando (`robo-game run --game game_a`).
2. Plugin do jogo constroi dependencias (detector, actions, FSM, logger).
3. `BotEngine` executa loop por `ticks`.
4. A cada tick:
   - detector monta `Context`
   - FSM decide `BotState`
   - action executa comportamento do estado

## Estrutura do Projeto

```text
.
|-- assets/
|-- scripts/
|   `-- run_game_a.ps1
|-- src/
|   |-- app/
|   |   `-- cli.py
|   |-- core/
|   |   |-- bot.py
|   |   |-- state_machine.py
|   |   `-- types.py
|   |-- infra/
|   |   |-- config.py
|   |   |-- input_controller.py
|   |   |-- logger.py
|   |   |-- screen_capture.py
|   |   `-- window.py
|   `-- games/
|      |-- game_a/
|      |   |-- actions.py
|      |   |-- bot.py
|      |   |-- config.yaml
|      |   `-- detectors.py
|      `-- game_battle/
|          `-- __init__.py
|-- tests/
|   |-- integration/
|   `-- unit/
|-- pyproject.toml
`-- README.md
```

## Principios Tecnicos

- Separacao clara de responsabilidades por camada
- Acoplamento baixo entre regra de negocio e detalhes tecnicos
- Extensao por plugin de jogo (`games/<nome_do_jogo>`)
- Testes unitarios para regras centrais

## Requisitos

- Python 3.11+
- pip

## Instalacao

```bash
pip install -e .[dev]
```

## Como Executar

Rodar bot de exemplo:

```bash
robo-game run --game game_a --ticks 10
```

Ou via script PowerShell:

```powershell
./scripts/run_game_a.ps1
```

## Testes

```bash
python -m pytest -q
```

## Como criar um novo plugin de jogo

1. Criar pasta `src/games/<novo_jogo>/`
2. Implementar:
   - `detectors.py` (gera `Context`)
   - `actions.py` (executa acoes por estado)
   - `bot.py` (monta dependencias e retorna engine)
   - `config.yaml` (parametros do jogo)
3. Registrar no CLI (`src/app/cli.py`)
4. Adicionar testes unitarios e/ou integracao

## Roadmap

- Reimplementar `game_battle` com nova logica
- Adicionar observabilidade (metricas e eventos por estado)
- Adicionar fixtures/imagens sinteticas para testes de detector
- Pipeline CI (lint + testes)

## Licenca

Defina aqui a licenca do projeto (ex.: MIT).
