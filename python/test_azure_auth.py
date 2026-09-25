from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()

print("Azure credential criada com sucesso!")
print(type(credential))