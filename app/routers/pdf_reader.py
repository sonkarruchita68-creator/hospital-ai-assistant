from fastapi import APIRouter

from app.services.rag import extract_pdf_text, split_text
from app.services.embeddings import create_embeddings
from app.services.vectorstore import vector_store

router = APIRouter()


@router.get("/read-pdf")
def read_pdf():
    text = extract_pdf_text("app/uploads/sample.pdf")
    chunks = split_text(text)

    return {
        "total_chunks": len(chunks),
        "chunks": chunks
    }


@router.get("/embed-pdf")
def embed_pdf():
    text = extract_pdf_text("app/uploads/sample.pdf")
    chunks = split_text(text)

    embeddings = create_embeddings(chunks)
    
    vector_store.add(chunks, embeddings)

    return {
        "total_chunks": len(chunks),
        "embedding_dimension": len(embeddings[0]) if embeddings else 0,
        "embeddings_created": len(embeddings)
    }
    
@router.get("/search")
def search_pdf():
    text = extract_pdf_text("app/uploads/sample.pdf")
    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    vector_store.add(chunks, embeddings)

    query_embedding = embeddings[0]

    results = vector_store.search(query_embedding)

    return {
        "results": results
    }