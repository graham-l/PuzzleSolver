import yaml


class Face:
    def __init__(self, numList):
        self.numList = numList


class Block:
    def __init__(self, faceList, blockNumber):
        self.faceList = faceList
        self.blockNumber = blockNumber


def blockPerms(builtChain: list, spareBlocks: list):
    if len(spareBlocks) == 0:
        print('I HAVE FOUND A SOLUTION')
        print(yaml.dump(builtChain))
        quit()
        return True
    elif len(builtChain) == 0:
        for b in spareBlocks:
            for f in b.faceList:
                newFace = Face([f.numList[0], f.numList[1]])
                newBlock = Block([newFace], b.blockNumber)
                testChain = builtChain.copy()
                testChain.append(newBlock)
                spares = []

                for s in spareBlocks:
                    if s.blockNumber != b.blockNumber:
                        spares.append(s)

                #print(yaml.dump(testChain))
                ressie: bool = blockPerms(testChain, spares)

                if not ressie:
                    newFace = Face([f.numList[1], f.numList[0]])
                    newBlock = Block([newFace], b.blockNumber)
                    testChain = builtChain.copy()
                    testChain.append(newBlock)
                    #print(yaml.dump(testChain))
                    thisOutcome: bool = blockPerms(testChain, spares)

                    if thisOutcome:
                        return True
    else:
        lenny = len(builtChain)
        lastInChain = builtChain[len(builtChain) - 1]
        #print(yaml.dump(lastInChain))
        #print(yaml.dump(lastInChain.faceList[0].numList))
        matchDigit = lastInChain.faceList[0].numList[1]

        for b in spareBlocks:
            spares = []
            for b2 in spareBlocks:
                if b2.blockNumber != b.blockNumber:
                    spares.append(b2)

            for f in b.faceList:
                newFace = Face([f.numList[1], f.numList[0]])
                newBlock = Block([newFace], b.blockNumber)

                if newBlock.faceList[0].numList[0] != matchDigit:
                    temp: int = newBlock.faceList[0].numList[0]
                    newBlock.faceList[0].numList[0] = newBlock.faceList[0].numList[1]
                    newBlock.faceList[0].numList[1] = temp

                if newBlock.faceList[0].numList[0] == matchDigit:
                    newChain = builtChain.copy()
                    newChain.append(newBlock)

                    outcome: bool = blockPerms(newChain, spares)

                    if not outcome:
                        newFace = Face([f.numList[0], f.numList[1]])
                        newBlock = Block([newFace], b.blockNumber)

                        if newBlock.faceList[0] != matchDigit:
                            return False

                        newChain = builtChain.copy()
                        newChain.append(newBlock)

                        testResult: bool = blockPerms(newChain, spares)

                        if testResult:
                            return True


f1 = Face([2, 3])
f2 = Face([10, 11])
b1 = Block([f1, f2], 1)

f1 = Face([20, 21])
f2 = Face([1, 2])
b2 = Block([f1, f2], 2)

f1 = Face([3, 4])
f2 = Face([30, 31])
b3 = Block([f1, f2], 3)

blocksAll = [b1, b2, b3]
blockPerms([], blocksAll)

print('Finished');
