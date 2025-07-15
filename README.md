
# CRUD de Personagens do Universo Sonic 🌀🦔

Este projeto é um CRUD (Create, Read, Update, Delete) feito em **Python + SQLite**, inspirado no universo de personagens do Sonic. A aplicação funciona inteiramente via terminal, com foco em aprendizagem de banco de dados, manipulação de arquivos SQL e organização de código com funções reutilizáveis.

> 💡 O projeto foi desenvolvido como um exercício prático para explorar **conceitos de banco de dados com SQLite**, **integração com Python**, **validações de entrada**, **menu interativo** e **estrutura modular**.

---

## 🎮 Funcionalidades

- [x] Adicionar novo personagem ao banco de dados
- [x] Listar todos os personagens cadastrados (sem exibir o ID)
- [x] Atualizar dados com visualização dos valores antigos
- [x] Remover personagem com confirmação de exclusão
- [x] Buscar personagem por campo (nome, tipo, time, cor ou poderes)
- [x] Importar **dados sugeridos** com opção de **adicionar** ou **substituir** a tabela
- [x] Exportar os personagens para arquivo `.csv` com **acentuação preservada**
- [x] `.csv` é ignorado no GitHub via `.gitignore` (mantendo o repositório limpo)
- [x] Validação de entrada para evitar erros (ex: letras em campos numéricos)
- [x] Layout organizado, mensagens de retorno claras e UX amigável via terminal

---

## 📋 Estrutura de dados do personagem

Cada personagem possui os seguintes campos:

| Campo    | Descrição                                        |
|----------|--------------------------------------------------|
| `nome`   | Nome do personagem (ex: Sonic, Tails, Knuckles) |
| `tipo`   | Speed, Power ou Fly                              |
| `time`   | Time de origem (Sonic, Dark, Babylon Rogues...)  |
| `cor`    | Cor predominante (Azul, Amarelo, Roxo...)         |
| `poderes`| Habilidades especiais ou marcantes               |

---

## 🧠 Tecnologias utilizadas

- **Python 3**
- **SQLite3** (banco de dados embutido, simples e funcional)
- **VSCode** com extensão SQLite Viewer (opcional para ver o banco `.db` graficamente)

---

## 🗃️ Organização do projeto

| Arquivo                | Descrição                                                                 |
|------------------------|---------------------------------------------------------------------------|
| `main.py`              | Interface principal com o menu e lógica de entrada do usuário             |
| `database.py`          | Todas as operações do banco de dados (CRUD, busca, exportação, etc.)      |
| `dados_iniciais.sql`   | Tabela com personagens icônicos para importar de forma prática            |
| `.gitignore`           | Impede versionamento de arquivos como `.db`, `.csv` e `__pycache__`       |

---

## 💾 Como executar

1. Clone este repositório:
```bash
git clone https://github.com/leomacedo/python-banco-de-dados.git
cd crud_personagens_sonic
```

2. Execute o script principal:
```bash
python main.py
```

3. Escolha as opções do menu para interagir com o banco de dados!

---

## 📝 Exemplo de uso do menu

```bash
--- Banco de Dados do Universo Sonic 🌀 ---
1. Adicionar personagem
2. Listar todos
3. Atualizar personagem
4. Remover personagem
5. Buscar personagem por campo
6. Sair
7. Importar dados iniciais sugeridos
8. Exportar backup da tabela para CSV
```

> 🗒️ Observação: O arquivo `.csv` gerado pelo menu (opção 8) **não é salvo no GitHub**, pois está incluído no `.gitignore`. Isso evita poluir o repositório com backups locais.

---

## 🤝 Créditos

Projeto criado por [@leomacedo](https://github.com/leomacedo)
