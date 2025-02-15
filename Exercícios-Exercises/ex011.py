#Create a code that reads the width and the height of a wall in meters, calc the area and the necessary ammount of paint to cover it, knowing that a liter of paint can cover 2m²

width = float(input('Wall\'s width:' ))
height = float(input('Wall\'s height: '))
area = width*height
paint = area/2

print('The area of this wall is {:.1f}m².\nThe amount of paint that is needed to cover that wall is {:.1f}L.'.format(area, paint))