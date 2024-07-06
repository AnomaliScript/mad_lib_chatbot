# Import the OpenAI library
from openai import OpenAI
client = OpenAI(
    api_key = "#"
)
def main():
    while True:
        # Style of story
        style = input("What do kind of story do you want?")
        if style.lower() in ("bye", "exit", "stop", "quit"):
            return
        
        # Create a print statement requesting the users to enter one word for each category.
        print("Please enter the following prompts: \n1. An emotion \n2. A color \n3. A noun \n4. An adjective " + 
             "\n5. A verb (past tense) \n6. A plural noun \n7. A type of food \n8. Another adjective " + 
             "\n9. A verb \n10. A noun (plural) \n11. An occupation/job \n12. A type of animal \n13. An adjective " + 
             "\n14. A verb (past tense) \n15. A noun \n16. A name \n17. Another name \n")
        
        # Create an empty list called list_of_words.
        list_of_words = []
        
        # Create an empty string called string_of_words.
        string_of_words = " "
        
        # Create a for loop asking the user to enter a word for each category.
        for x in range(17):
            get_input = input("Enter a response to prompt #" + str(x+1) + ": ")
            if get_input.lower() in ("bye", "exit", "stop", "quit"):
                print("bye")
                return
            else:
                list_of_words.append(get_input)
        
        # Create a system_data list to set up the functionality of the chatbot and set the value as the user input as a string_of_words in a key/value pair.
        system_data = [
            {"role": "system", "content": "Generate a " + str(style) + " two-paragraph MadLib story using the words."},
            {"role": "user", "content": string_of_words.join(list_of_words)}
        ]
        
        # Make a client.chat.completions.create() API call and set the model and messages.
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = system_data,
            temperature = 1
        )
        
        # Extract the AI's response from the API call and set the value to assistant_response.
        assistant_response = response.choices[0].message.content
        
        # Create a new dictionary to define the "assistant" role and the assistant_response as the content value, and add the dictionary to the system_data list.
        system_data.append({"role": "assistant", "content": assistant_response})
        
        # Print the assistant's response.
        print("Assistant: " + assistant_response)

main()
print("bye")
