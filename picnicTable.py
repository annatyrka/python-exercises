import PyPDF2


def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEM".center(leftWidth+rightWidth, "-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".")+str(v).rjust(rightWidth))


picnicItems = {"sandwitches": 4, "apples": 12, "cups": 4, "cookies": 8000}
printPicnic(picnicItems, 12, 5)