import json
import os
import openai
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
            temperature=0.5,
            max_tokens=2000,
        )

    def generate_csv(self, subject):
        """
        Generate a csv file from the response.
        """
        response = self.response["choices"][0]["message"]["content"]

        try:
            response_to_json = json.loads(response)
            with open(f"llama-{subject}-dataset.csv", "a", encoding="cp1252") as f:
                # if file is not empty don't write the header
                if os.stat(f"llama-{subject}-dataset.csv").st_size == 0:
                    f.write("instruction,input,output,text\n")

                for data in response_to_json:
                    # write the data to the file
                    try:
                        f.write(
                            f"{data['instruction'].replace(',', '')},"
                            f"{data['input'].replace(',', '')},"
                            f"{json.dumps(data['output']).replace(',', ';')},"
                            f"{data['text'].replace(',', '')}\n"
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
                dyn_prompt = self.prompt.get_prompt(f=f"manual-questions-{key}.csv", subject=key)
                self.model(prompt_content=dyn_prompt)
                self.generate_csv(subject=key)
                print(f"generated {(i + 1) * 5} responses")


if __name__ == "__main__":
    generator = OpenAIGenerator()
    # generate dataset
    generator.generate_dataset(generator.config['first-step-iterations'])
    # generator.generate_dataset(generator.config['second-step-iterations'])

    # add manual questions
    # generator.add_manual_questions("manual-questions-maths.csv", "llama-maths-dataset.csv")
    # generator.add_manual_questions("manual-questions-physics.csv", "llama-physics-dataset.csv")

    # verify duplicates in csv files
    print('\n')
    for file in os.listdir():
        if file.endswith('.csv'):
            duplicates = DuplicatesVerification(file=file)
            duplicates.verify_duplicates()
