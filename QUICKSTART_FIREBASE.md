# 🚀 Guia Rápido - Firebase Conselho

## ⚡ Configuração em 5 Minutos

### 1️⃣ Criar Projeto Firebase (2 min)

1. Acesse: https://console.firebase.google.com
2. Clique em **"+ Adicionar projeto"**
3. Nome: `meu-conselho`
4. Desmarque Analytics (opcional)
5. Clique em **"Criar"**

### 2️⃣ Ativar Serviços (2 min)

#### Authentication
1. Menu lateral → **Authentication** → **"Começar"**
2. **"Email/Password"** → Ativar primeira opção → **"Salvar"**

#### Firestore
1. Menu lateral → **Firestore Database** → **"Criar banco"**
2. **"Modo de produção"** → Localização: `southamerica-east1` → **"Ativar"**
3. **"Regras"** → Cole:
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```
4. **"Publicar"**

#### Storage
1. Menu lateral → **Storage** → **"Começar"**
2. **"Avançar"** → Mesma localização → **"Concluído"**
3. **"Regras"** → Cole:
```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```
4. **"Publicar"**

### 3️⃣ Copiar Credenciais (1 min)

1. **⚙️ Configurações** (ícone ao lado de "Visão geral")
2. Role até **"Seus apps"**
3. Clique no ícone **Web** (`</>`)
4. Apelido: `conselho-web`
5. **"Registrar app"**
6. Copie o objeto `firebaseConfig` completo

### 4️⃣ Configurar HTML (30 seg)

1. Abra `firebaseconselho.html` no editor
2. Procure por `const firebaseConfig = {` (linha ~2530)
3. Cole suas credenciais
4. Salve o arquivo

### 5️⃣ Usar! (30 seg)

1. Abra `firebaseconselho.html` no navegador
2. Clique em **"Cadastrar"**
3. Digite email e senha
4. **"Criar Conta"**
5. ✅ Pronto!

## 🎯 Próximos Passos

### Adicionar Dados

1. **☰ MENU** → **🔒 Editar**
2. Senha: `admin123`
3. Preencha informações
4. **💾 Finalizar Edição**

### Convidar Usuários

Compartilhe o arquivo `firebaseconselho.html` com mesmo `firebaseConfig`.
Cada pessoa cria sua conta e vê os mesmos dados em tempo real!

### Fazer Backup

**☰ MENU** → **💾 Exportar Backup JSON**

## 🆘 Problemas Comuns

**Erro ao inicializar Firebase**
- Verifique se copiou TODAS as credenciais corretamente

**Não consigo salvar dados**
- Confirme se publicou as regras do Firestore e Storage

**Tela de login não some**
- Abra Console do Browser (F12) → veja erros
- Verifique se Authentication está ativado

## 📞 Ajuda Completa

Veja **FIREBASE_README.md** para:
- Documentação detalhada
- Solução de problemas
- Configurações avançadas
- Segurança

---

**Tempo total de setup: ~5 minutos** ⚡

Depois disso, você terá um sistema colaborativo em tempo real funcionando!
