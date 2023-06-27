from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])

challenges = deque([int(x) for x in input().split()])

while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances[-1]
    value = tool * substance

    if value in challenges:
        challenges.remove(value)
        substances.pop()
    else:
        substance -= 1
        if substance > 0:
            substances[-1] = substance
        else:
            substances.pop()
        tool += 1
        tools.append(tool)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances:
    print(f"Substances: {', '.join(map(str, substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")