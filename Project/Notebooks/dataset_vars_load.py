import pandas as pd
from sklearn.model_selection import train_test_split

#Load the dataframe first 200 rows
data = pd.read_csv('../Dataset/preprocessed_dataset.csv', usecols=['text','label1'], nrows=200)
data = data.rename(columns={'label1': 'label'})

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data["text"], data["label"], test_size=0.2, random_state=42)
