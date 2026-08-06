from store_embeddings import store_document, collection

documents_to_store = {
    "InfectionControl": "documents/InfectionControl.pdf",
    "InsurancePolicy": "documents/InsurancePolicy.pdf",
    "ClinicalGuidelines": "documents/ClinicalGuidelines.pdf",
    "DischargeProcess": "documents/DischargeProcess.pdf"
}

for doc_name, filepath in documents_to_store.items():
    store_document(filepath, doc_name)

print("Total chunks in collection:", collection.count())