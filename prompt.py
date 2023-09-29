prompt = ''' 
Act as a data parser with those 3 elements: "instructions, input and output\n" 
instruction will always be the same: \"You are a data parser aim to help students finding ressources, answer with a json format as best as possible."\n 
input will be something that a student need for their study, example: "I need help with mathematics"\n 
output should be an answer to the input as a JSON format.\n" 
\nGive me a JSON format that is an array of hundreds of instruction,input,output this way:" 
[
         {
            instruction: "You are a data parser aim to help students finding ressources, answer with a json format as best as possible.",
            input: "I need help with mathematics",
            output: {
                "topic": "maths",
                "subject": "general"
            }
        },
        {
            instruction: "You are a data parser aim to help students finding ressources, answer with a json format as best as possible.",
            input: "I need to understand better matrices  ",
            output: {
                "topic": "maths",
                "subject": "matrices"
            }
        }
]

IMPORTANT: Don't give same example twice, it should be unique.
'''