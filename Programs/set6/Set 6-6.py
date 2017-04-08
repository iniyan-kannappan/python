print('Enter a number in 1 to 12.')
number=int(input())
months='JanFebMarAprMayJunJulAugSepOctNovDec'
starting_position=(number-1)*3
ending_position=starting_position+3
print(months[starting_position:ending_position])
