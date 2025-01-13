def capitalize_lines():
    lines = []
    print("Enter lines (enter an empty line to stop):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.upper())
    
    for line in lines:
        print(line)

capitalize_lines()
