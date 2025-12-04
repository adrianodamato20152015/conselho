# 🏛️ Sistema de Gestão de Conselho Consultivo - Firebase Edition

Este é um sistema colaborativo em tempo real para gestão de Conselhos Consultivos, com sincronização via Firebase.

## ✨ Características Principais

### 🔥 Novidades da Versão Firebase

- ✅ **Autenticação Segura**: Login com email/senha via Firebase Authentication
- ✅ **Sincronização em Tempo Real**: Múltiplos usuários editando simultaneamente
- ✅ **Trabalho Offline**: Continue editando sem internet, sincroniza automaticamente ao reconectar
- ✅ **Backup na Nuvem**: Todos os dados salvos no Firebase Firestore
- ✅ **Upload de Imagens**: Avatares e logos armazenados no Firebase Storage
- ✅ **Indicadores de Status**: Visualização do status de conexão (online/offline/sincronizando)
- ✅ **Exportação de Backup**: Baixe seus dados em formato JSON a qualquer momento
- ✅ **Controle de Acesso**: Apenas usuários autenticados podem editar

### 📋 Funcionalidades Herdadas do app62.html

- Gestão completa de Presidência, Grupos, Setores e Cadeiras
- Sistema de Câmaras Temáticas com Atividades e Grupos de Trabalho (GTs)
- Modo Reunião com controle de presença
- Sistema de Documentos organizados em pastas
- Análises e estatísticas
- Paleta de cores personalizável
- Exportação para HTML e JSON

## 🚀 Como Configurar

### Pré-requisitos

- Uma conta Google (gratuita)
- Navegador moderno (Chrome, Firefox, Edge, Safari)
- Conexão com internet (apenas para configuração inicial)

### Passo 1: Criar Projeto no Firebase

1. Acesse: [https://console.firebase.google.com](https://console.firebase.google.com)
2. Clique em **"Adicionar projeto"** ou **"Create a project"**
3. Dê um nome ao projeto (exemplo: "conselho-consultivo-sp")
4. (Opcional) Desative o Google Analytics se não for usar
5. Clique em **"Criar projeto"** e aguarde a criação

### Passo 2: Configurar Firebase Authentication

1. No menu lateral esquerdo, clique em **"Authentication"**
2. Clique em **"Get started"** ou **"Começar"**
3. Na aba **"Sign-in method"**, localize **"Email/Password"**
4. Clique em **"Email/Password"**
5. Ative a primeira opção: **"Email/Password"**
6. Clique em **"Salvar"**

### Passo 3: Criar Firestore Database

1. No menu lateral, clique em **"Firestore Database"**
2. Clique em **"Criar banco de dados"**
3. Escolha **"Iniciar no modo de produção"**
4. Escolha a localização mais próxima:
   - Para Brasil: `southamerica-east1 (São Paulo)`
   - Para Portugal: `europe-west1 (Bélgica)`
5. Clique em **"Ativar"** e aguarde

#### Configurar Regras de Segurança do Firestore

6. Após criar o banco, vá em **"Regras"** (Rules)
7. Substitua o conteúdo por:

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

8. Clique em **"Publicar"** (Publish)

> **Explicação**: Esta regra permite que qualquer usuário autenticado possa ler e escrever dados. Para produção, você pode querer regras mais restritivas.

### Passo 4: Configurar Firebase Storage

1. No menu lateral, clique em **"Storage"**
2. Clique em **"Começar"** ou **"Get started"**
3. Aceite as regras padrão e clique em **"Avançar"**
4. Escolha a **mesma localização** do Firestore
5. Clique em **"Concluído"**

#### Configurar Regras de Segurança do Storage

6. Vá em **"Regras"** (Rules)
7. Substitua o conteúdo por:

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

8. Clique em **"Publicar"** (Publish)

### Passo 5: Obter as Credenciais do Firebase

1. Clique no ícone de **⚙️ (configurações)** ao lado de "Visão geral do projeto"
2. Selecione **"Configurações do projeto"**
3. Role até a seção **"Seus apps"**
4. Clique no ícone da **Web** (`</>`)
5. Dê um apelido ao app (exemplo: "conselho-web")
6. **NÃO** marque a opção "Firebase Hosting"
7. Clique em **"Registrar app"**
8. Você verá um código JavaScript parecido com:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyB1a2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q",
  authDomain: "seu-projeto-12345.firebaseapp.com",
  projectId: "seu-projeto-12345",
  storageBucket: "seu-projeto-12345.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:abc123def456ghi789"
};
```

9. **Copie todo este objeto** (com os valores reais do seu projeto)

### Passo 6: Configurar o Arquivo HTML

1. Abra o arquivo **`firebaseconselho.html`** em um editor de texto
2. Procure pela seção (por volta da linha 2530):

```javascript
const firebaseConfig = {
  apiKey: "SUA_API_KEY_AQUI",
  authDomain: "seu-projeto.firebaseapp.com",
  projectId: "seu-projeto-id",
  storageBucket: "seu-projeto.appspot.com",
  messagingSenderId: "123456789",
  appId: "seu-app-id"
};
```

3. **Substitua** os valores de exemplo pelas credenciais que você copiou no Passo 5
4. Salve o arquivo

### Passo 7: Usar o Sistema

1. Abra o arquivo `firebaseconselho.html` em seu navegador
2. Você verá a tela de login
3. Clique em **"Cadastrar"** para criar sua primeira conta
4. Preencha um email e senha (mínimo 6 caracteres)
5. Clique em **"Criar Conta"**
6. Pronto! Você está dentro do sistema

## 👥 Como Adicionar Mais Usuários

### Método 1: Cadastro Direto (Recomendado)

1. Compartilhe o arquivo `firebaseconselho.html` com outros membros da equipe
2. Certifique-se de que eles configuraram as mesmas credenciais do Firebase
3. Cada pessoa pode criar sua própria conta na tela de cadastro
4. Todos verão os mesmos dados em tempo real

### Método 2: Via Console do Firebase

1. Acesse o [Console do Firebase](https://console.firebase.google.com)
2. Selecione seu projeto
3. Vá em **Authentication** → **Users**
4. Clique em **"Add user"**
5. Digite o email e senha do novo usuário
6. O usuário pode fazer login com essas credenciais

## 📊 Estrutura dos Dados no Firestore

```
/conselhos/
  └── conselho-principal/
      ├── info/
      │   └── geral/
      │       ├── titulo
      │       ├── subtitulo
      │       ├── proximaReuniao
      │       ├── updatedAt
      │       └── updatedBy
      ├── presidencia/
      │   └── membro-{index}/
      │       ├── nome
      │       ├── entidade
      │       ├── municipio
      │       ├── boneco
      │       ├── logo
      │       └── ...
      ├── grupos/
      │   └── {grupo_id}/
      │       ├── titulo
      │       └── setores/
      │           └── setor-{index}/
      │               ├── nome
      │               └── cadeiras/
      │                   └── cadeira-{index}/
      │                       ├── numero
      │                       └── membros[]
      └── camaras/
          └── {camara_slug}/
              ├── nome
              ├── membros[]
              ├── atividades[]
              └── gts[]
