from sys import exit


def vault_room():
	print "The vault is full of small sacks of bills. How many do you take?"
	
	next = raw_input("> ")
	if next.isdigit():
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 10:
		print "You quickly grab some money and sneak out through the exit door. You win!"
		exit(0)
	else:
		dead("The police come in while you're loading up and take you away.")
		
		
def guard_room():
	print "There is a guard here."
	print "The guard has a gun and a newspaper."
	print "The guard is sitting in front of the vault door."
	print "There is also an exit door, which you're ignoring for now."
	print "How are you going to pass the guard?"
	guard_moved = False
	
	while True:
		next = raw_input("> ")
		
		if "gun" in next or "paper" in next:
			dead("The guard draws his gun and shoots you.")
		elif ("alarm" in next and not guard_moved) or ("lobby" in next and not guard_moved):
			print "The guard goes to investigate in the lobby. You can go through the door now."
			guard_moved = True
		elif ("alarm" in next and guard_moved) or ("lobby" in next and guard_moved):
			dead("The guard comes back, suspicious, and shoots you.")
		elif ("door" in next and guard_moved) or ("vault" in next and guard_moved):
			vault_room()
		elif "exit" in next:
			print "You're not going to leave just yet."
		else:
			print "That doesn't seem to make sense."
			
			
def office_room():
	print "This is the office of the bank manager."
	print "He stares at you and asks what you think you're doing in here."
	print "Do you go back or hold him hostage?"
	
	next = raw_input("> ")
	
	if "back" in next:
		start()
	elif "hostage" in next:
		dead("The SWAT team comes in and shoots you.")
	else:
		office_room()
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in an empty bank lobby."
	print "That doesn't seem right. Maybe you should tell someone?"
	print "The outside door is behind you."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		guard_room()
	elif next == "right":
		office_room()
	else:
		dead("The police come and take you away.")
		
		
start()