def validStartingCity(distances, fuel, mpg):
    """
    TC: O(n^2)
    SC: O(1)
    """
    def helperVSC(d, f, mpg):

        availableMPG = 0
        for i in range(len(d) - 1):
            availableMPG += (f[i] * mpg)
            if availableMPG < d[i]:
                return False
            availableMPG -= d[i]

        return True

    for i in range(len(distances)):
        if helperVSC(distances[i:] + distances[:i], fuel[i:] + fuel[:i], mpg):
            return i

    return -1
