def push_dominoes(dominoes):
    n = len(dominoes)
    result = list(dominoes)
    forces = [0] * n

    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n  
        elif dominoes[i] == 'L':
            force = 0  
        else:
            force = max(force - 1, 0)  
        forces[i] += force

    force = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            force = n  
        elif dominoes[i] == 'R':
            force = 0  
        else:
            force = max(force - 1, 0)  
        forces[i] -= force

    for i in range(n):
        if forces[i] > 0:
            result[i] = 'R'
        elif forces[i] < 0:
            result[i] = 'L'
        else:
            result[i] = '.'

    return ''.join(result)

if __name__ == "__main__":
    dominoes = input().strip()  
    result = push_dominoes(dominoes)
    print(result)
