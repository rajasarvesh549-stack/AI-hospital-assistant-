from langchain_text_splitters import RecursiveCharacterTextSplitter
from read_pdf import extract_text_from_pdf

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=30
    )

    
    chunks = splitter.split_text(text)
    return chunks


if __name__ == "__main__":
    text = extract_text_from_pdf("documents/PatientAdmission.pdf")
    chunks = chunk_text(text)

    print(f"Total chunks created: {len(chunks)}")
    print("---")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        print(chunk)
        print("---")

        
