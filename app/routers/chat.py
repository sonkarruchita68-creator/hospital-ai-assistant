from fastapi import APIRouter

from app.services.rag import extract_pdf_text, split_text
from app.services.embeddings import create_embeddings
from app.services.vectorstore import vector_store
from app.services.groq_service import ask_groq

router = APIRouter()


@router.get("/chat")
def chat(question: str):
    question_lower = question.lower()

    emergency_keywords = [
        "heart attack",
        "suicide",
        "stroke",
        "unconscious",
        "severe bleeding",
        "emergency"
    ]

    if any(keyword in question_lower for keyword in emergency_keywords):
        return {
            "answer": "This may be a medical emergency. Please contact emergency medical services or visit the nearest hospital immediately.",
            "sources": []
        }

    text = extract_pdf_text("app/uploads/sample.pdf")

    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    vector_store.add(chunks, embeddings)

    context = "\n".join(chunks[:3])

    answer = ask_groq(question, context)

    return {
        "answer": answer,
        "sources": ["sample.pdf"]
    }