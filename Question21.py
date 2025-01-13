import math

def calculate_distance():
    x, y = 0, 0
    
    while True:
        move = input("Enter movement (e.g., UP 5) or type 'end' to stop: ")
        
        if move.lower() == 'end':
            break
        
        direction, steps = move.split()
        steps = int(steps)
        
        if direction == 'UP':
            y += steps
        elif direction == 'DOWN':
            y -= steps
        elif direction == 'LEFT':
            x -= steps
        elif direction == 'RIGHT':
            x += steps
    
    distance = math.sqrt(x**2 + y**2)
    print(round(distance))

# Example usage
calculate_distance()
