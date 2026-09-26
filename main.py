import transcript
import gerar_ata
from pathlib import Path
caminho_da_sua_pasta = "Desktop/Minhas pastas/Proa/Demoday/Audios_dailys"
PASTA_DAILYS = Path.home() / caminho_da_sua_pasta
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
RESET = "\033[0m"
def main():
    print(f"{AMARELO}⏳ [1/2] Transcrevendo áudio com o Whisper...{RESET}")
    try:
        arquivo_txt = transcript.transcrever_ultimo_audio(PASTA_DAILYS)
        print(
            f"{VERDE}✅ [1/2] Transcrição concluída!{RESET}"
        )
    except Exception as e:
        print(f"{VERMELHO}❌ Erro na etapa de transcrição: {e}{RESET}")
        return
    print(
            f"{AMARELO}⏳ [2/2] Enviando transcrição para o Google Gemini...{RESET}"
        )
    try:
        ata_md = gerar_ata.gerador_de_ata(arquivo_txt)
        print(
            f"{VERDE}✅ [2/2] Ata processada!{RESET}"
        )
        print(f"   📝 Documento final: {ata_md.name}\n")
    except Exception as e:
        print(f"{VERMELHO}❌ Erro no processamento do Gemini: {e}{RESET}")
        return
    
if __name__ == "__main__":
    main()