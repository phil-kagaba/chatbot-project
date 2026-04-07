# 📖 Chatbot-Project

**Cornell Movie Dialogs Chatbot**

A simple AI chatbot using the Cornell Movie Dialogs Corpus. It responds to user input by finding the closest matching line from the dataset. Supports **TF-IDF** or **embeddings** for better responses.

---

## 🗂 Project Structure
```bash
chatbot-project/
├── dataset.csv # Preprocessed Q&A
├── prepare_data.py # Generates dataset.csv
├── model.py # Chatbot brain (TF-IDF or embeddings)
├── app.py # CLI chat interface
└── README.md # This file
```
---

## ⚡ Features

- Loads Cornell Movie Dialogs Corpus  
- Creates clean **question-answer pairs**  
- Uses TF-IDF or embeddings for matching  
- Simple CLI chat interface  

---

## 🛠 Requirements

```bash
pip install pandas scikit-learn numpy sentence-transformers

movie_lines.txt
movie_conversations.txt

```

## 🛠 Generate the dataset:
```bash
python prepare_data.py
```

## 🛠 Run the Chatbot
```bash
python app.py
```
Type a message → bot replies
Type exit to quit

## 🛠 Example Chat

You: hello
Bot: hi.

You: how are you?
Bot: i am fine, thanks.

You: what’s your name?
Bot: my name is vicki.
