import json
import os
import sys

import openai
import pandas as pd
from dotenv import load_dotenv
from duplicates_verification import DuplicatesVerification
from prompt import Prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAIGenerator:
    """
    GPT3.5 turbo class that uses a prompt to generate a dataset.
    Dataset is then saved in a csv file to be used for fine-tune LLM.
    """

    def __init__(self):
        # Set the API key
        with open("dataforge-config.json", "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.prompt = Prompt()
        self.response = None

    def model(self, prompt_content):
        """
        Generate a response from the prompt.
        """
        self.response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt_content,
                },
            ],
            temperature=0.3,
            max_tokens=2000,
        )

    def write_csv(self, subject):
        """
        Generate a csv file from the response.
        """
        response = self.response["choices"][0]["message"]["content"]

        try:
            response_to_json = json.loads(response)
            with open(f"llama-{subject}-dataset.csv", "a", encoding="utf-8") as f:
                # if file is not empty don't write the header
                if os.stat(f"llama-{subject}-dataset.csv").st_size == 0:
                    f.write("instruction,input,output\n")

                for data in response_to_json:
                    # write the data to the file
                    try:
                        f.write(
                            f"{data['instruction'].replace(',', '')},"
                            f"{data['input'].replace(',', '')},"
                            f"{json.dumps(data['output']).replace(',', ';')}\n"
                        )
                    except KeyError:
                        pass

        except json.decoder.JSONDecodeError as e:
            print("JSONDecodeError")
            print(e)

    def generate_dataset(self, nb_iterations):
        """
        Generate a dataset from the prompt.
        """
        # get the model
        for key in self.config['themes_dict'].keys():
            print(f"subject: {key}")

            for i in range(nb_iterations):
                print(f"iteration: {i + 1}")
                dyn_prompt = self.prompt.get_prompt(f="test.csv", subject=key)
                self.model(prompt_content=dyn_prompt)
                self.write_csv(subject=key)
                print(f"generated {(i + 1) * 5} responses")

    def combine_datasets(self):
        """
        Combine all datasets into one.
        """
        found = False
        # you should have header like other csv: instruction,input,output only one time
        # create hader in the first file
        with open('bigbrain-dataset.csv', 'w', encoding="utf-8") as f:
            f.write("instruction,input,output\n")

        for f in os.listdir():
            if f.endswith('.csv'):
                found = True
                df = pd.read_csv(f, encoding="utf-8")
                df.to_csv('bigbrain-dataset.csv', mode='a', header=False, index=False)
                print(f"Combined {f} into bigbrain-dataset.csv")

        if not found:
            return print("No csv file found")
        return print("Done combining datasets")


if __name__ == "__main__":
    generator = OpenAIGenerator()
    args = sys.argv[1:]
    list_args = ['--generate', '--combine', '--no-duplicates']

    if '--generate' in args:
        generator.generate_dataset(generator.config['nb_iterations'])

    if '--combine' in args:
        generator.combine_datasets()

    if '--no-duplicates' in args:
        for file in os.listdir():
            if file.endswith('.csv'):
                duplicates = DuplicatesVerification(file=file)
                duplicates.verify_duplicates()

    if not args or not set(args).issubset(set(list_args)) or args == '--help':
        print("Please use: "
              "\n--generate to generate a dataset"
              "\n--combine to combine all datasets into one"
              "\n--no-duplicate to verify duplicates in the csv files")
