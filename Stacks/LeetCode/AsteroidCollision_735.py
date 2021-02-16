def asteroidCollision(asteroids):

    # stack = []
    # isCollided = True
    # asteroids_copy = asteroids[:]

    # while isCollided:

    #     isCollided = False

    #     for asteroid in asteroids_copy:
    #         if not stack:
    #             stack.append(asteroid)
    #         elif (stack[-1] > 0 and asteroid <0):
    #             if abs(stack[-1]) < abs(asteroid):
    #                 stack.pop()
    #                 stack.append(asteroid)
    #             elif abs(stack[-1]) == abs(asteroid):
    #                 stack.pop()
    #             isCollided = True
    #         else:
    #             stack.append(asteroid)
    #         print(stack)
    #     asteroids_copy = stack[:]
    #     stack = []
    
    # return asteroids_copy

    stack = []

    for new in asteroids:
        while stack and new < 0 < stack[-1]:
            if stack[-1] < - new:
                stack.pop()
                continue
            elif stack[-1] == -new:
                stack.pop()
            break
        else:
            stack.append(new)
    
    return stack


asteroids = [8,-8]
print(asteroidCollision(asteroids))
        

        