from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

class Review(TypedDict):

      summary: str
      sentiment: str

structured_model = model.with_structured_output(Review)

review = """I recently purchased the XYZ product and I am extremely satisfied with its performance. The build quality is excellent and it works exactly as advertised. I would highly recommend this product to anyone in the market for something similar."""

result = structured_model.invoke(review)
print(result)