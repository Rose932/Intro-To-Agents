from mistralai import Mistral

def generate_text(api_key, prompt):
    """
        Generate text using Mistral AI's API.

        Args:
        api_key (str): The Mistral AI API key.
        prompt (str): The user's input prompt.

        Returns:
        str: The generated response text.
    """

    client = Mistral(api_key=api_key)
    response = client.chat.complete(
        model="open-mistral-7b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content