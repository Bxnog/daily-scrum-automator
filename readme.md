# 🎙️ Daily Scrum Automator

Uma ferramenta em Python para automação de atas de reuniões *Daily Scrum*. O script captura áudios gravados, realiza transcrição local (*Speech-to-Text*) com **Faster-Whisper** e gera relatórios executivos formatados em Markdown utilizando a API do **Google Gemini (LLM)**.

---

## Funcionalidades

- **Mapeamento Automático:** Identifica dinamicamente o áudio mais recente salvo na pasta de entrada.
- **Transcrição Offline/Local:** Processamento de áudio via `faster-whisper` sem dependência de serviços pagos de transcrição.
- **Estruturação Scrum:** O Gemini atua como um Scrum Master sênior, organizando o texto em:
  - O que foi feito ontem
  - O que será feito hoje
  - Bloqueios/Impedimentos

---

## Pré-requisitos

- Python 3.10 ou superior instalado.
- Chave de API do Google Gemini.

---

## Como preparar o ambiente e rodar

Se você acabou de baixar este repositório, siga os passos abaixo para rodar o projeto no seu computador:

### 1. Criar o Ambiente Virtual (opcional, mas recomendado)
O ambiente virtual garante que as bibliotecas deste projeto não misturem com outros projetos do seu computador. No terminal, dentro da pasta do projeto, rode:

**No Windows:**
```bash
python -m venv venv
```

**No Linux/Mac:**
```bash
python3 -m venv venv
```

---

### 2. Ativar o Ambiente Virtual

- **Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Linux / Mac:**
  ```bash
  source venv/bin/activate
  ```

---

### 3. Instalar as Dependências

Com o ambiente virtual ativado, rode:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar a Chave da API (Gemini)

1. Crie um arquivo chamado `.env` na raiz do projeto (no mesmo nível do `main.py`).
2. Adicione sua chave de API do Google Gemini assim:

```env
GEMINI_API_KEY=sua_chave_aqui_sem_aspas
```

---

### 5. Executar

1. Abra o arquivo `main.py` e defina a variável `caminho_da_sua_pasta` apontando para o diretório dos seus áudios a partir da pasta do seu usuário (Home) (exemplo: `"Desktop/Audios"`).
2. Coloque um áudio por vez na pasta especificada e rode:

```bash
python main.py
```