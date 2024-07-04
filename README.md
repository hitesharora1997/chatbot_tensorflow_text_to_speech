# ChatBot 

This project is a simple voice-activated chatbot that uses Google's Speech Recognition and Text-to-Speech, and the DialoGPT model for conversation.

## Project Structure

chatbot_project/
│
├── chatbot/
│ ├── init.py
│ ├── chatbot.py
│ ├── speech.py
│ ├── text_to_speech.py
│ └── utilities.py
│
├── main.py
│
└── README.md



## Files and Directories

- **chatbot/**: Contains the main logic and helper functions for the chatbot.
  - **chatbot.py**: Defines the `ChatBot` class.
  - **speech.py**: Contains the `speech_to_text` function.
  - **text_to_speech.py**: Contains the `text_to_speech` function.
  - **utilities.py**: Contains helper functions like `wake_up` and `action_time`.
  - **\_\_init\_\_.py**: Makes the directory a Python package.
- **main.py**: The main entry point to run the chatbot.
- **README.md**: This file.

## Setup

1. Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Ensure you have `mpg123` installed for Linux if not already available:
    ```bash
    sudo apt-get install mpg123
    ```

## Usage

To run the chatbot, simply execute:

```bash
python main.py
