from langchain_cerebras import ChatCerebras
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def chatbot_initialization(system_message, user_message, output_payload):
    # Ensure the API key is loaded
    api_key = os.getenv("CEREBRAS_API_KEY")
    if not api_key:
        raise ValueError("CEREBRAS_API_KEY is not set in the environment.")

    # Initialize the Cerebras model
    model = ChatCerebras(
        model="llama3.1-70b",
        api_key=api_key,
    )

    # Define the JSON parser for structured output
    parser = JsonOutputParser(pydantic_object=output_payload)

    # Create a prompt template for structured LLM responses
    prompt = PromptTemplate(
        template="Generate a response in the following JSON format:\n"
                 "{format_instructions}\n"
                 "System Message:\n{system_message}\n"
                 "User Message:\n{user_message}\n",
        input_variables=["system_message", "user_message", "format_instructions"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    
    # Format the prompt with the system and user messages
    formatted_prompt = prompt.format(
        system_message=system_message,
        user_message=user_message,
    )

    # Run the model and get the response
    chatbot_response = model.invoke(formatted_prompt)

    # Check if the response is an AIMessage and extract its content as a string
    if hasattr(chatbot_response, 'content'):
        response_content = chatbot_response.content
    else:
        response_content = str(chatbot_response)

    # Parse the response content
    structured_response = parser.parse(response_content)

    return structured_response



# utils.py or similar utility file
def construct_user_message(payload):
    return (
        f"Weight: {payload.weight} kg, Height: {payload.height} inches, Days of workout: {payload.days_workout}, "
        f"Gender: {payload.gender}, Fitness goal: {payload.fitness_goal}, Meals: {payload.meals}, Budget Plan: {payload.budget_friendly}"
    )

