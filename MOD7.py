def schedule():     
# create dictionaries using the course number as the key and room,instructors,and times as values.     
	rooms = {'CSC101':3004, 'CSC102':4501, 'CSC103':6755, 'NET110':1244, 'COM241':1411}     
	instructors = {'CSC101':'Haynes', 'CSC102':'Alvarado', 'CSC103':'Rich', 'NET110':'Burke', 'COM241':'Lee'}      
	times = {'CSC101':'8:00 a.m.', 'CSC102':'9:00 a.m.', 'CSC103':'10:00 a.m.', 'NET110':'11:00 a.m.', 'COM241':'1:00 p.m.'}    
# ask the user to input the course number to retreive detailed course information	
	course = input('Enter a course number: ')      
	if course not in rooms:         
		print(course, 'is an invalid course number.')     
	else:    
		print('The details for course', course, 'are:')         
		print('Room:', rooms[course])         
		print('Instructor:', instructors[course])         
		print('Time:', times[course])  
# Call the schedule function. 
schedule()
