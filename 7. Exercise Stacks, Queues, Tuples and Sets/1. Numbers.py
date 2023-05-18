first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command
    if command == "Add First":
        [first_sequence.add(int(el)) for el in data]
    elif command == "Add Second":
        [second_sequence.add(int(el)) for el in data]
    elif command == "Remove First":
        [first_sequence.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [second_sequence.discard(int(el)) for el in data]
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
