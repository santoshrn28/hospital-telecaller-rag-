import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load documents
with open("data/hospital_docs.txt", "r") as f:
    docs = f.readlines()

# Embed docs
doc_embeddings = model.encode(docs)

# Create FAISS index
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

def retrieve_context(query, top_k=3):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, top_k)
    return [docs[i] for i in I[0]]
