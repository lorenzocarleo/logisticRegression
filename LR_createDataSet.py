import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Simulate data for 1000 customers
n_customers = 1000

# Features
data = {
    'CustomerID': range(1, n_customers + 1),
    'Gender': np.random.choice(['Male', 'Female'], n_customers),
    'Age': np.random.randint(18, 70, n_customers),
    'Tenure': np.random.randint(1, 72, n_customers),  # 1 to 71 months
    'ServiceType': np.random.choice(['Phone', 'Internet', 'Both'], n_customers),
    'MonthlyCharges': np.random.uniform(20, 120, n_customers),
    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_customers),
    'PaperlessBilling': np.random.choice(['Yes', 'No'], n_customers),
    'PaymentMethod': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n_customers),
    'OnlineSecurity': np.random.choice(['Yes', 'No'], n_customers),
    'TechSupport': np.random.choice(['Yes', 'No'], n_customers),
    'StreamingTV': np.random.choice(['Yes', 'No'], n_customers),
    'StreamingMovies': np.random.choice(['Yes', 'No'], n_customers)
}

# DataFrame
df = pd.DataFrame(data)

# Calculate TotalCharges (somewhat correlated with Tenure and MonthlyCharges)
df['TotalCharges'] = df['MonthlyCharges'] * df['Tenure'] + np.random.uniform(0, 100, n_customers)

# Target Variable: Churn
# Assume churn rate is around 20%
df['Churn'] = np.random.choice(['Yes', 'No'], n_customers, p=[0.2, 0.8])

#df.head(5)  # Display the first few rows of the DataFrame

print(df)

# Saving the DataFrame to a CSV file
csv_file_path = 'customer_churn_dataset.csv'  # Specify the file path and name
df.to_csv(csv_file_path, index=False)




