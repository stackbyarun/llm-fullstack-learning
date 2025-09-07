import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#load api key from env
api_key = os.getenv("GOOGLE_API_KEY")
#initialize the gemini llm
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",api_key=api_key,temperature=0)
#prompt 1 : Extract information
prompt_extract = ChatPromptTemplate.from_template(
    "Extract the keywords from this text:\n{text_input}\n")

#prompt 2 : Transform to JSON
prompt_transform = ChatPromptTemplate.from_template(
    "Transform the following specifications into a JSON object with 'cpu', 'memory', and 'storage' as keys:\n\n{specifications}"
)

#build the chain
extraction_chain = prompt_extract|llm|StrOutputParser()
full_chain =(
    {"specifications":extraction_chain}
    |prompt_transform
    |llm
    |StrOutputParser()
)
#---run the chain
input_text = "the new laptop model features a 3.5 ghz octa-core processor,16gb ram ,and 1Tb ssd NVem."

final_result = full_chain.invoke({"text_input":input_text})
print("\n---Final Json output---")
print(final_result)
