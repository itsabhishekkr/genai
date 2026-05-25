
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.1,  
    max_new_tokens=150 
)
model = ChatHuggingFace(llm=llm)




def get_researcher_info(question):
    result = model.invoke(question)
    return result.content