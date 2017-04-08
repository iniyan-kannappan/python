from T_Shapes import rectangle,triangle,circle

def main():
    print('Type in the area of a Circle,Rectangle,or Triangle.')
    shape=str(input())        
    if shape=='Rectangle':
        rectangle()
    if shape=='Triangle':
        triangle()
    if shape=='Circle':
        circle()
main()
