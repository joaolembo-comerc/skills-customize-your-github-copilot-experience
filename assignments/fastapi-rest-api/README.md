# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a criar uma API REST funcional usando o framework FastAPI do Python. Você construirá endpoints para gerenciar uma lista de tarefas (to-do list), aplicando os conceitos fundamentais de APIs REST incluindo métodos HTTP, validação de dados e documentação automática.

## 📝 Tasks

### 🛠️	Criar Estrutura Básica da API

#### Description
Configure um projeto FastAPI básico e crie seu primeiro endpoint. Instale o FastAPI e o Uvicorn (servidor ASGI), e crie uma API simples com um endpoint de boas-vindas.

#### Requirements
Completed program should:

- Ter o FastAPI e Uvicorn instalados via pip
- Incluir um endpoint GET na rota raiz (/) que retorna uma mensagem de boas-vindas
- Executar com sucesso usando `uvicorn main:app --reload`
- Ser acessível em http://localhost:8000


### 🛠️	Implementar CRUD para Tarefas

#### Description
Crie endpoints REST completos para gerenciar uma lista de tarefas. Implemente as operações Create, Read, Update e Delete (CRUD) usando os métodos HTTP apropriados (GET, POST, PUT, DELETE).

#### Requirements
Completed program should:

- GET /tasks - Listar todas as tarefas
- GET /tasks/{id} - Buscar uma tarefa específica por ID
- POST /tasks - Criar uma nova tarefa com título e descrição
- PUT /tasks/{id} - Atualizar uma tarefa existente
- DELETE /tasks/{id} - Remover uma tarefa
- Usar modelos Pydantic para validação de dados
- Retornar códigos de status HTTP apropriados (200, 201, 404, etc.)


### 🛠️	Adicionar Validações e Documentação

#### Description
Aprimore sua API com validações de dados robustas usando Pydantic e explore a documentação interativa automática gerada pelo FastAPI.

#### Requirements
Completed program should:

- Validar que o título da tarefa tenha entre 3 e 100 caracteres
- Validar que a descrição não exceda 500 caracteres
- Incluir um campo booleano 'completed' com valor padrão False
- Retornar mensagens de erro claras para dados inválidos
- Ter documentação interativa acessível em /docs (Swagger UI)
- Incluir descrições úteis nos endpoints usando docstrings


