import os
# STEP 1: Set the directory FIRST before loading anything else
os.environ["HF_HOME"] = r"D:\ollama-model"

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
# This model is tiny (under 100MB), fast, and highly rated
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2",)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

embeddings_documents = embeddings.embed_documents(documents)
embeddings_query = embeddings.embed_query(query)

print(embeddings_documents)
print(embeddings_query)

# Calculate cosine similarity between the query and each document
similarities = cosine_similarity([embeddings_query], embeddings_documents)[0]
# Get the index of the most similar document
print(similarities)

sim_list=list(enumerate(similarities))
index,score=sorted(sim_list,key=lambda x:x[1],reverse=True)[0]
print(index, score)
print(documents[index])