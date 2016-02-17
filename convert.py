import cc_dat_utils
import cc_json_utils
import json



json_reader = open('data\jcossins_ccl.json', "r")
json_data = json.load(json_reader)
json_reader.close() #Close the file now that we're done using it
from_dat = cc_json_utils.make_cc_data_from_json(json_data)

print(from_dat)
