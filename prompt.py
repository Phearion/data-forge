import json

with open("dataforge-config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

print(config)
def get_prompt(subject):
    return '''
    Tu es un professeur spécialisé en %s. Tu as les connaissances à propos de tous les concepts et thèmatiques de cette matière.
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
    Tu DOIS construire les demandes en fonction du degré de généralité. Par exemple, si la thématique est
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
},
{
               instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                               répond au mieux en format JSON.",
               input: "C'est quoi la loi d'Ampère",
               output: {
                   "subject": "Electromag",
                   "topic": "Ampere"
               }
},
{
               instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                               répond au mieux en format JSON.",
               input: "Est ce qu une âme charitable pourrait juste m explique la méthode pour déterminer la direction des lignes de champs électriques",
               output: {
                   "subject": "Electromag",
                   "topic": "Ampere"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                  répond au mieux en format JSON.",
                input: "pour ce cas la prof nouq dit qui a une charge linéique mais c pas plutot une charge surfacique?"
                output: {
                    "subject": "Electromag",
                    "topic": "loadDistribution"
                  }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Quelqu’un est chaud en electromag ? Je comprends pas pourquoi quand z>e/2 on a un cylindre de hauteur e dans la zone chargée",
                output: {
                    "subject": "Electromag",
                    "topic": "loadDistribution"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Quand t'en cordonné polaire pour former un cylindre faut bien faire une rotation de 2pi nan ?",
                output: {
                    "subject": "Electromag",
                    "topic": "Ampere"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Quelqu'un sait faire Gausse ?",
                output: {
                    "subject": "Electromag",
                    "topic": "Gauss"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "on est d'accord que pour un file infinie, l'expression du champ électrostatique c'est ça",
                output: {
                    "subject": "Electromag",
                    "topic": "Ampere"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Sur les nb complexes, pour calculer l’argument d’un nb réel et imaginaire pur, après avoir mis l’angle, on met [pi] ou [2pi]? Ex:  arg(2i)=pi/2 [pi] ou [2pi] ? Il me semble plus logique que se soit [2pi] mais je ne sais pas pourquoi,",
                output: {
                    "subject": "Maths",
                    "topic": "ComplexeNumbers"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Comment une fonction peut être injective et surjective en même temps sachant qu'une fonction injective associe (en très gros c'est ce que j'ai compris) un y à un x au max et qu'une surjective peut associer plusieurs y à un x ? Toute injective est surjective ?",
                output: {
                    "subject": "Maths",
                    "topic": "Functions"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Comment on résout un système ?"
                output: {
                    "subject": "Maths",
                    "topic": "SystemResolution"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Salut, je bloque sur une question en maths. Est-ce que quelqu’un pourrait m’aider svp. J’ai posé u(x)=(3x-7)^4 et v(x)=racine de 4x-3. Et après j’ai dérivé avec la formule uv=u’v+uv’ mais j’aboutis a quelque de bizarre."
                output: {
                    "subject": "Maths",
                    "topic": "Derivatives"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "On est d'accord que (ln(kx))' avec k une constante ça donne k/x ?"
                output: {
                    "subject": "Maths",
                    "topic": "Derivatives"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "La négation de = c'est "différent" ?"
                output: {
                    "subject": "Maths",
                    "topic": "Logic"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Si une fonction est continue elle est forcément surjective ?"
                output: {
                    "subject": "Maths",
                    "topic": "Functions"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Du coup pour trouver un produit téléscopique, on doit définir une suite?"
                output: {
                    "subject": "Maths",
                    "topic": "Series"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "tu connais la formule de pascal?"
                output: {
                    "subject": "Maths",
                    "topic": "Analysis"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Est ce possible que la derivée soit negative et que la fonction soit croissante?"
                output: {
                    "subject": "Maths",
                    "topic": "Functions"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Pendant que l'on y est, c'est quoi le domaine de dérivabilité de arcsin(x) et de arctan(x) ?"
                output: {
                    "subject": "Maths",
                    "topic": "Functions"
                }
},
{
                instruction: "Tu es un analyseur de données chargé d'aider les étudiants à trouver des ressources,
                                répond au mieux en format JSON.",
                input: "Pourquoi arcsin(cos(x)) est dérivable sur ]0,pi[ alors que arccos(cos(x)) sur ]-1,0[U]0,1[ ?"
                output: {
                    "subject": "Maths",
                    "topic": "Functions"
                }
},


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
