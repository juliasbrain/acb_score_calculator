
def acb_score(medication_df, output_dir=None):
    """
    Function to calculate the Anticholinergic Burden of medication (ACB) for each patient based on their medication data.
    The ACB scores are sourced from the Anticholinergic Burden (ACB) Calculator available at: https://www.acbcalc.com/

    Args:
        medication_df (pd.DataFrame): A pandas DataFrame containing patient medication data with the following format:
            - 'Subject_ID': Unique identifier for each patient.
            - Other columns: Medication names and doses for each session, formatted as "Medication: dose".
        
        output_dir (str, optional): Directory to save the resulting ACB score dataframe. 
            If None, the output will be saved to the current directory.

    Returns:
        pd.DataFrame: A dataframe with columns:
            - 'Subject_ID': Unique identifier for each patient.
            - 'acb_score_total': Total ACB score for each patient.
    """

    import os
    import pandas as pd
    import numpy as np

    # Load the ACB score data
    acb_data = pd.read_csv(os.path.join(os.path.realpath('.'), 'acb_list.csv'))

    # Prepare Input dataframe
    df = medication_df.copy()
    df.iloc[:, 1] = df.iloc[:, 1].fillna("0: 0")  # Set zero for patients without medication
    df = df.melt(id_vars='Subject_ID', var_name='Medication', value_name='medication')  # Create longitudinal df
    df[['medication', 'dose']] = df['medication'].str.split(': ', expand=True)  # Split 'medication' and 'dose'
    df = df.drop(columns=['Medication', 'dose']).dropna(subset=['medication']).loc[df['medication'].str.strip() != '']  # Clean up rows
    df['Subject_ID'] = df['Subject_ID'].str.strip()  # Remove whitespaces
    df['medication'] = df['medication'].str.capitalize()  # Capitalize first letter


    # Calculate ACB Score
    df = df.merge(acb_data[['medication', 'acb_score']], on='medication', how='left')
    df['acb_score_total'] = df.groupby('Subject_ID')['acb_score'].transform('sum')
    df = df.drop_duplicates(subset='Subject_ID').reset_index(drop=True)
    df = df.drop(columns=['medication', 'acb_score'])

    # Set output directory to current directory if not specified
    if not output_dir:
        output_dir = os.getcwd()

    # Save output as CSV
    output_path = os.path.join(output_dir, 'medication_acb.csv')
    df.to_csv(output_path, index=False)

    return df