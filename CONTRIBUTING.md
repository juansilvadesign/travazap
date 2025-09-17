# 🤝 Contribuindo para o Travazap

Obrigado pelo interesse em contribuir para o projeto Travazap! Este guia vai te ajudar a entender como você pode participar e melhorar o projeto.

## 🎯 Tipos de Contribuições

### 📝 Novos Roteiros
- Filmes clássicos ou populares
- Séries famosas
- Memes e bordões icônicos
- Letras de música
- Diálogos de jogos

### 🔧 Melhorias no Código
- Otimizações de performance
- Correção de bugs
- Novas funcionalidades
- Melhorias na interface
- Tratamento de erros

### 📚 Documentação
- Correções no README
- Exemplos de uso
- Tutoriais
- Tradução para outros idiomas

## 🚀 Como Contribuir

### 1. Fork e Clone
```bash
# Fork o repositório no GitHub
git clone https://github.com/seu-usuario/travazap.git
cd travazap
```

### 2. Crie uma Branch
```bash
# Para novos roteiros
git checkout -b feature/roteiro-nome-do-filme

# Para correções
git checkout -b fix/descricao-do-problema

# Para melhorias
git checkout -b improvement/descricao-da-melhoria
```

### 3. Faça suas Mudanças

#### Para Adicionar um Novo Roteiro:
1. Crie uma nova pasta: `roteiro-nome-do-filme/`
2. Copie o `main.py` de outro roteiro como base
3. Crie o arquivo `.txt` com o conteúdo do roteiro
4. Atualize a referência no `main.py`:
   ```python
   with open('nome-do-arquivo.txt','r') as arquivo:
   ```
5. Teste o script antes de submeter

#### Estrutura Esperada:
```
roteiro-nome-do-filme/
├── main.py
└── roteiro.txt
```

### 4. Teste Localmente
```bash
cd roteiro-nome-do-filme
python main.py
```

### 5. Commit e Push
```bash
git add .
git commit -m "Adiciona roteiro do filme X"
git push origin feature/roteiro-nome-do-filme
```

### 6. Abra um Pull Request
- Vá para o GitHub e abra um Pull Request
- Use um título descritivo
- Explique suas mudanças na descrição
- Mencione se resolve alguma issue existente

## 📋 Diretrizes para Novos Roteiros

### ✅ Critérios de Aceitação
- **Qualidade**: Roteiro deve estar correto e bem formatado
- **Encoding**: Use UTF-8 para caracteres especiais
- **Tamanho**: Considere roteiros que não sejam excessivamente longos
- **Relevância**: Conteúdo deve ser apropriado e conhecido

### ❌ Conteúdo Não Aceito
- Material com direitos autorais muito restritivos
- Conteúdo ofensivo, discriminatório ou inadequado
- Spam ou conteúdo sem valor
- Roteiros com erros graves ou incompletos

## 🔧 Padrões de Código

### Python
```python
# Use imports organizados
import pyautogui as pag
from time import sleep

# Sempre inclua delay inicial
sleep(2)

# Use context managers para arquivos
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo.readlines():
        pag.write(linha.strip())
        pag.press('enter')
```

### Nomes de Arquivos
- Pastas: `roteiro-nome-do-filme` (minúsculas, hífens)
- Scripts: `main.py` (padrão para todos)
- Roteiros: `nome-descritivo.txt` (minúsculas, hífens)

## 🐛 Reportando Bugs

### Antes de Reportar
- Verifique se o bug já foi reportado
- Teste em diferentes sistemas se possível
- Reproduza o erro consistentemente

### Template para Issues
```markdown
**Descrição do Bug**
Descrição clara do que aconteceu.

**Para Reproduzir**
Passos para reproduzir o comportamento:
1. Vá para '...'
2. Execute '...'
3. Veja o erro

**Comportamento Esperado**
O que você esperava que acontecesse.

**Sistema**
- OS: [Windows/macOS/Linux]
- Python: [versão]
- PyAutoGUI: [versão]

**Informações Adicionais**
Qualquer contexto adicional sobre o problema.
```

## 💡 Sugestões de Melhorias

### Ideias Bem-Vindas
- ⚙️ Configurações personalizáveis (velocidade, delay)
- 🎮 Interface gráfica simples
- 📊 Estatísticas de uso
- 🔄 Sistema de interrupção mais intuitivo
- 📁 Organizador de roteiros
- 🌐 Suporte a diferentes idiomas

## 📞 Comunicação

### Onde Discutir
- **Issues**: Para bugs e solicitações de recursos
- **Pull Requests**: Para discussões sobre código
- **Discussions**: Para ideias gerais e perguntas

### Etiqueta
- Seja respeitoso e construtivo
- Use linguagem clara e objetiva
- Ajude outros contribuidores quando possível
- Documente suas mudanças adequadamente

## 🎖️ Reconhecimento

Todos os contribuidores serão:
- Listados nos créditos do projeto
- Mencionados nas release notes
- Reconhecidos publicamente nas redes sociais do projeto

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto.

---

💬 **Dúvidas?** Abra uma issue ou discussion que teremos prazer em ajudar!

🙏 **Obrigado** por ajudar a tornar o Travazap ainda melhor!