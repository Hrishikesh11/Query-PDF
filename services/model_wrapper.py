import os
from openai import OpenAI
import json
from dotenv import load_dotenv

load_dotenv()
class ModelWrapper:
    def __init__(self):
        # Ensure API key is properly set
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))  # Ensure this is correctly set

    def query(self, question: list, context: str) -> dict:
        """Queries GPT-4 with multiple questions and a context."""
        try:
            # Format the questions in the required format
            # formatted_questions = "\n".join([f"Question {i + 1}: {question}" for i, question in enumerate(questions)])
            
            # Create the system message and user message based on the provided context and questions
            prompt = f"""
            Your task is to generate responses based on the provided context in <> for each question. 
            If the relevant information is not available in the given context, respond with the phrase "Data Not Available". 
           
            Context: <{context}>
            Questions:
            {question}
            """
            # print(prompt)
            # Query the model with the constructed prompt
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Ensure you're using the correct model
                messages=[{"role": "system", "content": "Answer questions based on the provided context."},
                          {"role": "user", "content": prompt}],
                temperature=0,
            )

            # Parse the response and return as a dictionary
            answer =response.choices[0].message.content.strip()
            return answer

        except Exception as e:
            raise RuntimeError(f"Error querying model: {e}")

