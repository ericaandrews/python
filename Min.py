#Min
	list=[1,3,6,8,4,9,23,45,67,89]
	print(min(list))
	
	my_letters= ('m,y,l,e,t,t,e,r,s')
	print(min(my_letters))
	
	print(min(10, 300, 450, 50, 90))
	
	player_guesses= [12,6,45,8,23]
	if min(player_guesses) > 25:
	    print("You win!")
	else:
	    print("You lose!")

	guess_this_number = 25
	player_guesses=[2,3,5,4,7,6,8]
	if min(player_guesses) > guess_this_number:
	    print("You win!")
	else:
	    print("You lose!")	
