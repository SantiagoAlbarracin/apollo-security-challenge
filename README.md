# Apollo Security Challenge

This repository contains the solution to the security scripting challenge presented by Apollo.io.

## Usage
To execute the challenge script, run the Python script `security_scripting_challenge.py`. After completion, you'll find the generated output file named `output_requests_ips.json`, containing information on the number of requests per source IP.

Additionally, as part of the provided solution, the source IP involved in the incident must be blocked via API. In this case, the source IP `181.31.10.13` has been successfully blocked via API. You can review the details of this action in the file `blocked_ip_post.jpg`.


---

### Sequence diagram
![sequence_diagram](https://github.com/SantiagoAlbarracin/apollo-security-challenge/assets/63375461/51ec126a-a871-4ea6-b44d-f5137404ad7d)

## Enhancements

This script can be improved by adding new steps in the future.
We can do the following:

1- Number of requests for source port and IP, to which port and destination IP.
2- Timestamp control to know the number of requests at a certain time. This way you can control that it is not a bot that triggers the requests.
3- Reputation verification of destination IPs.


---

**Contact Information:**

Santiago Albarracin  
Email: [snalbarracin@live.com](mailto:snalbarracin@live.com)
