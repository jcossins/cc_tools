def make_cc_data_from_json(json_data):
	cc_data_object = cc_data.CCDataFile()
	for json_level in json_data:
		cc_level = cc_data.CCLevel()
		#initialize cc_level's data from json_level data
		#this involves setting the level_number, time, num_chips
		#upper_layer, and lower_layer
		for json_field in json_level["optional_fields"]:
			#look at the "type" value of the json_field
			#make the appropriate Field based on the type and data
			cc_field = make_cc_field_from_json(jcossins_ccl.json)
			cc_level.add_field(cc_field)

		cc_data_object.add_level(cc_level)
	return cc_data_object