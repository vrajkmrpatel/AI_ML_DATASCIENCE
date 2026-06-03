from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="models/text-bison-001", temperature=0.7)

result = llm.invoke("What is the capital of France?")
print(result.content)