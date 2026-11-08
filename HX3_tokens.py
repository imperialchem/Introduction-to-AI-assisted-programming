# This script is used to generate access tokens to the HX3 cluster.

import urllib.request
import urllib.parse
import json

# add you Access Key information here
runai_client_id=
runai_client_secret=

data = {
    "grantType": "client_credentials",
    "clientId": runai_client_id,
    "clientSecret": runai_client_secret
}

request = urllib.request.Request(
    "https://runai.hx3.hpc.ic.ac.uk/api/v1/token",
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(request) as response:
    token = json.loads(response.read().decode("utf-8"))["accessToken"]

print(token)