"""Script for summarize the vpc flow log"""

import csv
import json


def get_requests_per_ip():
    with open("./vpc-flow-logs.csv") as csv_input, open("./output_requests_ips.json", "w") as output_file:
        # Variables initiation
        ip_data_requests = {}
        csv_content = csv.reader(csv_input)

        next(csv_content)  # Skip of column names row.

        for row in csv_content:
            srcip = row[3]  # Get third column, that contains the srcip.

            # In case that the ip is already registered in the json, we add 1 to the amount of requests.
            # Otherwise, we create the ip and assign one to the amount of requests.
            if ip_data_requests.get(srcip):
                ip_data_requests[srcip] += 1
            else:
                ip_data_requests[srcip] = 1

        output_file.write(
            json.dumps(ip_data_requests)
        )  # Output file with the amount of requests per ip.


if __name__ == "__main__":
    get_requests_per_ip()