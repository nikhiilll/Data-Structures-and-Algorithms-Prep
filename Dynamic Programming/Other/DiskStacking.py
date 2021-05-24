"""
TC: O(n^2)
SC: O(n)
"""


def diskStacking(disks):

    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    stacks = [None for disk in disks]
    maxHeightIdx = 0

    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            previousDisk = disks[j]
            if isValidDisk(previousDisk, currentDisk):
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    stacks[i] = j
        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i

    return buildDiskStack(stacks, disks, maxHeightIdx)


def isValidDisk(disk1, disk2):
    return disk1[0] < disk2[0] and disk1[1] < disk2[1] and disk1[2] < disk2[2]


def buildDiskStack(stacks, disks, maxHeightIdx):

    sequence = []
    while maxHeightIdx is not None:
        sequence.append(disks[maxHeightIdx])
        maxHeightIdx = stacks[maxHeightIdx]

    return list(reversed(sequence))
