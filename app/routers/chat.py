from fastapi import APIRouter

from app.services.rag import extract_pdf_text, split_text
from app.services.embeddings import create_embeddings
from app.services.vectorstore import vector_store
from app.services.groq_service import ask_groq

router = APIRouter()


@router.get("/chat")
def chat(question: str):
    text = extract_pdf_text("app/uploads/sample.pdf")

    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    vector_store.add(chunks, embeddings)

    context = "\n".join(chunks[:3])

    answer = ask_groq(question, context)

    return {
        "question": question,
        "answer": answer
    }