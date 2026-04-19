import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

r = requests.get(r'http://api.cquest.org/dvf?code_commune=35152&nature_mutation=Vente&type_local=Maison')
data = json.loads(r.text)

# with open('data.json', 'w') as f:
#     print(r.text)
#     f.write(r.text)

list_transactions = pd.DataFrame(data["resultats"])

