import json
import random
import pandas as pd


class Prompt:
    """
    Prompt class to generate prompts for GPT.
    """

    def __init__(self):
        with open("dataforge-config.json", "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def dynamic_prompt(self, f):
        """
        Select 3 random examples from the CSV file.
        """
        examples = []

        df = pd.read_csv(f, encoding="utf-8")
        for _ in range(3):
            rand_num = random.randint(1, df.shape[0] - 1)
            examples.append('''{
                            instruction: "%s",
                            input: "%s",
                            output: %s
                        }''' % (df.iloc[rand_num]["instruction"],
                                df.iloc[rand_num]["input"],
                                df.iloc[rand_num]["output"]))

        return examples

    def get_prompt(self, f, subject):
        """
        Generate a prompt to be given to GPT.
        """
        if not self.config["dynamic-prompting"]:
            examples = '''[
                 {
                    instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                    répond au mieux en format JSON.",
                    input: "J'ai besoin d'aide en mathématiques",
                    output: {
                        "subject": "maths",
                        "topic": "general"
                    }
                },
                {
                    instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                    répond au mieux en format JSON.",
                    input: "J'ai besoin de mieux comprendre les matrices.",
                    output: {
                        "subject": "maths",
                        "topic": "matrices"
                    }
                },
                {
                   instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                   répond au mieux en format JSON.",
                   input: "C'est quoi la loi d'Ampère",
                   output: {
                       "subject": "electromag",
                       "topic": "ampere"
                   }
               }
        ]'''

        else:
            examples = "[\n"
            for ex in self.dynamic_prompt(f):
                examples += f"\t\t\t{ex}"
                examples += ",\n"
            examples += "\t\t]"

        return f'''
        Tu es un professeur spécialisé en {subject}. Tu as les connaissances à propos de tous les concepts et
        thèmatiques de cette matière.
        Agis en tant qu'analyseur de données avec ces 3 éléments : "instructions, entrée et sortie\n
        L'instruction sera toujours la même : "Tu es un analyseur de données chargé d'aider les étudiants à trouver des
        ressources, répond au mieux en format JSON."\n
        L'entrée sera quelque chose dont un étudiant a besoin pour ses études. Cela pourrait être formulé sous forme de
        phrase ou de question. Dans tous les cas, cela devra ressembler à une demande qu'un étudiant pourrait faire,
        par exemple : "J'ai besoin d'aide en mathématiques"\n
        Les demandes des étudiants DOIVENT SEULEMENT porter sur les thèmatiques et les matières qui sont présents dans
        le dictionnaire : {self.config["themes_dict"]} (la clé est la matière (subject) et la valeur est la liste des
        thématiques (topics)).\n
        La matière et les thématiques que tu vas aborder maintenant sont respectivement :
        {subject} et {self.config["themes_dict"][subject]}.
        Tu peux adopter la structure que tu préfère pour construire la demande.\n
        Les demandes DOIVENT UNIQUEMENT porter sur la matière en question et les thèmatiques qui la concerne. C'est très
        important !!\n
        Tu DOIS construire les demandes en fonction du degré de généralité. Par exemple, si la thématique est
        "Algèbre", tu dois construire des demandes sur les concepts mathématiques en algèbre, et ainsi de suite.
        NE SOIS PAS général dans les demandes.\n
        Essaie d'adopter un langage naturel de jeune étudiant, ne sois pas trop formel.\n
        La sortie doit être une réponse à l'entrée sous forme de format JSON.\n
        Donne-moi un format JSON qui est un tableau comportant CINQ lignes (instructions, entrées, sorties) de cette
        manière :
        {examples}
        \n
        'subject' et 'topic' DOIVENT être les MEMES que ceux écrits dans le dictionnaire {self.config["themes_dict"]}.\n
        Tu NE DOIS PAS rajouter les exemples donnés ci-dessus dans le format JSON, ils sont juste là pour te montrer
        comment le format JSON doit être construit.\n
        IMPORTANT : NE DONNE PAS le même exemple deux fois, il doit être unique.
        '''


if __name__ == "__main__":
    prompt = Prompt()
    print(prompt.get_prompt("test.csv", "maths"))
