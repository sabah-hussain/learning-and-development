import csv
from datetime import datetime
from google.cloud import bigquery

def transform_date(date_str):
    old_date = datetime.strptime(date_str, '%Y-%m-%d')
    transformed_date = old_date.strftime('%d-%m-%Y')
    return transformed_date

file_path = '/Users/sabahhussain/learning_development/CSV_files/people_100.csv'

transformed_data = []
with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        row['Date of birth'] = transform_date(row['Date of birth'])
        transformed_data.append(row)

client = bigquery.Client()

table_id = 'dt-sabah-sandbox-dev.load_with_transformations.people_100_sample'

schema = [
    bigquery.SchemaField('Index', 'INTEGER', mode='NULLABLE'),
    bigquery.SchemaField('User Id', 'STRING', mode='NULLABLE'),
    bigquery.SchemaField('First Name', 'STRING', mode='NULLABLE'),
    bigquery.SchemaField('Last Name', 'STRING', mode='NULLABLE'),
    bigquery.SchemaField('Sex', 'STRING', mode='NULLABLE'),
    bigquery.SchemaField('Email', 'STRING', mode='NULLABLE'),
    bigquery.SchemaField('Phone', 'STRING', mode='NULLABLE'),
    bigquery.SchemaField('Date of birth', 'DATE', mode='NULLABLE'),
    bigquery.SchemaField('Job Title', 'STRING', mode='NULLABLE')
]

job_config = bigquery.LoadJobConfig(
    schema=schema,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1
)

# Load the transformed data into BigQuery table
load_job = client.load_table_from_file(
    transformed_data,
    table_id,
    job_config=job_config
)

load_job.result()  # Wait for the job to complete
print(f"Data loaded into {table_id} with transformations")
