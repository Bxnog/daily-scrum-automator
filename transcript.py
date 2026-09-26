from faster_whisper import WhisperModel
from datetime import date
import sys

def transcrever_ultimo_audio(pasta_input):
    EXTENSOES_VALIDAS = {".mp3", ".opus", ".aac", ".wav", ".flac"}
    audios = [
        p
        for p in pasta_input.iterdir()
        if p.is_file() and p.suffix.lower() in EXTENSOES_VALIDAS
    ]
    if audios:
        # max pega o maior valor de uma lista, a key decide o que vai ser comparado pra ver o maior
        # lambda f é tipo => do js, stat vê as propriedades do arquivo f, st_mtime é o tempo de alteração
        audio_mais_recente = max(audios, key=lambda f: f.stat().st_mtime)
    else:
        raise FileNotFoundError(f"Não há arquivos de áudio em: {pasta_input}")

    # escolhe o modelo
    model_size = "small"

    # Run on CPU with int8
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    # model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, info = model.transcribe(audio_mais_recente, beam_size=5)

    
    pasta_transcricoes = pasta_input / "Transcricoes"

    #Cria a pasta no computador se ela ainda não existir
    pasta_transcricoes.mkdir(exist_ok=True)
    data_hoje = date.today().strftime("%Y-%m-%d")
    texto_completo = " ".join([segment.text for segment in segments])
    nome_novo = f"{audio_mais_recente.stem}_{data_hoje}_transcricao.txt"
    arquivo_final = pasta_transcricoes / nome_novo
    arquivo_final.write_text(texto_completo, encoding="utf-8")
    return arquivo_final














# print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))