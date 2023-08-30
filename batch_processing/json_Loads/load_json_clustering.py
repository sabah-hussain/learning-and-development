from google.cloud import bigquery

client = bigquery.Client()

table_id = "dt-sabah-sandbox-dev.load_json_clustering.Birthdays"
file_path = "/Users/sabahhussain/learning_development/batch_processing/json_files/birthdays.json"

schema = [
    bigquery.SchemaField('Name', 'STRING'),
    bigquery.SchemaField('Age', 'INTEGER'),
    bigquery.SchemaField('Date', 'DATE')
]

clustering_fields = ['Date']

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    schema=schema,
    clustering_fields=clustering_fields
)

with open(file_path, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config
    )
    
load_job.result()  # Wait for the job to complete
print("Data loaded successfully!")