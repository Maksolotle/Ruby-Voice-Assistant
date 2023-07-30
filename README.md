# Maks-Voice-Assistant

![poster](poster.jpg)

`Maks` - is a voice assistant using neural networks for things like **STT/TTS/Wake Word/NLU** etc.

The main project challenges we try to achieve is:
 - 100% offline *(no cloud)*
 - Open source *(Full transparency)*
 - No data collection *(I respect your privacy)*

Our backend stack is 🐍 **[Python](https://www.python.org/)**, 🦀 **[Rust](https://www.rust-lang.org/)** with ❤️ **[Tauri](https://tauri.app/)**.<br>
For the frontend I use 🌐 **[HTML](https://ru.wikipedia.org/wiki/HTML)** + 💥 **[CSS](https://ru.wikipedia.org/wiki/CSS)** + 🛠️ **[JavaScript](https://ru.wikipedia.org/wiki/JavaScript)** with 💙 **[jQuery](https://jquery.com/)**

*Other libraries, tools and packages can be seen in requirements.txt*

## Neural Networks

This are the neural networks I am currently using:

 - Speech-To-Text
	 - [Vosk Speech Recognition Toolkit](https://github.com/alphacep/vosk-api)
 - Text-To-Speech
	 - [Pyttsx3](https://pypi.org/project/pyttsx3/) *(soon to be replaced by our own)*

 - Wake Word
	 - [Vosk Speech Recognition Toolkit](https://github.com/alphacep/vosk-api)
 - Chat
	- [~~ChatGPT~~](https://chat.openai.com/) (coming soon)

## Supported Languages

Currently, only Russian language is supported.<br>
But soon, Ukranian and English will be added for the interface, wake-word detection and speech recognition.

## How to build?

Nothing special was used to build this project.<br>
You need only Rust and Python installed on your system.<br>
Other than that, all you need is to install all the dependencies and then compile the code with `cargo tauri build` command.<br>

## Author

Maksolotle
