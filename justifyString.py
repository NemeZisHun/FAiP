#! python3

def printPicnic(items,leftWidth,rightWidth):
    print('PICNIC STOCK'.center(leftWidth+rightWidth,'-'))
    for a,s in items.items():
        print(a.ljust(leftWidth,'.')+str(s).rjust(rightWidth,' '))


picnicItems={'apples':4,'cigarettes':20,'salad':2,'wine':3,'beer':12}
printPicnic(picnicItems,14,3)