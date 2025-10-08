![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 🚀 CodeLeap API - Django REST Framework

Uma API RESTful completa desenvolvida com Django e Django REST Framework para o desafio técnico da CodeLeap.

## 📋 Sobre o Projeto

Esta API permite operações CRUD (Create, Read, Update, Delete) em posts, com endpoints RESTful e validações completas.

### ✨ Funcionalidades

- ✅ **CRUD Completo** de posts
- ✅ **Validações** de dados
- ✅ **Paginação** automática
- ✅ **Tempo relativo** (ex: "5 minutes ago")
- ✅ **Endpoints para modais** (confirmação de delete)
- ✅ **CORS configurado** para frontend
- ✅ **Admin Django** para gerenciamento
- ✅ **Script de testes** para PowerShell

## 🛠️ Tecnologias

- **Python 3.8+**
- **Django 4.2+**
- **Django REST Framework**
- **SQLite** (desenvolvimento)
- **django-cors-headers**

## 🗃️ Estrutura do Projeto

```
codeleap-api/
├── 📁 codeleap/                 # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py             # Configurações do projeto
│   ├── urls.py                 # URLs principais
│   ├── wsgi.py
│   └── asgi.py
├── 📁 posts/                   # App principal da API
│   ├── __init__.py
│   ├── admin.py               # Admin Django
│   ├── apps.py
│   ├── models.py              # Modelos de dados (Post)
│   ├── views.py               # Views e endpoints da API
│   ├── serializers.py         # Serializers DRF
│   ├── urls.py                # URLs da API
│   └── tests.py
├── 📄 manage.py               # Script de gerenciamento Django
├── 📄 api_test.ps1            # Script de teste para PowerShell 🪟
├── 📄 requirements.txt        # Dependências do projeto
├── 📄 README.md               # Documentação principal
└── 📄 .gitignore              # Arquivos ignorados pelo Git
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/CarowlCarvalho/codeleap-api.git
cd codeleap-api
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py migrate
```

5. **Execute o servidor**
```bash
python manage.py runserver
```

A API estará disponível em: `http://127.0.0.1:8000/`

## 📚 Endpoints da API

### Posts
- `GET /api/posts/` - Listar todos os posts
- `POST /api/posts/` - Criar novo post
- `GET /api/posts/{id}/` - Buscar post específico
- `PUT /api/posts/{id}/` - Atualizar post
- `DELETE /api/posts/{id}/` - Excluir post
- `GET /api/posts/{id}/confirm-delete/` - Confirmar exclusão

## 🧪 Testes e Exemplos

### Script de Teste Automatizado

O projeto inclui um script `api_test.ps1` para testar rapidamente todos os endpoints:

```powershell
# Executar testes completos
.\api_test.ps1

# O script testará:
# ✅ Criação de posts
# ✅ Listagem de posts  
# ✅ Confirmação de exclusão
# ✅ Exclusão de posts
# ✅ Verificação final
```

### Testes com PowerShell

**Criar Post:**
```powershell
$body = @{
    username = "usuario"
    title = "Título do Post"
    content = "Conteúdo do post aqui"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/posts/" -Method Post -Body $body -ContentType "application/json"
```

**Listar Posts:**
```powershell
$posts = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/posts/" -Method Get
```

**Confirmar Exclusão:**
```powershell
$confirm = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/posts/1/confirm-delete/" -Method Get
```

**Excluir Post:**
```powershell
$delete = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/posts/1/" -Method Delete
```

### Testes com cURL

**Criar Post:**
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "joao",
    "title": "Meu Post",
    "content": "Conteúdo do post"
  }'
```

**Listar Posts:**
```bash
curl http://127.0.0.1:8000/api/posts/
```

## 🔧 Desenvolvimento

### Criando superusuário
```bash
python manage.py createsuperuser
```

### Acessando o admin
`http://127.0.0.1:8000/admin/`

### Executando migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### Executando testes
```bash
python manage.py test
```

## 🎯 Exemplo de Resposta da API

**Criação de Post:**
```json
{
  "id": 1,
  "username": "joao",
  "title": "Meu primeiro post",
  "content": "Conteúdo do meu post",
  "created_datetime": "2024-01-15T10:30:00Z",
  "updated_datetime": "2024-01-15T10:30:00Z",
  "time_ago": "just now"
}
```

**Listagem de Posts:**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "joao",
      "title": "Meu primeiro post",
      "content": "Conteúdo do meu post",
      "created_datetime": "2024-01-15T10:30:00Z",
      "updated_datetime": "2024-01-15T10:30:00Z",
      "time_ago": "5 minutes ago"
    }
  ]
}
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

---

**Desenvolvido para o desafio técnico CodeLeap ✨** 

