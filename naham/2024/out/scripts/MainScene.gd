extends Control

func _ready():
	if Global.has_drippy:
		var buggy = get_node("Background/Sprite")
		buggy.texture = preload("res://assets/images/drippy_buggy.png")

func _on_Play_pressed():
	get_tree().change_scene_to(load("res://scenes/game.tscn"))


func _on_Shop_pressed():
	get_tree().change_scene_to(load("res://scenes/shop.tscn"))
