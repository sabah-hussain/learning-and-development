def generate_file_table_pairs(*args):
    file_table_pairs = []
    for file, table in args:
        file_table_pairs.append((
            f"/Users/sabahhussain/learning_development/batch_processing/csv_files/{file}",
            f"dt-sabah-sandbox-dev.{table}"
        ))
    return file_table_pairs

file_table_pairs = generate_file_table_pairs(
    ("Planets.csv", "dummy_dataset.Planets"),
    ("nutrition.csv", "dummy_dataset.Nutrition"),
    ("WorldPopulation2023.csv", "dummy_dataset.World_Population"),
    ("earning.csv", "dummy_dataset.Earnings"),
    ("efw_cc.csv", "dummy_dataset.Economic_Freedom_of_the_World"),
    ("significant_earthquakes.csv", "dummy_dataset.Significant_Earthquakes"),
    ("SampleforOrders.csv", "dummy_dataset.Orders"),
    ("mock_orders.csv", "dummy_dataset.mock_orders"),
    ("njord_csv_sample.csv", "dummy_dataset.njord_csv_sample"),
    ("people_100.csv", "dummy_dataset.people_sample"),
    ("people_account_type.csv", "data_for_joins.people_account_types"),
    ("people_credit_check.csv", "data_for_joins.people_credit_check")
)
