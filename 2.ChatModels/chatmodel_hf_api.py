from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# Use a highly-supported modern small model for the free Serverless API
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0,
    max_new_tokens=50  # Sets max token length for the response
)

# Pass the configured LLM into the Chat wrapper
model = ChatHuggingFace(llm=llm)

result = model.invoke("i am a buigneer and i wanted to learn about the python programming language, can you teach me the basics of code in python?")
print(result.content)

