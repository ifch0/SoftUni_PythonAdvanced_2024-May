# 01. Reverse Strings

input_text = list(input())
stack_list = []

for i in range(len(input_text)):
    stack_list.append(input_text.pop())

print("".join(stack_list))

# 02. Matching Parentheses

input_text = input()
starting_indexes = []

for i in range(len(input_text)):
    if input_text[i] == "(":
        starting_indexes.append(i)
    elif input_text[i] == ")":
        starting_index = starting_indexes.pop()
        print(input_text[starting_index:i+1])

# 03. Supermarket

from collections import deque
queue_customers = deque()

while True:
    command_input = input()

    if command_input == "Paid":
        while len(queue_customers):
            print(queue_customers.popleft())
    elif command_input == "End":
        print(f"{len(queue_customers)} people remaining.")
        break
    else:
        queue_customers.append(command_input)

# 04. Water Dispenser

from collections import deque
queue_customers = deque()
water_supply = int(input())

input_command = input()

while input_command != "Start":
    queue_customers.append(input_command)
    input_command = input()

input_command = input()

while input_command != "End":
    if "refill" in input_command:
        commands = input_command.split()
        water_supply += int(commands[1])
    else:
        water_demand = int(input_command)

        if water_demand <= water_supply:
            water_supply -= water_demand
            print(f"{queue_customers.popleft()} got water")
        else:
            print(f"{queue_customers.popleft()} must wait")

    input_command = input()

print(f"{water_supply} liters left")

# 05. Hot Potato

from collections import deque

kid_queue = deque()

input_list = input().split()

for i in input_list:
    kid_queue.append(i)

counter = int(input())

while len(kid_queue) > 1:
    for i in range(counter):
        if i == counter - 1:
            print(f"Removed {kid_queue.popleft()}")
        else:
            kid_queue.append(kid_queue.popleft())

print(f'Last is {kid_queue.popleft()}')
