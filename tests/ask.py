from rag.rag_chain import ask_question


def main():
    print("Ask questions about your PDF (type 'exit' to quit)\n")

    while True:
        question = input("Question: ").strip()

        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue

        result = ask_question(question)
        print("\nAnswer:", result["answer"])
        print("Sources: pages", result["pages"], "\n")


if __name__ == '__main__':
    main()