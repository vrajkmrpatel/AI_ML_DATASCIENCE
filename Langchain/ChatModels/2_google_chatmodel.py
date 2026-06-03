from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)

result = model.invoke("What is the capital of France?")
print(result.content[0]['text'])