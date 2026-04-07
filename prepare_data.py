import pandas as pd

lines = open("movie_lines.txt", encoding='utf-8', errors='ignore').read().split('\n')

id2line = {}

for line in lines:
    parts = line.split(" +++$+++ ")
    if len(parts) == 5:
        id2line[parts[0]] = parts[4]

# Now load conversations
conversations = open("movie_conversations.txt", encoding='utf-8', errors='ignore').read().split('\n')

questions = []
answers = [] 

for conv in conversations:
    parts = conv.split(" +++$+++ ")
    if len(parts) == 4:
        line_ids = eval(parts[3])  # list of IDs
        
        for i in range(len(line_ids) - 1):
            questions.append(id2line[line_ids[i]])
            answers.append(id2line[line_ids[i+1]])

# Save dataset
df = pd.DataFrame({"question": questions, "answer": answers})
df.to_csv("dataset.csv", index=False)

print("Dataset created!")