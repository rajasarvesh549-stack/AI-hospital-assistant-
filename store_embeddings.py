import chromadb
from chunk_text import chunk_text
from read_pdf import extract_text_from_pdf
from embed_text import embed_chunks

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="hospital_documents")


def store_document(filepath, doc_name):
    text = extract_text_from_pdf(filepath)
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)

    ids = [f"{doc_name}_chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=chunks,
        metadatas=[{"source": doc_name} for _ in chunks]
    )
    print(f"Stored {len(chunks)} chunks from {doc_name}")


if __name__ == "__main__":
    store_document("documents/PatientAdmission.pdf", "PatientAdmission")
    print("Total chunks in collection:", collection.count())
