def isSorted(lst):
    if len(lst) <= 1:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
def main():
    test_cases = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 3, 4, 2, 1],
        [3, 3, 3, 3],
        [1, 2, 3, 5, 4]]
    for i, case in enumerate(test_cases, 1):
        print(f"Test case {i}: {case} -> {isSorted(case)}")
if __name__ == "__main__":
    main()
