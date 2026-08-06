from sentence_transformers import SentenceTransformer
from chunk_text import chunk_text
from read_pdf import extract_text_from_pdf

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    embeddings = model.encode(chunks)
    return embeddings


if __name__ == "__main__":
    text = extract_text_from_pdf("documents/PatientAdmission.pdf")
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)

    print(f"Number of chunks: {len(chunks)}")
    print(f"Shape of embeddings: {embeddings.shape}")
    print("---")
    print("First embedding (first 10 numbers only):")
    print(embeddings[0][:10])


    


