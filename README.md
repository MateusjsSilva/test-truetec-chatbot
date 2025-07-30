# TrueTec Virtual Assistant

This is a virtual customer service assistant for the fictional company **TrueTec**, specialized in technology solutions and technical support in Teresina-PI, Brazil. The assistant answers questions in natural language, helps open technical support tickets, and collects relevant customer information, using the Google Gemini API for natural language processing.

## How to Run the Project

### Prerequisites

- Python 3.8 or higher installed.

### 1. Clone the Repository

```bash
git clone https://github.com/MateusjsSilva/test-truetec-chatbot.git
cd test-truetec-chatbot
```

### 2. Configure the Google Gemini API Key

- Create an API key at [Google AI Studio](https://aistudio.google.com/app/apikey).
- Create a `.env` file at the root of the project with the following content:

```
GOOGLE_API_KEY=YOUR_GENERATED_KEY_HERE
```

> **Important:** Do not share your API key publicly.

### 3. Create and Activate the Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**  
  ```bash
  .\venv\Scripts\activate
  ```
- **Linux/macOS:**  
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Virtual Assistant

- **Terminal (text mode):**
  ```bash
  python src/main.py
  ```
- **Graphical Interface (WhatsApp-style chat):**
  ```bash
  python src/gui_app.py
  ```

## How to Test the Assistant

Example questions:

- **Sobre a empresa:**
  - "Qual o horário de funcionamento?"
  - "Qual o telefone da TrueTec?"
- **Abertura de chamado técnico:**
  - "Quero abrir um chamado para suporte."
  - "Minha internet caiu, preciso de ajuda."
- **Fora do escopo:**
  - "Qual a capital da França?"
  - "Conte uma piada."

Para sair da conversa digite 'sair'.

## Project Structure

```
TrueTec-Test/
├── .env                  # Environment variables (DO NOT version)
├── .env.example          # Example .env file
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── venv/                 # Virtual environment (DO NOT version)
├── src/
│   ├── __init__.py
│   ├── main.py           # Terminal mode
│   ├── gui_app.py        # Graphical interface (Tkinter)
│   ├── assistant_core.py # Assistant core logic
│   └── config.py         # API key configuration
└── .gitignore
```

---

## Notes

- The assistant uses Google's Gemini API. Make sure your key is active and has sufficient quota.
- The `.env` file should **NOT** be versioned.
- For questions or suggestions, open an issue in the repository.

---