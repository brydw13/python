'''
unit converter: Milles and kilometers
'''
def print_menu():
	print('1. kilometers to miles')
	print('2. miles to kilometers')
	
def km_miles():
	km = float(input('enter disance in kilometers: '))
	miles = km / 1.609
	
	print('Distance in miles: {0}' .format(miles))
	
def miles_km():
	miles = float(input('Enter distance in miles: '))
	km = miles * 1.609

	print('Distance in miles: {0}' .format(miles))

if __name__ == '__main__':
	print_menu()
	choice = input('Which conversion would you like to do?: ')
	if choice == '1':
		km_miles()
		
if choice == '2':
	miles_km()
