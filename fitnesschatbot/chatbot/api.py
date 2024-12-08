from ninja import NinjaAPI
from .schema import DietPlanRequest, DietPlanResponse
from .utils import chatbot_initialization
from .constants import diet_plan_system_message

# Initialize the API
api = NinjaAPI()

# Define a POST endpoint to generate the diet plan
@api.post("/chatbot/generate-diet-plan", response={200: DietPlanResponse})
def generate_diet_plan(request, payload: DietPlanRequest):
    
    # Extract the user message from the payload
    user_message = (
        f"Weight: {payload.weight} kg, Height: {payload.height} inches, Days of workout: {payload.days_workout}, "
        f"Gender: {payload.gender}, Fitness goal: {payload.fitness_goal}, Meals: {payload.meals}"
    )
    
    # Invoke the chatbot to get the diet plan response
    chatbot_response = chatbot_initialization(diet_plan_system_message,user_message, DietPlanResponse)

    # Return the structured diet plan
    return chatbot_response

