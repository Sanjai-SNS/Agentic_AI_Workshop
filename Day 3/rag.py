# -*- coding: utf-8 -*-
"""RAG.ipynb"""

# 📦 Step 1: Install Dependencies
!pip install -q faiss-cpu sentence-transformers transformers PyMuPDF

# 📂 Step 2: Upload PDFs
from google.colab import files
uploaded = files.upload()

# 📥 Step 3: Load and Extract Text from PDFs
import fitz  # PyMuPDF

def load_pdfs(uploaded_files):
    texts = []
    for fname in uploaded_files:
        doc = fitz.open(fname)
        for page_num, page in enumerate(doc):
            texts.append({
                "page": page_num + 1,
                "text": page.get_text()
            })
    return texts

pdf_texts = load_pdfs(uploaded.keys())
print(f"Loaded {len(pdf_texts)} pages.")

# 🧱 Step 4: Chunk the Text
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def chunk_texts(texts):
    chunks = []
    for entry in texts:
        words = entry["text"].split()
        for i in range(0, len(words), CHUNK_SIZE - CHUNK_OVERLAP):
            chunk = " ".join(words[i:i + CHUNK_SIZE])
            if chunk:
                chunks.append({"page": entry["page"], "chunk": chunk})
    return chunks

chunks = chunk_texts(pdf_texts)
print(f"Generated {len(chunks)} chunks.")

# 📐 Step 5: Embed the Chunks
from sentence_transformers import SentenceTransformer
import numpy as np

embedder = SentenceTransformer('all-MiniLM-L6-v2')
texts = [c["chunk"] for c in chunks]
embeddings = embedder.encode(texts, show_progress_bar=True)
embeddings = np.array(embeddings).astype("float32")

# 🔎 Step 6: Build FAISS Index
import faiss

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# 💬 Step 7: Answer Questions using Retrieved Context
from transformers import pipeline

qa_generator = pipeline("text2text-generation", model="google/flan-t5-base")

def retrieve(query, k=3):
    q_embedding = embedder.encode([query]).astype("float32")
    D, I = index.search(q_embedding, k)
    return [chunks[i] for i in I[0]]

def generate_answer(query):
    top_chunks = retrieve(query)
    context = "\n".join([f"[Page {c['page']}] {c['chunk']}" for c in top_chunks])
    prompt = f"Answer the question based on the context below.\nContext: {context}\nQuestion: {query}"
    result = qa_generator(prompt, max_length=1024)[0]['generated_text']
    return result, top_chunks

# 🧪 Step 8: Ask a Question
question = {"Explain about Positional Encoding"
}
answer, sources = generate_answer(question)

print("✅ Answer:\n", answer)
print("\n📚 Sources:")
for src in sources:
    print(f"- Page {src['page']}")
