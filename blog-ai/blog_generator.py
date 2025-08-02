import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("API_KEY")
print(openai.api_key)


def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-4o-mini',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 200,
    temperature = 0.5
  )

  retrieve_blog = response.choices[0].text

  return retrieve_blog

print(generate_blog("The best programming language for beginners"))

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. \n Enter your answer: ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about?\n Enter a topic: ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False



"""client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)"""

"""
client = OpenAI(
    ai_api_key = os.getenv("ai_apiKey")
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
"""