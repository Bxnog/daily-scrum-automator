from pathlib import Path
from google import genai
from dotenv import load_dotenv  # 1. Importa o leitor do .env
def gerador_de_ata(arquivo_txt):
# 2. Carrega as variáveis do arquivo .env para a memória do Python
    load_dotenv()

    # inicializa o clint gemini
    # Precisa da chave de api, a minha esta na variavel de ambiente o genai pega sozinho
    client = genai.Client()
    prompt_sistema = """
    Você é um Scrum Master e Engenheiro de Software sênior. 
    Sua tarefa é analisar a transcrição bruta de uma reunião Daily e gerar um resumo executivo formatado estritamente em Markdown.

    Regras Obrigatórias:
    0. Crie um título principal no Markdown com a data da reunião informada no contexto.
    1. Extraia o que foi dito e organize por cada participante mencionado.
    2. Para cada participante, crie as seções:
    - **O que fez ontem/recentemente**
    - **O que fará hoje/próximos passos**
    - **Bloqueios/Impedimentos** (se não houver nenhum mencionado, escreva "Nenhum bloqueio informado").
    3. Mantenha um tom profissional e direto.
    4. NUNCA invente fatos ou informações que não foram ditas no texto.
    5. Corrija pequenos erros de digitação ou termos de tecnologia que foram mal transcritos pelo áudio.
    6. Não inclua conversa paralelas ao resumo. Caso não esteja em duvida um trecho é paralelo
    coloque no resumo, mas indicado como possivelmente sendo paralelo
    """

    
    # acessa o texto do arquivo de texto
    texto_transcrito = arquivo_txt.read_text(encoding="utf-8")

    print("Enviando para o Gemini processar...")
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            prompt_sistema,
            f"Arquivo: {arquivo_txt.name}\n\nTranscrição da reunião:\n\n{texto_transcrito}"
        ]
    )
    if not response.text:
        raise RuntimeError(
        "A API do Gemini respondeu, mas não gerou nenhum texto."
        )
    
    pasta_ata = arquivo_txt.parent.parent / "Atas"
    
        #Cria a pasta no computador se ela ainda não existir
    pasta_ata.mkdir(exist_ok=True)
    nome_arquivo = f"{arquivo_txt.stem}_ATA.md"
    caminho_final = pasta_ata / nome_arquivo
    caminho_final.write_text(response.text, encoding="utf-8")

    print(f"✅ Ata formatada em Scrum salva com sucesso em: {nome_arquivo}")
    return caminho_final
