import json

with open("DataForgeConfig.json", "r", encoding="utf-8") as file:
    config = json.load(file)


def get_prompt(subject):
    return '''
    Act as a data parser with those 3 elements: "instructions, input and output\n"
    Instruction will always be the same: \"You are a data parser aim to help students finding resources, answer with a
    json format as best as possible."\n
    Input will be something that a student need for their study. It could be formulated as a sentence or a question.
    In any case, it should looks like a request that a student could ask, for example : "I need help with
    mathematics""\n
    You can adopt any structure you like to build the request."\n
    Student requests MUST ONLY be about the topics and the subjects that are present in the dictionary: %s (the key is
    the subject and the value is the topics list)""
    The subject you will be tackling now is: %s.
    Here are some examples of structure for sentence starting that could be used:"\n
    Could you please help me to,
    I'm struggling to,
    I'm not sure how to,
    Can you help me to improve,
    I'm stuck on,
    I'm having trouble with,
    Do you have any tips for,
    Could you give me some advice on"\n
    Gather some concepts from the subjects and topic lists and build requests according them. The requests MUST only be
    about them. It's very important !! "\n
    If the topic name is in an output (for example: "I need help in algebra"), try your best to add a concept in that
    topic or be specific in the request."\n
    You MUST NOT create requests that are too general.\n
    output should be an answer to the input as a JSON format.\n"
    \nGive me a JSON format that is an array of EXACTLY %s lines (instructions,inputs,outputs) this way:"
    [
             {
                instruction: "You are a data parser aim to help students finding resources, answer with a json format
                as best as possible.",
                input: "I need help with mathematics",
                output: {
                    "topic": ...,
                    "subject": ...
                }
            },
            {
                instruction: "You are a data parser aim to help students finding resources, answer with a json format as
                best as possible.",
                input: "I need to understand better matrices  ",
                output: {
                    "topic": ...,
                    "subject": ...
                }
            }
    ]
    \n
    The subject and the topic MUST be the same as the written ones in the dictionary %s.

    IMPORTANT: DO NOT give same example twice, it should be unique. Only the input and instruction should be in french.
    ''' % (config["themes_dict"], subject, config["nb_observations"], config["themes_dict"])
