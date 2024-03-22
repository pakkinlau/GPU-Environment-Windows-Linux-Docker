from gpt4all import GPT4All
model = GPT4All("./models/nous-hermes-llama2-13b.Q4_0.gguf")
# model = GPT4All("orca-2-13b.Q4_0.gguf")
output = model.generate("The capital of France is ", max_tokens=3)
print(output)