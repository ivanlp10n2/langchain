from llama_index import GPTSimpleVectorIndex, download_loader

DadJokesReader = download_loader("DadJokesReader")

loader = DadJokesReader()
documents = loader.load_data()
index = GPTSimpleVectorIndex(from_documents(documents))
question = "tell me a joke"
print(f"question {question}")
result = index.query(question)
print(result)

