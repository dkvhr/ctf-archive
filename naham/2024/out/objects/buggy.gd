extends RigidBody2D

var jump_strength = - 750.0

var tilt_velocity = 5.0

var can_input = true

var score_timer
var score_label
var game_over_label
var play_again_button

var score = 0


func _ready():
	score_timer = get_node("../ScoreTimer")
	score_label = get_node("../ScoreLabel")
	game_over_label = get_node("../GameOverLabel")
	play_again_button = get_node("../PlayAgain")
	
	if Global.has_drippy:
		var buggy = get_node("Sprite")
		buggy.texture = preload("res://assets/images/drippy_buggy.png")
	
	
	
	game_over_label.visible = false
	play_again_button.visible = false
	
	score_timer.connect("timeout", self, "_on_ScoreTimer_timeout")
	score_timer.start(1.0)


func _input(event):
	if can_input and (event is InputEventScreenTouch or event is InputEventMouseButton):
		if event.pressed and linear_velocity.y > 0:
			apply_central_impulse(Vector2(0, jump_strength))
			
			
			if randf() < 0.5:
				angular_velocity = max(tilt_velocity, - 100 - rotation)
			else :
				angular_velocity = max( - tilt_velocity, - 100 - rotation)


func _on_ScoreTimer_timeout():
	score += 1
	score_label.text = "SCORE: " + str(score)


func _on_Exit_pressed():
	get_tree().change_scene_to(load("res://MainScene.tscn"))

func _on_Area2D_body_entered(body):
	Global.points = Global.points + round(score / 10)
	Global.save_value(Global.points)
	score_timer.stop()
	can_input = false
	game_over_label.set_bbcode("[center][wave amp=50.0 freq=5.0 connected=1]GAME OVER![/wave]\nNEW TOTAL POINTS:\n" + str(Global.points) + "[/center]")
	game_over_label.visible = true
	play_again_button.visible = true


func _on_PlayAgain_pressed():
	get_tree().change_scene_to(load("res://scenes/game.tscn"))
