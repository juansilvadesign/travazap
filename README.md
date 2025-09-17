# 🎬 Travazap - Gerador Automático de Scripts

Um compilado de "travazaps" automatizados que digitam scripts famosos de filmes e séries automaticamente no seu chat ou aplicativo favorito usando PyAutoGUI.

## 📂 Scripts Disponíveis

### 🟢 Shrek (2001)
- **Pasta:** `roteiro-shrek/`
- **Arquivo:** `main.py`
- **Conteúdo:** Roteiro completo do filme Shrek em português
- **Linhas:** 3.739 linhas de diálogo

## 🚀 Como Usar

### Pré-requisitos
```bash
pip install pyautogui
```

### Execução
1. Abra o chat ou aplicativo onde deseja enviar o texto
2. Navegue até a pasta do script desejado:
   ```bash
   cd roteiro-shrek
   ```
3. Execute o script:
   ```bash
   python main.py
   ```
4. **Importante:** Você tem 2 segundos para clicar no campo de texto do chat antes do script começar a digitar!

## ⚙️ Como Funciona

O script utiliza a biblioteca PyAutoGUI para:
1. Aguardar 2 segundos (`sleep(2)`) para você posicionar o cursor
2. Ler linha por linha do arquivo de texto (.txt)
3. Digitar cada linha automaticamente
4. Pressionar Enter após cada linha

```python
import pyautogui as pag
from time import sleep
sleep(2)
with open('shrek.txt','r') as shrek:
    for i in shrek.readlines():
        pag.write(i)
        pag.press('enter')
```

## ⚠️ Avisos Importantes

- **Use com responsabilidade**: Este projeto é apenas para fins educacionais e de entretenimento
- **Spam**: Evite usar em grupos ou conversas onde possa incomodar outras pessoas
- **Interrupção**: Para parar o script durante a execução, mova o mouse para o canto superior esquerdo da tela
- **Velocidade**: O script digita automaticamente, então certifique-se de estar no local correto antes de executar

## 🎯 Casos de Uso

- **Diversão com amigos**: Surpreender amigos em conversas privadas
- **Memes**: Criar situações engraçadas em contextos apropriados  
- **Automação**: Base para outros projetos de automação de texto
- **Estudo**: Exemplo prático de uso do PyAutoGUI

## 🔧 Personalização

Para adicionar novos scripts:

1. Crie uma nova pasta com o nome do filme/série
2. Adicione o arquivo `main.py` (pode copiar de `roteiro-shrek/`)
3. Crie um arquivo `.txt` com o roteiro desejado
4. Atualize a referência do arquivo no `main.py`:
   ```python
   with open('seu_roteiro.txt','r') as arquivo:
   ```

## 📋 Próximos Scripts Planejados

- 🎭 Mais filmes clássicos
- 📺 Séries famosas  
- 🎪 Memes e bordões
- 🎵 Letras de música

## 🤝 Contribuições

Contribuições são muito bem-vindas! Veja o [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como contribuir com novos roteiros, melhorias no código ou correções.

## 📄 Licença

Este projeto é apenas para fins educacionais e de entretenimento. Os roteiros utilizados são propriedade de seus respectivos detentores de direitos autorais.

## 🐛 Problemas Conhecidos

- Em alguns sistemas, pode ser necessário ajustar o tempo de delay
- Caracteres especiais podem não ser digitados corretamente em alguns teclados
- A velocidade de digitação pode variar dependendo do sistema

## 🛠️ Requisitos Técnicos

- **Python 3.6+**
- **PyAutoGUI 0.9.52+**
- **Sistema Operacional:** Windows, macOS, Linux
- **Permissões:** Acesso para controlar mouse e teclado

---

⭐ **Dica:** Se você gostou do projeto, deixe uma estrela no repositório!

📧 **Contato:** Para sugestões ou problemas, abra uma issue no GitHub.