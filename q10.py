
final_val = int(input("enter final value: "))
curr_val = 0
moves = 0

while not curr_val == final_val:
    moves += 1
    if curr_val + moves > final_val:
        curr_val -= moves
    else:
        curr_val += moves

    print(curr_val, final_val)

print("moves: ", moves)
