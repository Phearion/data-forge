# Import the openai package
import json

import openai
from prompt import prompt
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIGenerator:
    ''' create a class that uses gpt-3.5-turbo to follow the prompt in the variable inside the prompt.py: prompt.
    Then you should get those variables as a CSV by getting what's after "input" and "output" and then you should
    return the CSV as a string.'''

    def __init__(self):
        # Set the API key
        self.prompt = prompt
        self.response = None

    def model(self):
        self.response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": self.prompt,
                },
            ],
            temperature=0.3,
            max_tokens=2000,
        )

        # say if the response is ready
        print("response ready")

    def generate_csv(self):
        # get the response
        response = self.response["choices"][0]["message"]["content"]
        try:
            responseToJson = json.loads(response)
            with open("llama.csv", "a", encoding="utf-8") as file:
                # if file is not empty don't write the header
                if os.stat("llama.csv").st_size == 0:
                    file.write("instruction,input,output\n")

                for data in responseToJson:
                    # write the data to the file
                    try:
                        file.write(f"{data['instruction'].replace(',', '')},{data['input'].replace(',', '')},{json.dumps(data['output']).replace(',', ';')}\n")
                    except:
                        print("err")
        except:
            pass



if __name__ == "__main__":
    # create a class
    generator = OpenAIGenerator()
    # get the model
    for i in range(3):
        print(f"iteration {i}")
        generator.model()
        generator.generate_csv()
