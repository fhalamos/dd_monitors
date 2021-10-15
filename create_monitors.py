def create_monitor_json(resource_str):
	with open('monitor_template.json', 'r+') as template_file:
	    content = template_file.read()
	    template_file.seek(0)
	    content = content.replace("<resource>", resource_str)
	    outfile_name = f"{resource_str.replace('/','')}.json"
	    with open(outfile_name, 'w+') as outfile:
	    	outfile.write(content)

def create_all_monitor_jsons(resources_file_path):
	with open(resources_file_path) as resources_file:
		for line in resources_file:
			line = line.strip()
			create_monitor_json(line)

if __name__ == '__main__':
	create_all_monitor_jsons('resources_list.txt')