```

## 🔧 Funcionalidades Principais

### Modo Edição

1. Clique no menu **☰ MENU**
2. Selecione **🔒 Editar**
3. Digite a senha: `admin123`
4. Faça suas alterações
5. Clique em **💾 Finalizar Edição** para salvar no Firebase

### Sincronização em Tempo Real

- Quando você ou outro usuário salva alterações, todos conectados veem as mudanças instantaneamente
- O indicador no canto inferior direito mostra o status:
  - 🟢 **Online**: Conectado e sincronizado
  - 🟠 **Sincronizando**: Salvando alterações
  - ⚫ **Offline**: Sem conexão (dados salvos localmente)
  - 🔴 **Erro**: Problema na sincronização

### Modo Offline

- Continue trabalhando mesmo sem internet
- As alterações são salvas localmente
- Quando a conexão retornar, tudo sincroniza automaticamente

### Exportar Backup

1. Menu **☰ MENU** → **💾 Exportar Backup JSON**
2. O arquivo será baixado com seus dados completos
3. Recomendamos fazer backups regulares

### Importar Dados

1. Menu **☰ MENU** → **📂 Importar JSON**
2. Selecione um arquivo JSON de backup
3. Confirme se deseja sincronizar com o Firebase

## 🔐 Segurança

### Regras de Segurança Implementadas

- ✅ Apenas usuários autenticados podem acessar o sistema
- ✅ Todos os dados são criptografados em trânsito (HTTPS)
- ✅ Firebase Storage protege as imagens com autenticação
- ✅ Senhas são criptografadas pelo Firebase Authentication

### Recomendações de Segurança

1. **Use senhas fortes** com pelo menos 8 caracteres
2. **Não compartilhe** suas credenciais de login
3. **Faça backups regulares** dos dados
4. **Configure regras mais restritivas** no Firestore para produção
5. **Considere habilitar 2FA** nas contas do Firebase Console

### Regras de Firestore Mais Restritivas (Opcional)

Para limitar o acesso apenas a emails específicos:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /conselhos/{conselhoId}/{document=**} {
      allow read, write: if request.auth != null && 
        request.auth.token.email in [
          'usuario1@example.com',
          'usuario2@example.com',
          'usuario3@example.com'
        ];
    }
  }
}
```

