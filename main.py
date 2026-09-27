import gerar_ata
import transcript
from argumento_caminho import argumentos


    



VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
RESET = "\033[0m"




def main() -> int:
    tipo, alvo = argumentos()
    if tipo == "text":
        try:
            ata_md = gerar_ata.gerador_de_ata(alvo)
        except Exception as e:
            print(f"{VERMELHO}[ERRO] Erro no processamento do Gemini: {e}{RESET}")
            return 1
        print(f"{VERDE}[OK] Ata processada!{RESET}")
        print(f"   Documento final: {ata_md.name}\n")
        return 0

    print(f"{AMARELO}[1/2] Transcrevendo audio com o Whisper...{RESET}")
    try:
        arquivo_txt = transcript.transcrever_ultimo_audio(alvo)
        print(
            f"{VERDE}[OK] [1/2] Transcricao concluida!{RESET}"
        )
    except Exception as e:
        print(f"{VERMELHO}[ERRO] Erro na etapa de transcricao: {e}{RESET}")
        return 1
    print(
            f"{AMARELO}[2/2] Enviando transcricao para o Google Gemini...{RESET}"
        )
    try:
        ata_md = gerar_ata.gerador_de_ata(arquivo_txt)
        print(
            f"{VERDE}[OK] [2/2] Ata processada!{RESET}"
        )
        print(f"   Documento final: {ata_md.name}\n")
    except Exception as e:
        print(f"{VERMELHO}[ERRO] Erro no processamento do Gemini: {e}{RESET}")
        return 1
    return 0
    





if __name__ == "__main__":
    raise SystemExit(main())