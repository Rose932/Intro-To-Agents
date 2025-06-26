from config import API_KEY
from processor import process_input
from api import generate_text
from generator import format_response, log_interaction

def main():
    """
        Main function to run the Mistral AI chatbot CLI.
    """
    print("Welcome to the Mistral AI Chatbot. Type 'exit' to quit.")
    
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Process the input
            processed_input = process_input(user_input)

            # Generate response from Mistral AI
            response_text = generate_text(API_KEY, processed_input)

            # Formate the response into a structured object
            formatted_response = format_response(processed_input, response_text)

            # Log the interaction
            log_interaction(formatted_response)

            # Display the response to the user
            print("Bot:", formatted_response["response"])

        except Exception as e:
            # Handle any errors and provide feedback
            print("An error occurred:", str(e))

if __name__ == "__main__":
    main()