import chromadb
from embed_text import model

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="hospital_documents")


def search_rag(query, top_k=2):
    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k
    )

    matched_chunks = results["documents"][0]
    sources = results["metadatas"][0]

    return matched_chunks, sources


if __name__ == "__main__":
    question = "What documents are required for admission?"
    chunks, sources = search_rag(question)

    print(f"Question: {question}")
    print("---")
    for chunk, source in zip(chunks, sources):
        print(f"Source: {source['source']}")
        print(f"Content: {chunk}")
        print("---")
