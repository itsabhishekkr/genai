# from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
# from dotenv import load_dotenv
# load_dotenv()
# import os
# os.environ["HF_HOME"] = "D:/Genai/Models"

# # Configure the HuggingFacePipeline with the desired model and parameters
# llm  = HuggingFacePipeline.from_model_id(
#     model_id="meta-llama/Llama-3.1-8B-Instruct",
#     task="text-generation",
#     pipeline_kwargs={"temperature": 0, "max_new_tokens": 50}
# )

# model = ChatHuggingFace(llm=llm)
# result = model.invoke("i am a buigneer and i wanted to learn about the python programming language, can you teach me the basics of code in python?")
# print(result.content)

# not recomended as it is not working properly, the above code is working fine but it is taking a lot of time to load the model and generate the response, so it is better to use the HuggingFaceEndpoint which is faster and more efficient.