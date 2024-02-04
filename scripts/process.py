import pandas as pd


def read_and_process_csv(file_path):
    # Read CSV with multi-level columns, keeping only the second row of headers
    df = pd.read_csv(file_path, header=[0, 1])
    df.columns = [col[1] for col in df.columns.values]  # Simplify columns to second row
    return df.iloc[:, :2], df.select_dtypes(
        include=["number"]
    )  # Split geographic and numeric data


# Paths of the CSV files
file_paths = [
    "data/Small_Neighbourhood_COICOP3_LCFS.csv",
    "data/Small_Neighbourhood_COICOP3_OAC.csv",
    "data/Small_Neighbourhood_COICOP3_TransUnion.csv",
]

# Process each CSV file and unpack results
geographic_info, numeric_dfs = zip(*(read_and_process_csv(path) for path in file_paths))

# Assuming geographic info is consistent, use the first file's data, removing duplicates
geographic_info_df = pd.concat(geographic_info).drop_duplicates().reset_index(drop=True)

# Calculate the average of numeric columns across all DataFrames
average_df_numeric = pd.concat(numeric_dfs).groupby(level=0).mean()

# Combine geographic info with the averaged numeric data, handling NaN values by filling with 0
average_df = pd.concat(
    [geographic_info_df.iloc[:, :2], average_df_numeric], axis=1
).fillna(0)

# Remove the first column
average_df = average_df.iloc[:, 1:]

# Remove the first row
average_df = average_df.iloc[1:, :]

# Save the result to a new CSV file
average_df.to_csv("output/Average_COICOP3.csv", index=False)

print(
    "The average values have been calculated and saved to 'output/Average_COICOP3.csv'."
)
