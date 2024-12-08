# chatapi/schema.py
from pydantic import BaseModel
from typing import List, Dict

class PlanRequest(BaseModel):
    """Schema for the diet plan request."""
    weight: float
    height: float  
    days_workout: int  
    gender: str
    fitness_goal: str
    budget_friendly: bool
    meals: int  # Change from str to int if it represents the number of meals


class MealPlan(BaseModel):
    """Schema for an individual meal plan."""
    meal_name: str  # Name of the meal, e.g., "Breakfast"
    ingredients: List[str]  # List of ingredients
    nutritional_value: Dict[str, float]  # Nutritional values, e.g., {"protein": 20.0, "carbohydrates": 30.0, "calories": 250.0}

class DailyDietPlan(BaseModel):
    """Schema for the diet plan of an individual day."""
    day: str  # Name of the day, e.g., "Monday"
    meals: List[MealPlan]  # List of meal plans for the day

class DietPlanResponse(BaseModel):
    """Schema for the diet plan response."""
    diet_plan: List[DailyDietPlan]  # A list containing the diet plan for each day of the week


class Exercise(BaseModel):
    name: str
    sets: int
    reps: int

class DayWorkout(BaseModel):
    day: str
    type: str
    exercises: List[Exercise]

class WorkoutPlanResponse(BaseModel):
    workoutPlan: List[DayWorkout]
    

