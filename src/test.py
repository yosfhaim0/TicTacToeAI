import maxIt


def checkSeq_test():
    assert maxIt.checkSeq([[[38, -30, -40],
                            [100, 100, -54],
                            [-43, 88, -67]],
                           1e-05, 1, 1, 0, 20, 0]) == -1
    "need to be -1"

    assert maxIt.getNext([[[38, -30, -40],
                            [100, 95, -54],
                            [-43, 88, -67]],
                           1e-05, 1, 1, 0, 0, 0]) == []
    "need to be 0"


if __name__ == "__main__":
    checkSeq_test()
