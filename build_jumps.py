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


system_info = {}
# Import system info from file
with open("system_info.json", 'r') as system_json:

    system_info = json.load(system_json)
    #pprint(galaxy)

system_json.close()
pprint("system_info.json closed")


# Get jumps data
jump_list = {}
try:
    api_response = api_instance.get_universe_system_jumps(datasource=datasource, if_none_match=if_none_match)

    for response in api_response:
        jump_list[response["system_id"]] = response["ship_jumps"]

    #pprint(jump_list)


except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_constellations: %s\n" % e)

pprint("API call completed")

# Store jumps data in system index and fill in zeros
galaxy_jumps = {}

for system in system_info:
    #pprint(system, jump_list[system])
    idx = int(system)
    if idx in jump_list:
        jump_num = jump_list[idx]
        galaxy_jumps[idx] = [jump_num]
    else:
        galaxy_jumps[idx] = [0]


pprint(galaxy_jumps)
save_json = json.dumps(galaxy_jumps)
fw = open("jumps_info.json", "w")
fw.write(save_json)
fw.close()
