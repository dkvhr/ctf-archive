extends Control

var points_label
var owned_label
var bought_label
var poor_label
var flag_label

func _ready():
	points_label = get_node("pointsLabel")
	owned_label = get_node("ownedLabel")
	bought_label = get_node("boughtLabel")
	poor_label = get_node("poorLabel")
	flag_label = get_node("flagLabel")
	points_label.text = "POINTS: " + str(Global.points)
	owned_label.visible = false
	bought_label.visible = false
	poor_label.visible = false
	
func _on_Main_Menu_pressed():
	get_tree().change_scene_to(load("res://MainScene.tscn"))

func _on_Buy_pressed():
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.connect("request_completed", self, "_on_request_completed")
	var headers = ["Content-Type: application/json", "Authorization: " + Global.auth_token]
	var error = http_request.request(Global.url + "/verify?value=" + str(Global.points), headers)
	print(headers)
	print(Global.url + "/verify?value=" + str(Global.points))
	if error != OK:
		pass
		
		
func _on_request_completed(result, response_code, headers, body):
	
	
	
	

	if response_code == 200:
		
		var json = JSON.parse(body.get_string_from_utf8())
		if json.error == OK:
			
			var message = json.result["message"]
			if not Global.has_drippy:
				if Global.points >= 73317331 and "flag" in message:
					flag_label.text = message
					Global.has_drippy = true
					bought_label.visible = true
					yield (get_tree().create_timer(3.0), "timeout")
					bought_label.visible = false
				else :
					poor_label.visible = true
					yield (get_tree().create_timer(3.0), "timeout")
					poor_label.visible = false
			else :
				if "flag" in message:
					flag_label.text = message
				owned_label.visible = true
				yield (get_tree().create_timer(3.0), "timeout")
				owned_label.visible = false
		else :
			pass
			
	else :
		pass
		
