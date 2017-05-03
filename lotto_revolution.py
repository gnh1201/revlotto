#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2016.12.17 Go Namhyeon

def main():
	# run
	lottoByWD1()
	
	lottoByWD2()
	
	return 0

def lottoByWD1():
	countRecord = [0, 0, 0, 0, 0, 0, 0, 0];
	countTable = [];
	
	nextStep = True;
	triedCnt = 0
	while nextStep is True:
		countTableLength = len(countTable)
		if countTableLength >= 1000:
			nextStep = False

		lottoNums = geneLotto()
		lottoFloat1 = lottoNums[0] / 45.0
		lottoFloat2 = lottoNums[1] / 45.0
		lottoFloat3 = lottoNums[2] / 45.0
		lottoFloat4 = lottoNums[3] / 45.0
		lottoFloat5 = lottoNums[4] / 45.0
		lottoFloat6 = lottoNums[5] / 45.0

		numGap1 = lottoFloat2 - lottoFloat1
		numGap2 = lottoFloat3 - lottoFloat2
		numGap3 = lottoFloat4 - lottoFloat3
		numGap4 = lottoFloat5 - lottoFloat4
		numGap5 = lottoFloat6 - lottoFloat5

		numGapAvg = round((numGap1 + numGap2 + numGap3 + numGap4 + numGap5) * 45)

		updateFlag = False
		for k in range(0, len(weightDegrees1)):
			if numGapAvg == (k + 2):
				if countRecord[k] < weightDegrees1[k]:
					updateFlag = True

				if updateFlag == True:
					countRecord[k] += 1
					countTable.append(lottoNums)
					break

				break

		triedCnt += 1
		
		if triedCnt >= 10000:
			print "{cnt} getted, 10,000 tried.".format(cnt=countTableLength)
			print countRecord
			triedCnt = 0
	
	print "Done."

	return countTable

def lottoByWD2():
	countRecord = [0, 0, 0, 0, 0, 0];
	oddEvenRates = [0.0, 0.2, 0.5, 1.0, 1.0, 5.0]
	countTable = [];
	
	nextStep = True;
	triedCnt = 0
	while nextStep is True:
		countTableLength = len(countTable)
		if countTableLength >= 1000:
			nextStep = False

		lottoNums = geneLotto()
		
		oddCnt = 0.0
		evenCnt = 0.0
		oddEvenRate = 0.0
		
		for k in lottoNums:
			if k % 2 == 1:
				oddCnt += 1.0
			else:
				evenCnt += 1.0

		if evenCnt > 0:
			oddEvenRate = oddCnt / evenCnt
		else:
			oddEvenRate = 0

		updateFlag = False
		for k in range(0, len(weightDegrees2)):
			if oddEvenRate == oddEvenRates[k] and countRecord[k] < weightDegrees2[k]:
				updateFlag = True

			if updateFlag == True:
				countRecord[k] += 1
				countTable.append(lottoNums)
				
				break

		triedCnt += 1
		
		if triedCnt >= 10000:
			print "{cnt} getted, 10,000 tried.".format(cnt=countTableLength)
			print countRecord
			triedCnt = 0
	
	print "Done."

	return countTable

def geneLotto():
    lotto = [0, 0, 0, 0, 0, 0]

    lotto[0] = random.randrange(1, 46, 1)

    lotto[1] = lotto[0]
    lotto[2] = lotto[0]
    lotto[3] = lotto[0]
    lotto[4] = lotto[0]
    lotto[5] = lotto[0]

    # 중복된 수가 발생되지 않도록 채번
    while (lotto[0] == lotto[1]):
        lotto[1] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[2] or lotto[1] == lotto[2]):
        lotto[2] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[3] or lotto[1] == lotto[3] or lotto[2] == lotto[3]):
        lotto[3] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[4] or lotto[1] == lotto[4] or lotto[2] == lotto[4] or lotto[3] == lotto[4]):
        lotto[4] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[5] or lotto[1] == lotto[5] or lotto[2] == lotto[5] or lotto[3] == lotto[5] or lotto[4] == lotto[5]):
        lotto[5] = random.randrange(1, 46, 1)

    # 결과를 정렬
    lotto.sort()
    
    return lotto

if __name__ == '__main__':
	import random
	
	weightDegrees1 = [1, 25, 57, 134, 222, 272, 246, 42];
	weightDegrees2 = [27, 64, 320, 347, 259, 73];
	weightDegrees3 = [26, 93, 249, 335, 216, 77];
	weightDegrees4 = [197, 346, 215, 130, 77, 16, 14, 1, 1];
	weightDegress5 = [1, 15, 38, 64, 175, 193, 279, 192, 42];
	
	main()

