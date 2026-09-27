from pathlib import Path
import argparse
from tkinter import filedialog
import json
def argumentos() -> tuple[str, Path]:
    parser = argparse.ArgumentParser(description="Transcreva e resuma audios de reuniões")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--folder", help="abre os arquivos para escolher o diretorio dos audios", action="store_true")
    group.add_argument("-t", "--text", help="usage: py main.py -t Caminho_do_texto", type=str)
    group.add_argument("-a", "--audio", help="usage: py main.py -a Caminho_do_audio", type=str)
    args = parser.parse_args()

    if args.text:
        caminho_texto = Path(args.text)
        if not caminho_texto.is_file() or caminho_texto.suffix.lower() != ".txt":
            parser.error("O arquivo especificado não existe ou não é um .txt válido.")
        return "text", caminho_texto

    if args.audio:
        caminho_audio = Path(args.audio)
        extensoes_validas = {".mp3", ".opus", ".aac", ".wav", ".flac"}
        if not caminho_audio.is_file() or caminho_audio.suffix.lower() not in extensoes_validas:
            parser.error("O arquivo de áudio não existe ou possui formato inválido.")
        return "audio", caminho_audio

    arquivo_config = Path(__file__).resolve().parent / "config.json"
    try:
        with arquivo_config.open("r", encoding="utf-8") as file:
            config_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        config_data = {}

    if not isinstance(config_data, dict):
        config_data = {}

    caminho_configurado = config_data.get("caminho")
    if args.folder or not config_data.get('caminho'):
        pasta_selecionada = filedialog.askdirectory()
        if not pasta_selecionada:
            parser.error("Nenhuma pasta de áudios foi selecionada.")
        pasta = Path(pasta_selecionada)
        if not pasta.is_dir():
            parser.error("A pasta selecionada não existe.")
        config_data["caminho"] = str(pasta)
        arquivo_config.write_text(
            json.dumps(config_data, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )
        return "folder", pasta

    pasta = Path(caminho_configurado)
    if not pasta.is_dir():
        parser.error(f"A pasta configurada não existe: {pasta}")
    return "folder", pasta