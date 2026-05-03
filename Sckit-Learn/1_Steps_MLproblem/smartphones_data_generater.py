import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)


#----------------------------------------


# Define the number of rows for  training/test data(80% , 20% of total data)
no_rows = 1000
train_data_row = 800                       
test_data_row = no_rows - train_data_row          # Remaining rows for test data


#----------------------------------------


# Generate data

train_data = {
    'camera': np.random.randint(8, 201, size=train_data_row),         # Megapixels (8 to 200)
    'age': np.random.randint(0, 4, size=train_data_row),              # Age in years (0 to 3)
    'ram': np.random.choice([4, 6, 8, 12, 16], size=train_data_row),  # RAM in GB
    'cpu_score': np.random.randint(40, 101, size=train_data_row),     # CPU benchmark score (40 to 100)
    'slot_sd': np.random.randint(0, 2, size=train_data_row),          # SD card slot (0 = no, 1 = yes)
    'sims': np.random.choice([1, 2], size=train_data_row),            # Number of SIMs
    'price': np.random.randint(8000, 70001, size=train_data_row)      # Price in INR (₹8,000 to ₹70,000)
}

test_data = {
    'camera': np.random.randint(8, 201, size=test_data_row),             # Megapixels (8 to 200)
    'age': np.random.randint(0, 4, size=test_data_row),                  # Age in years (0 to 3)
    'ram': np.random.choice([4, 6, 8, 12, 16], size=test_data_row),      # RAM in GB
    'cpu_score': np.random.randint(40, 101, size=test_data_row),         # CPU benchmark score (40 to 100)
    'slot_sd': np.random.randint(0, 2, size=test_data_row),              # SD card slot (0 = no, 1 = yes)
    'sims': np.random.choice([1, 2], size=test_data_row),                # Number of SIMs
    'actual_price': np.random.randint(8000, 70001, size=test_data_row),  # actualPrice in INR (₹8,000 to ₹70,000)
    'predicted_price': 0 ,                                               # predictedPrice by MODEL in INR  
    'error': 0                                                           # error = actualPrice - predictedPrice
}



#----------------------------------------


# Create DataFrame
df1 = pd.DataFrame(train_data)
df2 = pd.DataFrame(test_data)


#----------------------------------------

# Save to CSV (optional)
df1.to_csv("Sckit-Learn\\1_Intro\\smartphone_train_data.csv", index=False)
df2.to_csv("Sckit-Learn\\1_Intro\\smartphone_test_data.csv", index=False)


# Create 80-20 train-test split -> 80percent data = Train data, 20percent data = Test data 


#----------------------------------------


# Display first few rows
print(df1.head())
print(df2.head())
 