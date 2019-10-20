import pandas as pd
import FeatureExtractor as fe
from sklearn.feature_extraction.text import TfidfVectorizer
from pandas.io.json import json_normalize

df = pd.read_csv("stripped_data.csv")

df['ingredients'] = df['ingredients'].apply(lambda x: str(x))
df['ingredients'] = df['ingredients'].apply(fe.CleanUp)

# Jing

#change column 'country' from str to number
country_lst = df['country'].tolist()
dic = dict()
i = 0
for x in country_lst:
    if x not in dic:
        dic[x] = i
        i = i + 1

df['country'] = df['country'].apply(lambda x: dic.get(x))

#remove 'Brand' in column 'company'
df['company'] = df['company'].apply(lambda x: x.split()[1])

# drop column 'unit_pack_size_ml_g', since it's not related actual price
df = df.drop('unit_pack_size_ml_g', axis=1)
# df = df.drop('total_pack_size_ml_g', axis=1)

#change column 'price_per_100g_ml_dollars' to 'actual_price'
df['price_per_100g_ml_dollars'] = df['total_pack_size_ml_g'] / 100 * df['price_per_100g_ml_dollars']
df.rename(columns={'price_per_100g_ml_dollars': 'actual_price'}, inplace=True)

df = df.drop('country', axis=1)
df = df.drop('company', axis=1)


#Jing

df2 = json_normalize(df['ingredients'])
for column in df2:
    total = df2[column].sum()
    if(total < 2):
        df2 = df2.drop(column, axis=1)
# df2 = pd.DataFrame(abc.toarray(), columns=vectorizer.get_feature_names())
df = df.drop(['ingredients'], axis = 1)
df = df.join(df2, how = 'outer')
df = df.fillna(0)
df['price'] = df['actual_price']
df = df.drop(['actual_price'], axis = 1)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]



df.to_csv('final2.csv')
