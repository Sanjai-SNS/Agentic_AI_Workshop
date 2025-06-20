# rag_utils.py
import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import requests
from bs4 import BeautifulSoup

EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
CHROMA_DIR = "chroma_db"

client = chromadb.Client(Settings(
    persist_directory=CHROMA_DIR,
    anonymized_telemetry=False
))
collection = client.get_or_create_collection("docs")

def embed_docs(texts, ids):
    embs = EMBED_MODEL.encode(texts).tolist()
    collection.add(
        embeddings=embs,
        documents=texts,
        ids=ids
    )

def query_docs(query, k=3):
    q_emb = EMBED_MODEL.encode([query]).tolist()
    results = collection.query(query_embeddings=q_emb, n_results=k)
    return results['documents'][0]

def extract_text_from_pdf(pdf_path):
    imgs = convert_from_path(pdf_path)
    return "\n".join(pytesseract.image_to_string(img) for img in imgs)

def extract_text_from_image(img_path):
    return pytesseract.image_to_string(Image.open(img_path))

def web_search_text(url):
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "html.parser")
        return "\n".join(p.get_text().strip() for p in soup.find_all("p"))
    except:
        return ""
