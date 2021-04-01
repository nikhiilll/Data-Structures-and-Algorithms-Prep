class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

def getLowestCommonManager(topManager, reportOne, reportTwo):
    
    _, _, _, LCM = getLCMHelper(topManager, reportOne, reportTwo)
    return LCM

def getLCMHelper(manager, reportOne, reportTwo):

    currOneFound, currTwoFound, currBothFound, currLCM = False, False, False, None
    if manager.name == reportOne.name:
        currOneFound = True
    if manager.name == reportTwo.name:
        currTwoFound = True

    for report in manager.directReports:
        newOneFound, newTwoFound, newBothFound, newLCM = getLCMHelper(report, reportOne, reportTwo)
        if newBothFound:
            return (True, True, True, newLCM)
        if (currOneFound and newTwoFound) or (currTwoFound and newOneFound):
            return (True, True, True, manager)
        currOneFound = currOneFound or newOneFound
        currTwoFound = currTwoFound or newTwoFound

	return (currOneFound, currTwoFound, currBothFound, currLCM)
