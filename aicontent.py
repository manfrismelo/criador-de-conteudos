import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY

response = openai.Completion.create(
  model="davinci-instruct-beta",
  prompt="Generate a detiled product description for: {}.format(query),",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)