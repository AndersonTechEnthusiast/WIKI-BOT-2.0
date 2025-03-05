# WIKI-BOT 2.0

## 📚 Sobre o Projeto

O **WIKI-BOT 2.0** é um assistente interativo que permite ao usuário consultar informações diretamente da Wikipedia. O bot oferece duas opções de armazenamento de dados:

- **Memória Volátil**: As requisições são feitas a cada consulta, sem salvar dados localmente.
- **Memória Fixa**: As informações são armazenadas em um arquivo local para consultas futuras sem necessidade de novas requisições.

## ✨ Funcionalidades

- 🔎 Busca automática na Wikipedia
- 📂 Armazena histórico de perguntas e respostas
- 📁 Opção de armazenamento temporário ou permanente
- 🌐 Interface colorida e interativa

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Bibliotecas:**
  - `wikipediaapi`
  - `bs4 (BeautifulSoup)`
  - `requests`
  - `tqdm`
  - `pyfiglet`
  - `datetime`
  - `colorama`
  - `unidecode`
  - `os`
  - `time`

## 🔄 Como Executar o Projeto

### 1. Instale as Dependências

```bash
pip install wikipedia-api beautifulsoup4 requests tqdm pyfiglet colorama unidecode
```

### 2. Execute o Script

```bash
python wiki_bot.py
```

### 3. Escolha o Tipo de Memória

Quando o bot iniciar, ele perguntará qual tipo de memória deseja usar:

- Pressione **V** para **Memória Volátil**
- Pressione **F** para **Memória Fixa**

### 4. Faça suas Perguntas

Digite sua pergunta e aguarde a resposta extraída da Wikipedia.

## 🛢️ Estrutura de Arquivos

```
Wiki-Bot/
│-- ChatBox/                  # Pasta de armazenamento local
│   ├── Parametros.txt        # URLs ou palavras-chave para consulta
│   ├── ChatBox.txt           # Arquivo de cache das consultas
│-- Historico.txt             # Registra perguntas e respostas
│-- wiki_bot.py               # Script principal
│-- README.md                 # Documentação do projeto
```

## ⚠ Possíveis Erros e Soluções

| Erro                                                            | Solução                                                              |
| --------------------------------------------------------------- | -------------------------------------------------------------------- |
| **ModuleNotFoundError**: Alguma biblioteca está faltando        | Execute `pip install -r requirements.txt` para instalar dependências |
| **UnicodeEncodeError**: Problema ao exibir caracteres especiais | Tente rodar `chcp 65001` no terminal antes de executar o script      |
| **Requisição falhou**: Wikipedia não responde                   | Verifique sua conexão com a internet                                 |

## 💪 Contribuição

Fique à vontade para sugerir melhorias e abrir pull requests!

## ✨ Autor

- **Desenvolvedor**: [Seu Nome](https://github.com/seu-github)

---

📊 **WIKI-BOT 2.0** - Um assistente poderoso para buscas na Wikipedia! 🌟

