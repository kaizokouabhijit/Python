import os


env_var = os.environ
os.environ["Test"] = "Testing"

print(env_var["Test"])