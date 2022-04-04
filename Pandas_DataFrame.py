#Pandas DataFrame
import pandas as pd
data = {'Name':['Jubeen', 'Barath', 'Klinton', 'Saam'],
        'Age':[20, 20, 21, 20],
        'Address':['Tiruppur', 'Chennai', 'Cuddalore', 'North India'],
        'Qualification':['BCA', 'BCA', 'BCA', 'BCA']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name','Qualification', 'Address']])
