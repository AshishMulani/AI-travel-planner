import google.generativeai as genai
from langchain.chat_models import ChatOpenAI

# Initialize Google GenAI (set up your API key)
genai.configure(api_key="AIzaSyApJBcqf9MfKvaihVzVFTXCS5CGsKGayVc")

def get_travel_options(source, destination):
    # Define the prompt for GenAI
    prompt = f"Suggest travel options from {source} to {destination} with estimated costs."
    
    # Use Google GenAI to generate responses
    model = genai.GenerativeModel("gemini-pro")  # Adjust model name as needed
    response = model.generate_content(prompt)
    
    # Process output (assuming structured JSON response)
    travel_options = parse_response(response.text)
    
    return travel_options

def parse_response(response_text):
    """ Convert GenAI response into structured travel options """
    # Dummy parsing for simplicity; adjust based on actual response format
    options = []
    for line in response_text.split("\n"):
        parts = line.split("-")
        if len(parts) == 2:
            mode, cost = parts
            options.append({"mode": mode.strip(), "cost": cost.strip()})
    return options
