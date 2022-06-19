# ascending sort

AR = [3, 10, 7, 8, 4, 2, 11, 10]

NumberOfItems = len(AR)
for Pointer in range(1, NumberOfItems):
    ItemToBeInserted = AR[Pointer]
    CurrentItem = Pointer - 1
    while (AR[CurrentItem] > ItemToBeInserted) and (CurrentItem > -1):
        AR[CurrentItem + 1] = AR[CurrentItem]
        CurrentItem -= 1
    AR[CurrentItem + 1] = ItemToBeInserted

print(AR)
wait = input()
