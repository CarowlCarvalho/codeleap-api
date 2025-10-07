# Script teste API CodeLeap - CORRIGIDO encoding
Write-Host " Testando API CodeLeap (PowerShell)" -ForegroundColor Green

# URL base
$baseUrl = "http://127.0.0.1:8000/api"

# 1. CRIAR POST (sem acentos para garantir)
Write-Host "`n1. Criando post..." -ForegroundColor Yellow
$postData = @{
    username = "Carol"
    title = "Post de teste PowerShell"
    content = "Conteudo do post"
}

try {
    $jsonBody = $postData | ConvertTo-Json
    $response = Invoke-RestMethod -Uri "$baseUrl/posts/" -Method Post -Body $jsonBody -ContentType "application/json"
    $postId = $response.id
    Write-Host " POST CRIADO! ID: $postId" -ForegroundColor Green
    Write-Host "   Titulo: $($response.title)" -ForegroundColor Cyan
    Write-Host "   Autor: $($response.username)" -ForegroundColor Cyan
}
catch {
    Write-Host " Erro: $($_.Exception.Message)" -ForegroundColor Red
}

# 2. LISTAR POSTS
Write-Host "`n2. Listando posts..." -ForegroundColor Yellow
try {
    $posts = Invoke-RestMethod -Uri "$baseUrl/posts/" -Method Get
    Write-Host " Total de posts: $($posts.count)" -ForegroundColor Green
    if ($posts.count -gt 0) {
        foreach ($post in $posts.results) {
            Write-Host "   - ID $($post.id): $($post.title)" -ForegroundColor White
        }
    }
}
catch {
    Write-Host " Erro: $($_.Exception.Message)" -ForegroundColor Red
}

# 3. EXCLUIR POST (se criou um)
if ($postId) {
    Write-Host "`n3. Excluindo post ID: $postId..." -ForegroundColor Yellow
    try {
        $delete = Invoke-RestMethod -Uri "$baseUrl/posts/$postId/" -Method Delete
        Write-Host " $($delete.message)" -ForegroundColor Green
    }
    catch {
        Write-Host " Erro: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host "`n Teste completo!" -ForegroundColor Green
