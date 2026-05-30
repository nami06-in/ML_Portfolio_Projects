from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_ollama import OllamaLLM

from langchain_core.prompts import PromptTemplate

from config import *

print("1. Loading embeddings")

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

print("2. Embeddings loaded")

db = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

print("3. FAISS loaded")

retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

print("4. Retriever created")

llm = OllamaLLM(
    model=LLM_MODEL
)

print("5. LLM loaded")

prompt_template = """
You are a pneumonia medical assistant.

Answer ONLY from the provided context.

If the answer is not found in the context,
say:

"I do not have enough information in the provided medical documents."

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template
)

print("\nPNEUMONIA RAG CHATBOT")
print("Type 'exit' to stop.\n")

while True:

    question = input("You: ")

    print("6. Question received")

    docs = retriever.invoke(question)

    print("7. Documents retrieved")

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    print("8. Context created")

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    print("9. Prompt created")

    response = llm.invoke(final_prompt)

    print("10. Response generated")

    print("\nBot:", response)
    print()