seat_numbers = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]
target_seat = 130

print("================================")
print("MY TRAIN SEAT FINDER")
print("================================")
print("Available Seats:", seat_numbers)
print("Seat to Find:", target_seat)

def binary_search(seats, target):
    low = 0
    high = len(seats) - 1

    while low <= high:
        mid = (low + high) // 2
        print("Checking:", seats[mid])

        if seats[mid] == target:
            return mid
        elif target < seats[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

index = binary_search(seat_numbers, target_seat)

print("\nBinary Search Result:")
if index != -1:
    print("Seat found at index:", index)
else:
    print("Seat not found.")

def recursive_search(seats, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if seats[mid] == target:
        return mid
    elif target < seats[mid]:
        return recursive_search(seats, target, low, mid - 1)
    else:
        return recursive_search(seats, target, mid + 1, high)

index = recursive_search(seat_numbers, target_seat, 0, len(seat_numbers) - 1)

print("\nRecursive Search Result:")
if index != -1:
    print("Seat found at index:", index)
else:
    print("Seat not found.")

print("\nTime Complexity: O(log n)")
print("Binary search works on sorted lists.")