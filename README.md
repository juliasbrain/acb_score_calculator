# ACB Score Calculator

This Python tool calculates the Anticholinergic Burden (ACB) score for patients based on their medication.


## Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/juliasbrain/acb_score_calculator.git
cd acb_score_calculator
pip install -r requirements.txt
```

## Usage

### Input:
The function requires a DataFrame containing patient medication data in the following format:

- **'Subject_ID'**: A unique identifier for each patient.
- **Other columns**: Medication names and doses for each session, formatted as `"Medication: dose"`. Each column represents a different medication for each session.

Example:
```python
medication_df = pd.DataFrame({
    'Subject_ID': ['subject1', 'subject2'],
    'Medication_1': ['med1: 5mg', 'med2: 10mg'],
    'Medication_2': [None, 'med3: 2mg']
})
```

### Output:
The function generates a CSV file with the following columns:
- **'Subject_ID'**: A unique identifier for each patient.
- **'acb_score_total'**: The total ACB score for each patient, calculated based on the medications provided.

The CSV file will be saved in the specified output directory (or the current directory if not specified).

### Running the Function:

1. Import the function from the script:
```python
from acb_score import acb_score
```

2. Load the medication data:
```python
medication_df = pd.read_csv(/path/to/medication_df/medication_df.csv')
```
   
3. Calculate ACB scores
```python
acb_score(medication_df, output_dir='./output')  # Optional: Specify output directory
```
   
## Data Source

The ACB scores used in this repository are sourced from the Anticholinergic Cognitive Burden (ACB) Calculator available at:

https://www.acbcalc.com/

For more details on how the ACB scores are calculated, please refer to the official website.
