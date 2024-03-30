# Ruby-Voice-Assistant

`Ruby` - is a voice assistant using neural networks for things like **STT/TTS/Wake Word/NLU** etc.

Achievements in this project:
 - 100% offline *(no cloud)*
 - Open source *(full transparency)*
 - No data collection *(I respect your privacy)*

My backend stack is 🐍 **[Python](https://www.python.org/)** 🦀 **[Rust](https://www.rust-lang.org/)** with ❤️ **[Tauri](https://tauri.app/)**.<br>
For the frontend I use 🌐 **[HTML](https://ru.wikipedia.org/wiki/HTML)** + 💥 **[CSS](https://ru.wikipedia.org/wiki/HTML)** + 🛠️ **[JavaScript](https://ru.wikipedia.org/wiki/JavaScript)**

## Neural Networks

This are the neural networks I are currently using:

 - Speech-To-Text
	 - [Vosk Speech Recognition Toolkit](https://github.com/alphacep/vosk-api)
 - Text-To-Speech
	 - ~~[Pyttsx3](https://pypi.org/project/pyttsx3/)~~
         - ~~[Silero](https://pypi.org/project/silero/)~~
         - [Silero-Advanced](https://pypi.org/project/silero-advanced/) *(Soon there will be its own)*	
 - Wake Word
	 - [Vosk Speech Recognition Toolkit](https://github.com/alphacep/vosk-api)
- Chat
	- [ChatGPT](https://chat.openai.com/)

## Supported Languages

Currently, only Russian language is supported.<br>
But soon, Ukranian and English will be added for the interface, wake-word detection and speech recognition.

## How to build?

Nothing special was used to build this project.<br>
You need only Python and Rust installed on your system.<br>
Then you need follow these [instructions](https://tauri.app/v1/guides/getting-started/setup/html-css-js) on the Tauri website.
And you need to download Vosk model and move it to the Ruby-Voice-Assistant\APP directory.
All libraries in the file: requirements.txt.

## Author

Maksolotle
