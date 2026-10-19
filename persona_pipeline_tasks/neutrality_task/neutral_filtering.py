from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from pathlib import Path
import json
import os
import random
import argparse

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini")
json_data = {}
user_description = {}
relative_path = Path("wusef_task/summer_research/user_description_sample.json")
   
   

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You filter users and determine their neutrality. Make as little assumptions as possible. I will give you a question: {filtering_questions} and You need to return an answer that you assume the user would give. When you return an answer give explanations and end the response with a defninitve Neutral or Not Neutral filter for the user. Give a json as output in the form: '{{\"neutrality\": \"your answer\", \"user\": \"Give the username\", \"reasoning\": \"Explain why this determination was made\"}}'\nUser description:\n\n{userDes}")
# ])

# feed the comments in directly -> ask the 
prompt = ChatPromptTemplate.from_messages([
    ("system", "You filter users and determine their neutrality. Make as little assumptions as possible. I will give you a question: {filtering_questions} and You need to return an answer that you assume the user would give. When you return an answer give explanations and end the response with a defninitve Neutral or Not Neutral filter for the user. Give a json as output in the form: '{{\"user\": \"Give the username\", \"neutrality\": \"your definitive answer\", \"reasoning\": \"Explain why this determination was made\"}}'\nUser description:\n\n{userDes}")
])

llm_chain = prompt | llm

filtering_questions = ['Does the user have certain hobbies that point to a certain political standing?']
# other questions: 
# , 'Do you think this user is able to make important decisions outside of their beliefs? Why or why not. Explicitly answer with a political standing'

def get_user_neutrality(user_description):
    result = llm_chain.invoke({"userDes": user_description,  "filtering_questions": filtering_questions})
    return result

def process_user_info(file_path, num_choices=100):
    with open(relative_path, 'r') as f:
        user_description = json.load(f)
    usernames = list(user_description.keys())
    results = []
    
    for _ in range(num_choices):
        selected_user = random.choice(user_description[random.choice(usernames)])
        result = get_user_neutrality(selected_user)
        # print("\nAnalysis Result:") 
        try:
            result_json = json.loads(result.content)
            results.append(result_json)
            # print(json.dumps(result_json))
        except json.JSONDecodeError:
            print("Error printing result: {result}")
    return results
    
def main():
    # selected_user = random.choice(user_description["donald"])
    parser = argparse.ArgumentParser(description="Analyze user neutrality based on provided JSON data.")
    parser.add_argument("file", type=str, help="Path to the user description JSON file")
    args = parser.parse_args()
    results = process_user_info(args.file, num_choices=100)
    print("\nAnalysis Results:")
    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()