## ❓ Solução de Problemas

### Erro: "Firebase não inicializado"

**Causa**: Credenciais não configuradas corretamente.

**Solução**:
1. Verifique se você substituiu TODAS as credenciais no `firebaseConfig`
2. Certifique-se de não deixar valores como "SUA_API_KEY_AQUI"
3. Recarregue a página após salvar as alterações

### Erro: "Permission denied" ao salvar

**Causa**: Regras de segurança do Firestore muito restritivas.

**Solução**:
1. Vá no Firebase Console → Firestore → Regras
2. Verifique se a regra permite `allow read, write: if request.auth != null;`
3. Publique as regras novamente

### Não consigo fazer login

**Causa**: Email/senha incorretos ou Authentication não configurado.

**Solução**:
1. Tente fazer cadastro novamente
2. Use a função "Esqueci minha senha"
3. Verifique no Firebase Console → Authentication se o Email/Password está ativado

### Dados não sincronizam em tempo real

**Causa**: Persistência offline pode causar conflitos em múltiplas abas.

**Solução**:
1. Use apenas uma aba por vez
2. Recarregue a página
3. Verifique sua conexão com a internet

### Imagens não aparecem

**Causa**: Storage não configurado ou sem permissões.

**Solução**:
1. Verifique se configurou o Firebase Storage
2. Verifique as regras de segurança do Storage
3. Tente fazer upload novamente

## 📱 Compatibilidade

### Navegadores Suportados

- ✅ Google Chrome (recomendado) - versão 90+
- ✅ Mozilla Firefox - versão 88+
- ✅ Microsoft Edge - versão 90+
- ✅ Safari - versão 14+

### Dispositivos

- ✅ Desktop/Laptop (Windows, Mac, Linux)
- ✅ Tablet (iOS, Android)
- ⚠️ Smartphone (funciona, mas recomenda-se desktop para edição)

## 📈 Monitoramento e Uso

### Ver Uso do Firebase

1. Acesse o [Console do Firebase](https://console.firebase.google.com)
2. Selecione seu projeto
3. Vá em **"Uso e faturamento"** para ver:
   - Leituras/escritas do Firestore
   - Armazenamento usado
   - Usuários autenticados
   - Transferência de dados

### Limites do Plano Gratuito

O plano gratuito (Spark) do Firebase inclui:

- ✅ 1 GB de armazenamento no Firestore
- ✅ 50.000 leituras/dia
- ✅ 20.000 escritas/dia
- ✅ 5 GB de armazenamento no Storage
- ✅ 1 GB/dia de transferência no Storage
- ✅ Autenticação ilimitada

> **Nota**: Para um conselho de 20-50 membros com uso moderado, o plano gratuito é mais que suficiente.

## 🆘 Suporte

### Recursos

- 📖 [Documentação do Firebase](https://firebase.google.com/docs)
- 💬 [Comunidade Stack Overflow](https://stackoverflow.com/questions/tagged/firebase)
- 📺 [Firebase YouTube Channel](https://www.youtube.com/c/firebase)

### Contato

Para dúvidas específicas sobre este sistema, abra uma issue no repositório GitHub.

## 📝 Changelog

### Versão 3.0 - Firebase Edition (2024)

- ✨ Adicionada autenticação via Firebase
- ✨ Implementada sincronização em tempo real
- ✨ Adicionado suporte offline
- ✨ Migração de armazenamento local para nuvem
- ✨ Upload de imagens para Firebase Storage
- ✨ Indicadores de status de conexão
- ✨ Sistema de backup em JSON

### Versão 2.2 - app62.html (Base)

- Sistema completo de gestão de conselho
- Modo edição e modo reunião
- Sistema de documentos
- Análises e estatísticas

## 📄 Licença

Este projeto é de código aberto e está disponível para uso livre.

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

**Desenvolvido com ❤️ para Conselhos Consultivos**

🎯 **Objetivo**: Facilitar a gestão colaborativa e transparente de Conselhos Consultivos em todo o Brasil e Portugal.
