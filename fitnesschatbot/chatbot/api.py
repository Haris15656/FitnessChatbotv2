from ninja import NinjaAPI
from .schema import PlanRequest, DietPlanResponse, WorkoutPlanResponse
from .utils import chatbot_initialization, construct_user_message
from .constants import diet_plan_system_message,workout_plan_system_message

# Initialize the API
api = NinjaAPI()

# Define a POST endpoint to generate the diet plan
@api.post("/chatbot/generate-diet-plan", response={200: DietPlanResponse})
def generate_diet_plan(request, payload: PlanRequest):
    
    # Extract the user message from the payload
    user_message = construct_user_message(payload)
    
    # Invoke the chatbot to get the diet plan response
    chatbot_response = chatbot_initialization(diet_plan_system_message,user_message, DietPlanResponse)
    
    # Return the structured diet plan
    return chatbot_response



@api.post("/chatbot/generate-workout-plan", response={200: WorkoutPlanResponse})
def generate_workout_plan(request, payload: PlanRequest):
    
    # Extract the user message from the payload
    user_message = construct_user_message(payload)
    
    # Invoke the chatbot to get the diet plan response
    chatbot_response = chatbot_initialization(workout_plan_system_message,user_message, WorkoutPlanResponse)

    # Return the structured diet plan
    return chatbot_response

