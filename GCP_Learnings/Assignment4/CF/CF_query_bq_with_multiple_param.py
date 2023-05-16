from google.cloud import bigquery
import json

def retrieve_table_data(request):
    if request.method == 'POST' and request.get_json() is not None:

        client = bigquery.Client()

        table_name = request.get_json().get('table_name')
        column_name = request.get_json().get('column_name')
        column_value = request.get_json().get('column_value')

        column_value = [f"'{each_value}'" for each_value in column_value]

        query = f"SELECT * FROM `{table_name}` WHERE {column_name} in ({', '.join(column_value)})"

        rows = client.query(query).result()

        results = []
        for row in rows:
            row_dict = dict(row)
            results.append(row_dict)
        json_results = json.dumps(results)

        # Return results as JSON response
        return json_results
    else:
        return 'Invalid request'
    

# JSON PARAM
# {
#   "table_name": "tactical-grid-384204.demo.new_table",
#   "column_name": "Name",
#   "column_values": ["Janet", "John", "Alice"]
# }


# requirements.txt
# google-cloud-bigquery==3.3.1