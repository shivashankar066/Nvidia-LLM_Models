from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = ""
)

completion = client.chat.completions.create(
  model="nvidia/nemotron-4-340b-reward",
  messages=[{"role":"user",
             "content":"Instruct me how to build django API for my project?"},
            {"role":"assistant",
             "content":"Give me essential code"}],
)
print(completion)
