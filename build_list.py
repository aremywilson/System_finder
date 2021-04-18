from __future__ import print_function
import time
import swagger_client
import csv
import json
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UniverseApi(swagger_client.ApiClient())
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

system_ids = []
consortium = {}

with open("system_list.txt", 'r') as f:
	for line in f:
		if line[0] == '3':
			pizza = int(line.rstrip())
			info = {"sid": pizza, "name": "x", "sec_status": 11.01}
			consortium[pizza] = info

f.close()
#print(system_ids)
#pprint(consortium)

for system in consortium:
	try:
		# Get system info
		api_response = api_instance.get_universe_systems_system_id(datasource=datasource, system_id=system)

		# Populate system object
		consortium[system]['name'] = api_response['name']
		consortium[system]['sec_status'] = api_response['security_status']

		# Track calls progress
		if (system % 100 == 0):
			pprint(system + " out of 30045354 done")

	except ApiException as e:
		print("Exception when calling UniverseApi->get_universe_systems_system_id: %s\n" % e)


pprint(consortium)
save_json = json.dumps(consortium)
fw = open("system_info.json", "w")
fw.write(save_json)
fw.close()