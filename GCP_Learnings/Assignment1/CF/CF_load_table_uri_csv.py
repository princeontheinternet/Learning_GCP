# importing bigquery library to interact with BigQuery.
from google.cloud import bigquery
import logging

# Set the logging level to INFO.
logging.getLogger().setLevel(logging.INFO)


def load_csv_to_bigquery():


    bq_client = bigquery.Client()   #creates a client object that we can use to connect to BigQuery and interact with it. Here, Client is a cls
    job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("FirstName", "STRING"),
        bigquery.SchemaField("LastName", "STRING"),
        bigquery.SchemaField("DOB", "DATE"),
    ],
    skip_leading_rows=1,        # Skip the header row
    
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
    )

    table_id = "tactical-grid-384204.demo.mytable"


    uri = "gs://emp-details/data.csv"

    load_job = bq_client.load_table_from_uri(
    uri, table_id, job_config=job_config
    )


    load_job.result()  # Waits for the job to complete.

    destination_table = bq_client.get_table(table_id)

    logging.info("Loaded {} rows.".format(destination_table.num_rows))
    return f'check the results in the logs'
