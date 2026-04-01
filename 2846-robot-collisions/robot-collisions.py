class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(len(positions))])
        stack = []
        healths = list(healths)
        
        for pos, h, i_dir, i in robots:
            if i_dir == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack[-1]
                    if healths[j] < healths[i]:
                        healths[j] = 0
                        stack.pop()
                        healths[i] -= 1
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                    else:
                        healths[j] = 0
                        healths[i] = 0
                        stack.pop()
                        break
        
        return [healths[i] for i in range(len(healths)) if healths[i] > 0]