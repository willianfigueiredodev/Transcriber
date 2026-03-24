# Transcriber de Áudio

Projeto simples para transcrever áudios usando a biblioteca `whisper` da OpenAI. O script lê arquivos de áudio (nos formatos `.mp3`, `.wav` e `.m4a`) colocados na pasta `audios/` e retorna a transcrição no terminal.

## Pré-requisitos

Para rodar o projeto, você precisa ter instalado no seu sistema operacional:
- **Python 3.8+**
- **FFmpeg**: O Whisper depende do FFmpeg para processar o áudio.
  - No Ubuntu/Debian: `sudo apt update && sudo apt install ffmpeg`
  - No macOS (via Homebrew): `brew install ffmpeg`
  - No Windows (via Chocolatey): `choco install ffmpeg`

## Instalação

Recomenda-se o uso de um ambiente virtual (Virtual Environment) para não conflitar com as dependências do seu sistema.

1. **Crie e ative o ambiente virtual** (opcional, mas recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Linux/macOS
   # No Windows: venv\Scripts\activate
   ```

2. **Instale as dependências via pip**:
   ```bash
   pip install -r requirements.txt
   ```

   *(O comando principal da instalação baixa o pacote `openai-whisper` e o `torch` caso não estejam instalados).*

## Como Usar

1. Crie uma pasta chamada `audios` na raiz do projeto (caso não exista):
   ```bash
   mkdir -p audios
   ```
2. Mova seus arquivos `.mp3`, `.wav` ou `.m4a` para dentro da pasta `audios/`.
3. Execute o script:
   ```bash
   python transcrever.py
   ```

O texto transcrito pelo modelo `base` será exibido diretamente na saída do terminal. Caso queira um modelo mais robusto ou mais rápido (ex: `tiny`, `small`, `medium`, `large`), basta alterar a linha `whisper.load_model("base")` no arquivo `transcrever.py`.
