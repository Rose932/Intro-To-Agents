from datetime import datetime
import json

def format_response(prompt, response_text):
    """
    Format the response into a structured JSON object.

    Args:
    prompt (str): Tthe user's input prompt.
    response_text (str): The generated response from the API.

    Returns:
    dict: A dictionary containing the prompt, response and timestamp.
    """

    return {
        "prompt": prompt,
        "response": response_text,
        "timestamp": datetime.now().isoformat()
    }

def log_interaction(formatted_response):
    """
    Log the interaction to a file in JSON format.

    Args:
    formatted_response (dict): The structured response data
    """
    with open("interactions.log", "a") as log_file:
        log_file.write(json.dumps(formatted_response) + "\n")