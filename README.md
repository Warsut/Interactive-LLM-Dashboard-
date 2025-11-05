# Interactive Large Language Model (BOB)

An **interactive Large Language Model** that runs **locally on your device** — no cloud inference needed.

Users can:
- Upload files (PDFs, docs, txt, etc.)
- Have the model read / parse the file contents
- Ask questions and get contextual responses based on the uploaded data
- Create and switch between multiple chat sessions

This project is designed to give users privacy-first AI capabilities locally — removing dependency on remote cloud servers.

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| Local Model Inference | Runs on-device with no external API calls |
| File Upload Understanding | Users can upload files and the model will read/analyze them |
| Multi-Chat Session Support | Users can create new conversation threads |
| Contextual Answers | The LLM uses the file’s content to produce relevant responses |
| Privacy Focus | All execution and data remain local to the machine |

---

## 🛠️ Tech Stack

- Python
- Local LLM runtime (Ollama)
- Web UI (Python GUI)
- File parsing utilities

*(specifics will be defined once architecture is locked in)*

---

## 📦 Installation

```bash
git clone https://github.com/Interactive-LLM-Dashboard-.git
cd Interactive-LLM-Dashboard
pip install -r requirements.txt
python bob.py
