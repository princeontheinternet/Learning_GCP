from google.cloud import bigquery
import json

def retrieve_table_data(request):
    if request.method == 'POST' and request.get_json() is not None:

        client = bigquery.Client()

        table_name = request.get_json().get('table_name')
        column_name = request.get_json().get('column_name')
        column_value = request.get_json().get('column_value')

        query = f"SELECT * FROM `{table_name}` WHERE {column_name} = '{column_value}'"

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


# JSON Param
# {
#   "table_name": "tactical-grid-384204.demo.new_table",
#   "column_name": "Name",
#   "column_value": "Janet"
# }