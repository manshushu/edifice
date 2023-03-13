import numpy as np
from numpy.core.defchararray import array, count
from numpy.core.fromnumeric import sort
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

cs_content = pd.read_csv(
    "citeseer\\citeseer.content", sep="\t", header=None, low_memory=False
)
cs_cite = pd.read_csv(
    "citeseer\\citeseer.cites", sep="\t", header=None, low_memory=False
)
content = np.array(cs_content)
df_cite = pd.DataFrame(cs_cite)
dict_for_most_keywords_text = {}  # 这里面放的是每一行的关键词总数，每篇文章的关键词数
num_of_category = {"Agents": 0, "AI": 0, "DB": 0, "IR": 0, "ML": 0, "HCI": 0}
for i in content:
    if i[-1] == "Agents":
        num_of_category["Agents"] += 1
    if i[-1] == "AI":
        num_of_category["AI"] += 1
    if i[-1] == "DB":
        num_of_category["DB"] += 1
    if i[-1] == "IR":
        num_of_category["IR"] += 1
    if i[-1] == "ML":
        num_of_category["ML"] += 1
    if i[-1] == "HCI":
        num_of_category["HCI"] += 1
    # 被引越多次，关键词越多就说明他越受人人喜欢
    value1 = sum(i[1:-1])
    dict_for_most_keywords_text[str(i[0])] = value1

cited_num = df_cite[0].value_counts()
cited_num.to_dict()
X, Y = Counter(dict_for_most_keywords_text), Counter(cited_num)
z = dict(X + Y)
ans = sorted(z.items(), key=lambda item: item[1], reverse=True)
data_for_painting = dict(ans)

# data = {k: data_for_painting[k] for k in list(data_for_painting)[:5]}
# data={'1': 1056, '2': 426, '3': 186, '4': 95, 'kinny96methodology': 54}

data=num_of_category
plt.bar(data.keys(), data.values())
# plt.xlabel('Top 5 impact paper ID')
# plt.ylabel('Influence value')
plt.xlabel('Paper categories')
plt.ylabel('Total number of papers')
plt.show()

