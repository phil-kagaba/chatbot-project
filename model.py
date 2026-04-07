import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("dataset.csv")

# Drop rows with missing question or answer
data = data.dropna(subset=['question', 'answer'])

# Convert to strings and strip whitespace
questions = data['question'].astype(str).str.strip()
answers = data['answer'].astype(str).str.strip()

# Remove empty questions
mask = questions != ""
questions = questions[mask]
answers = answers[mask]

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):
    user_input = str(user_input).strip()
    if user_input == "":
        return "Please type something."
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    return answers.iloc[index]