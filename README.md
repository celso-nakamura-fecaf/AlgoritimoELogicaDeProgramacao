# REGISTRO E GERENCIAMENTO DE PEÇAS


## Descrição

Sistema em Python que simula um controle de produção de peças, incluindo validação de atributos, organização em caixas, armazenamento persistente e geração de relatórios.

O projeto foi desenvolvido com foco em organização de código, separação de responsabilidades e simulação de um ambiente industrial simplificado.

---

## Funcionalidades

- Cadastro manual de peças
- Produção em massa com dados simulados
- Validação automática (peso, cor e tamanho)
- Separação entre peças válidas e inválidas
- Organização em caixas com limite de capacidade
- Listagem de peças e caixas
- Exclusão de peças
- Geração de relatório com estatísticas

---

## Estrutura do Projeto

- models/ → entidades do sistema (Item, Box)
- services/ → regras de negócio (ItemService, BoxService, ReportService)
- db/ → persistência de dados
- main.py → menu principal

---

## Como executar

### Pré-requisitos
- Python 3.x instalado

### Passos

1. Clone o repositório:

git clone https://github.com/celso-nakamura-fecaf/AlgoritimoELogicaDeProgramacao.git

2. Acesse a pasta do projeto:

cd AlgoritimoELogicaDeProgramacao

3. Execute o programa:

python3 main.py

Caso o comando acima não funcione, tente:

python main.py

---

## Persistência de dados

O sistema utiliza arquivos JSON:

- db.json → armazenamento geral do sistema
- id_state.json → controle sequencial de IDs

---

## Exemplo de uso

### Cadastro de peça válida

Entrada:
Peso: 100  
Cor: azul  
Tamanho: 10  

Resultado:
Peça validada e armazenada como válida

---

### Cadastro de peça inválida

Entrada:
Peso: 70  
Cor: vermelho  
Tamanho: 8  

Saída:
Peça inválida  
Motivos:
- Peso fora do padrão  
- Cor inválida  
- Tamanho incorreto  

---

### Produção em massa

Entrada:
Quantidade: 5  

Resultado:
Geração automática de peças com validação aplicada

---

## Relatório

O sistema gera um relatório contendo:

- Total de peças válidas
- Total de peças inválidas
- Quantidade de caixas fechadas
- Motivos de invalidação

- Saída:

=== RELATÓRIO ===  
Caixas completas: 1  
Peças boas: 10  
Peças reprovadas: 5  

Motivos de reprovação:
- Peso fora do padrão: 2  
- Cor inválida: 2  
- Tamanho incorreto: 1  
=================

---

## Observações

- IDs são gerados automaticamente de forma sequencial
- O sistema evita inconsistência na numeração
- Arquitetura baseada em separação por serviços
- Interface via terminal (CLI)
