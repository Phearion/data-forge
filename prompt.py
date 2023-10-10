import json

with open("DataForgeConfig.json", "r", encoding="utf-8") as file:
    config = json.load(file)


def get_prompt(subject):
    return '''
    Tu es un professeur spécialisé en %s. Tu as les connaissances à propos de tous les concepts et thèmatiques de cette
    matière.
    Agis en tant qu'analyseur de données avec ces 3 éléments : "instructions, entrée et sortie\n"
    L'instruction sera toujours la même : "Tu es un analyseur de données chargé d'aider les étudiants à trouver des
    ressources, répond au mieux en format JSON."\n
    L'entrée sera quelque chose dont un étudiant a besoin pour ses études. Cela pourrait être formulé sous forme de
    phrase ou de question. Dans tous les cas, cela devra ressembler à une demande qu'un étudiant pourrait faire,
    par exemple : "J'ai besoin d'aide en mathématiques""\n
    Les demandes des étudiants DOIVENT SEULEMENT porter sur les thèmatiques et les matières qui sont présents dans le
    dictionnaire : %s (la clé est le matière (subject) et la valeur est la liste des thèmatiques (topics))""
    Le matière et les thématiques que tu vas aborder maintenant sont respectivement : %s et %s.
    Tu peux adopter la structure que tu préfére pour construire la demande."\n
    Voici quelques exemples de structures de phrases qui pourraient être utilisées:"\n
    Pourriez-vous m'aider à,
    J'ai du mal à,
    Je ne sais pas comment faire,
    Pouvez-vous m'aider à améliorer,
    Je suis bloqué sur,
    J'ai des problèmes avec,
    Avez-vous des conseils pour,
    Pourriez-vous me donner des conseils sur"\n
    Les demandes DOIVENT UNIQUEMENT porter sur la matière en question et les thèmatiques qui la concerne. C'est très
    important !!"\n
    Tu DOIS construire les demandes en fonction du degré de généralité. Par exemple, si le thèmatique est
    "Algèbre", tu dois construire des demandes sur les concepts mathématiques en algèbre, et ainsi de suite.
    NE SOIS PAS général dans les demandes.\n
    La sortie doit être une réponse à l'entrée sous forme de format JSON.\n".
    \nDonne-moi un format JSON qui est un tableau comportant CINQ lignes (instructions, entrées, sorties) de cette
     manière :"
    [
             {
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "J'ai besoin d'aide en mathématiques",
                output: {
                    "subject": "Maths",
                    "topic": "General"
                }
            },
            {
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "J'ai besoin de mieux comprendre les matrices.",
                output: {
                    "subject": "Maths",
                    "topic": "Matrices"
                }
            }
    ]
    \n
    'subject' et 'topic' DOIVENT être les MEMES que ceux écrits dans le dictionnaire %s.\n
    Tu NE DOIS PAS rajouter les exemples donnés ci-dessus dans le format JSON, ils sont juste là pour te montrer comment
    le format JSON doit être construit.\n

    IMPORTANT : NE DONNE PAS le même exemple deux fois, il doit être unique.
    ''' % (subject,
           config["themes_dict"],
           subject,
           config["themes_dict"][subject],
           config["themes_dict"])
