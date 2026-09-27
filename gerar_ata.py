from pathlib import Path
from google import genai
from dotenv import load_dotenv  # 1. Importa o leitor do .env
def carregar_prompt_ata():
    arquivo_prompt = Path(__file__).resolve().parent / "prompts" / "prompt_ata.md"
    if not arquivo_prompt.is_file():
        raise FileNotFoundError("O arquivo 'prompt_ata.md' não foi encontrado na raiz do projeto.")
    return arquivo_prompt.read_text(encoding="utf-8")

def gerador_de_ata(arquivo_txt):
# 2. Carrega as variáveis do arquivo .env para a memória do Python
    load_dotenv(Path(__file__).resolve().parent / ".env")

    # inicializa o clint gemini
    # Precisa da chave de api, a minha esta na variavel de ambiente o genai pega sozinho
    client = genai.Client()
    prompt_ata = carregar_prompt_ata()

    
    # acessa o texto do arquivo de texto
    texto_transcrito = arquivo_txt.read_text(encoding="utf-8")

    print("Enviando para o Gemini processar...")
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            prompt_ata,
            f"Arquivo: {arquivo_txt.name}\n\nTranscrição da reunião:\n\n{texto_transcrito}"
        ]
    )
    if not response.text:
        raise RuntimeError(
        "A API do Gemini respondeu, mas não gerou nenhum texto."
        )
    
    pasta_origem = arquivo_txt.parent.parent if arquivo_txt.parent.name.casefold() == "transcricoes" else arquivo_txt.parent
    pasta_ata = pasta_origem / "Atas"
    
        #Cria a pasta no computador se ela ainda não existir
    pasta_ata.mkdir(parents=True, exist_ok=True)
    nome_arquivo = f"{arquivo_txt.stem}_ATA.md"
    caminho_final = pasta_ata / nome_arquivo
    caminho_final.write_text(response.text, encoding="utf-8")

    print(f"[OK] Ata formatada em Scrum salva com sucesso em: {nome_arquivo}")
    return caminho_final


if __name__ == "__main__":
    pasta = Path.home() / "Desktop/Minhas pastas/Proa/Demoday/Audios_dailys"
    arquivo = pasta / "brio_clovis_de_barros_transcricao.txt"
    gerador_de_ata(arquivo)