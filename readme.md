# 🎙️ Daily Scrum Automator

Uma ferramenta em Python para automação de atas de reuniões. O script captura áudios gravados, realiza transcrição local (*Speech-to-Text*) com **Faster-Whisper** e gera relatórios executivos formatados em Markdown utilizando a API do **Google Gemini (LLM)**.

---

## Funcionalidades

* **Seleção e Memória de Pasta (`-f`):** Permite escolher a pasta de áudios através de uma janela visual (Tkinter) e salva a preferência para as próximas execuções.

* **Suporte a Áudio Direto (`-a`):** Processa um arquivo de áudio específico informado diretamente no terminal.

* **Suporte a Texto Direto (`-t`):** Gera a ata diretamente a partir de um arquivo de texto já transcrito, pulando a etapa do Whisper.

* **Transcrição Local com Contexto:** Processamento via `faster-whisper` com suporte a vocabulário técnico e mapeamento dos nomes da equipe.

* **Quadro de Tarefas para Kanban/Trello:** Identifica tarefas e atribui responsáveis (individuais, duplas ou para toda a equipe) em formato de checklist ao final do relatório.

* **Relatório Flexível:** Formatação atemporal baseada em ciclos de encontros ("desde a última reunião"), perfeita para reuniões diárias, semanais ou esporádicas.

* **Prompts Personalizáveis:** O arquivo `prompt_ata.md` pode ser editado para adaptar a geração da ata a necessidades específicas, como diferentes formatos, informações ou regras para o relatório.

* **Contexto Personalizável para Transcrição:** O arquivo `prompt_contexto.txt` pode ser alterado para fornecer contexto adicional ao processo de transcrição, como nomes, termos técnicos e vocabulário específico do projeto, ajudando a melhorar a precisão do áudio transcrito.


---

## Pré-requisitos

* Python 3.10 ou superior instalado.
* Chave de API do Google Gemini.

---

## Como preparar o ambiente e rodar

Se você acabou de baixar este repositório, siga os passos abaixo para rodar o projeto no seu computador.

### 1. Criar o Ambiente Virtual (opcional, mas recomendado)

O ambiente virtual garante que as bibliotecas deste projeto não misturem com outros projetos do seu computador.

No terminal, dentro da pasta do projeto, rode:

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

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / Mac:**

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

1. Crie um arquivo chamado `.env` na raiz do projeto, no mesmo nível do `main.py`.
2. Adicione sua chave de API do Google Gemini:

```env
GEMINI_API_KEY=sua_chave_aqui_sem_aspas
```

---

### 5. Como Executar

Você pode executar o programa de **4 formas diferentes** pelo terminal.

#### Execução Padrão

Usa o áudio mais recente da pasta configurada:

```bash
python main.py
```

#### Escolher ou Alterar a Pasta Padrão de Áudios

Abre uma janela visual para selecionar a pasta e salva a escolha para as próximas execuções:

```bash
python main.py -f
```

#### Processar um Arquivo de Áudio Específico

Processa diretamente o arquivo de áudio informado no terminal:

```bash
python main.py -a "C:\Caminho\Para\seu_audio.mp3"
```

#### Gerar a Ata a partir de uma Transcrição

Utiliza um arquivo de texto já transcrito, pulando a etapa do Whisper:

```bash
python main.py -t "C:\Caminho\Para\sua_transcricao.txt"
```
