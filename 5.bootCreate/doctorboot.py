from langchain.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv
load_dotenv()

from models import get_researcher_info

input_question = [
    SystemMessage(content="You are a doctor who is an expert in the filed of medical research. you guid the right way to solve the problem of the patient. you have a lot of experience in this field and you can give the best answer to the question of the patient.")
]

while True:
    question = input("Ask anything about the researcher (or type 'exit' to quit): ")
    if question.lower() == "exit":
        print("Goodbye!")
        break
    
    input_question.append(HumanMessage(content=question))
    
    print("Searching for researcher information...")
    answer = get_researcher_info(input_question)
    
    input_question.append(AIMessage(content=answer))
    print("\nAnswer:")
    print(answer)