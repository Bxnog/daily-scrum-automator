from faster_whisper import WhisperModel
from pathlib import Path

def carregar_contexto():
    arquivo_prompt = Path(__file__).resolve().parent / "prompts" / "prompt_contexto.txt"
    if arquivo_prompt.is_file():
        return arquivo_prompt.read_text(encoding="utf-8").strip()
    return "Reunião de alinhamento da equipe de software."

def transcrever_ultimo_audio(pasta_input: Path) -> Path:
    EXTENSOES_VALIDAS = {".mp3", ".opus", ".aac", ".wav", ".flac"}
    # Accept a selected audio file or choose the newest audio from a folder.
    if pasta_input.is_file():
        if pasta_input.suffix.lower() not in EXTENSOES_VALIDAS:
            raise ValueError(f"Formato de áudio inválido: {pasta_input}")
        audio_mais_recente = pasta_input
        pasta_saida = pasta_input.parent
    elif pasta_input.is_dir():
        audios = [
            p
            for p in pasta_input.iterdir()
            if p.is_file() and p.suffix.lower() in EXTENSOES_VALIDAS
        ]
        if audios:
            audio_mais_recente = max(audios, key=lambda f: f.stat().st_mtime)
        else:
            raise FileNotFoundError(f"Não há arquivos de áudio em: {pasta_input}")
        pasta_saida = pasta_input
    else:
        raise FileNotFoundError(f"Arquivo ou pasta não encontrado: {pasta_input}")

    # escolhe o modelo
    model_size = "small"

    # Run on CPU with int8
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    # model = WhisperModel(model_size, device="cpu", compute_type="int8")

    prompt_contexto = carregar_contexto()

    # Executa a transcrição com o contexto e idioma travado
    segments, info = model.transcribe(
        audio_mais_recente,
        beam_size=5,
        language="pt",  # Força português para evitar detecção automatica
        initial_prompt=prompt_contexto,  # Guia o modelo com os termos
    )

    
    pasta_transcricoes = pasta_saida / "Transcricoes"

    #Cria a pasta no computador se ela ainda não existir
    pasta_transcricoes.mkdir(parents=True, exist_ok=True)
    texto_completo = " ".join([segment.text for segment in segments])
    nome_novo = f"{audio_mais_recente.stem}_transcricao.txt"
    arquivo_final = pasta_transcricoes / nome_novo
    arquivo_final.write_text(texto_completo, encoding="utf-8")
    return arquivo_final










# print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))