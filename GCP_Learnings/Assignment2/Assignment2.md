# Create a file in Cloud Shell and load it into GCS Bucket and then to BigQuery table using gsutil and bq commands

## Step1

- Open Cloud Shell Editior and run the following Commands.

    ```sh
    mkdir first_csv_directory
    cd first_csv_directory/
    vi mycsv_file.csv
    ```

- Add the below data to mycsv_file.csv

    ```csv
    Name, Age, Gender
    John, 25, Male
    Jane, 30, Female
    Janet, 35, Female
    ```

- Make the Bucket using gsutil

    **Note**: _We can use gsutil for data transfer upto **1 TB.**_

    ```sh
    gsutil mb gs://bucket_created_using_cloud_shell
    ```

- Copy the CSV to the newly created bucket

    ```sh
    gsutil cp mycsv_file.csv gs://bucket_created_using_cloud_shell
    ```

- Load into the destination table.
(Note: Table will be created using the below command itself.)

    ```sh 
    bq load --autodetect --source_format=CSV tactical-grid-384204:demo.table_created_using_cloud_shell gs://bucket_created_using_cloud_shell/mycsv_file.csv
    ```

### Extras

- You can directly load table from the file created on cloud Shell.

    ```sh
    bq load --autodetect --source_format=CSV tactical-grid-384204:demo.new_table mycsv_file.csv
    ```

- You can also create dataset & table from cloud Shell.

    ```sh
    # Create dataset
    bq mk my_dataset 

    bq mk --table --schema Name:STRING,Age:INTEGER,Gender:STRING tactical-grid-384204:demo.new_table_created_using_cloud_shell
    ```

- You can also query from cloud shell.

    ```sh
    # we can use --use_legacy_sql=false or --nouse_legacy_sql
    bq query --nouse_legacy_sql \
    'SELECT
    COUNT(*)
    FROM
    `tactical-grid-384204`.demo.new_table'

    bq query "select * from  demo.new_table"
    ```
