#!/usr/bin/env python3
# TODO: Fix not being able to get the next_state function from main module
from main import next_state

print("Tests :")
print("Test 0 - Test if we get a all Dead grid and returns all dead grid")
state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
target_state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
needed_state = next_state(state=state)
if needed_state == target_state:
    print("Test Succeded")
else:
    print("Test Failed")
    print(f"needed_state is:{needed_state}")
    print("in not equal to :")
    print(f"target_state is :{target_state} ")

print("----------------------------------")
print("✅ Test Case 1: Still Life (Block)")
state = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

target_state = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
needed_state = next_state(state=state)
if needed_state == target_state:
    print("Test Succeded")
else:
    print("Test Failed")
    print(f"needed_state is:{needed_state}")
    print("in not equal to :")
    print(f"target_state is :{target_state} ")


print("----------------------------------")
print("✅ Test Case 2: Oscillator (Blinker)")
state = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

target_state = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]
needed_state = next_state(state=state)
if needed_state == target_state:
    print("Test Succeded")
else:
    print("Test Failed")
    print(f"needed_state is:{needed_state}")
    print("in not equal to :")
    print(f"target_state is :{target_state} ")


print("----------------------------------")
print("✅ Test Case 3: Reproduction")
state = [[0, 1, 0], [1, 0, 1], [0, 0, 0]]

target_state = [[0, 1, 0], [1, 1, 1], [0, 0, 0]]


needed_state = next_state(state=state)
if needed_state == target_state:
    print("Test Succeded")
else:
    print("Test Failed")
    print(f"needed_state is:{needed_state}")
    print("in not equal to :")
    print(f"target_state is :{target_state} ")

print("----------------------------------")
print("✅ Test Case 4: Overpopulation")
state = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

target_state = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


needed_state = next_state(state=state)
if needed_state == target_state:
    print("Test Succeded")
else:
    print("Test Failed")
    print(f"needed_state is:{needed_state}")
    print("in not equal to :")
    print(f"target_state is :{target_state} ")


print("----------------------------------")
print("✅ Test Case 5: Underpopulation")
state = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

target_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


needed_state = next_state(state=state)
if needed_state == target_state:
    print("Test Succeded")
else:
    print("Test Failed")
    print(f"needed_state is:{needed_state}")
    print("in not equal to :")
    print(f"target_state is :{target_state} ")


if __name__ == "main":
    pass
