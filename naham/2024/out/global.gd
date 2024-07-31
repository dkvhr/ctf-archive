extends Node

const DEFAULT_VALUE = 0


var initial_points


var points

var has_drippy = false

var url:String = "http://209.38.153.254:8888"

var auth_token = ""


func _ready():
	
	var saved_value = load_saved_value()
	if saved_value != null:
		initial_points = saved_value
		points = saved_value
	else :
		points = DEFAULT_VALUE
		write_to_local_storage(DEFAULT_VALUE)
		
	
	register()
	
	

func register():
	
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.connect("request_completed", self, "_on_request_completed1")
	var headers = ["Content-Type: application/json"]
	var error = http_request.request(url + "/register", headers, false, HTTPClient.METHOD_POST, "")
	if error != OK:
		pass
		
			

func save():
	
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.connect("request_completed", self, "_on_request_completed2")
	var headers = ["Content-Type: application/json", "Authorization: " + auth_token]
	var post_data = {
		"value":initial_points
	}
	
	var error = http_request.request(url + "/save", headers, false, HTTPClient.METHOD_POST, JSON.print(post_data))
	if error != OK:
		pass
		

func load_saved_value():
	
	var file = File.new()
	if file.file_exists("user://saved_value.dat"):
		if file.open("user://saved_value.dat", File.READ) == OK:
			var saved_value = file.get_as_text().strip_edges().to_int()
			file.close()
			return saved_value
		else :
			
			
			return null
	else :
		
		return null

func write_to_local_storage(value):
	
	save_value(value)

func save_value(value):
	
	var file = File.new()
	if file.open("user://saved_value.dat", File.WRITE) == OK:
		file.store_line(str(value))
		file.close()
	else :
		
		print("Error: Unable to open file for saving.")
		
func _on_request_completed1(result, response_code, headers, body):
	
	
	
	

	if response_code == 200:
	
		
		
		
		

		if response_code == 200:
			
			var json = JSON.parse(body.get_string_from_utf8())
			if json.error == OK:
				
				
				auth_token = json.result["auth_token"]
				save()
			else :
				pass
				
		else :
			
			var json = JSON.parse(body.get_string_from_utf8())
			if json.error == OK:
				pass
				
			else :
				pass
				
	else :
		pass
		

func _on_request_completed2(result, response_code, headers, body):
	
	
	
	

	if response_code == 200:
	
		
		
		
		

		if response_code == 200:
			
			var json = JSON.parse(body.get_string_from_utf8())
			if json.error == OK:
				pass
				
			else :
				pass
				
		else :
			
			var json = JSON.parse(body.get_string_from_utf8())
			if json.error == OK:
				pass
				
			else :
				pass
				
	else :
		pass
		
