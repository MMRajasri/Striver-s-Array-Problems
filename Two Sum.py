# "coding ninjja problem' link--> https://www.codingninjas.com/studio/problems/reading_6845742?leftPanelTabValue=PROBLEM

def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    left = 0
    right = n - 1
    book.sort()
    while left < right:
        summation = book[left] + book[right]
        if summation == target:
            return 'YES'
        elif summation < target:
            left += 1
        else:
            right -= 1
    return 'NO'
    pass
