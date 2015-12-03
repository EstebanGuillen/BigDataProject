import sys
#import os.path


totalDistanceDivotDistance50To75Yeards = 0.0
totalDistanceDivotDistance76To100Yeards = 0.0
totalDistanceDivotDistance101To125Yeards = 0.0
totalDistanceDivotDistance126To150Yeards = 0.0

shotCountDivotDistance50To75Yeards = 0
shotCountDivotDistance76To100Yeards = 0
shotCountDivotDistance101To125Yeards = 0
shotCountDivotDistance126To150Yeards = 0

totalDistanceDistance50To75Yeards = 0.0
totalDistanceDistance76To100Yeards = 0.0
totalDistanceDistance101To125Yeards = 0.0
totalDistanceDistance126To150Yeards = 0.0

shotCountDistance50To75Yeards = 0
shotCountDistance76To100Yeards = 0
shotCountDistance101To125Yeards = 0
shotCountDistance126To150Yeards = 0

print('Parsing...')
for i in xrange(1,len(sys.argv)):
    print(sys.argv[i])
    with open(sys.argv[i]) as f:
        for line in f:
            splitLine = line.split(';')
            if str(splitLine[19]) == 'Fairway' and str(splitLine[21]) == 'Green' and str(splitLine[17]) == 'S':
                #print(splitLine[19],splitLine[21],splitLine[24],splitLine[25],splitLine[28], splitLine[30])
                if 2400.0 <= float(splitLine[24]) <= 3600.0 and str(splitLine[30]) == 'Divot':
                    shotCountDivotDistance50To75Yeards = shotCountDivotDistance50To75Yeards + 1
                    totalDistanceDivotDistance50To75Yeards = totalDistanceDivotDistance50To75Yeards + float(splitLine[28])
                if 2400.0 <= float(splitLine[24]) <= 3600.0 and str(splitLine[30]) == 'Good':
                    shotCountDistance50To75Yeards = shotCountDistance50To75Yeards + 1
                    totalDistanceDistance50To75Yeards = totalDistanceDistance50To75Yeards + float(splitLine[28])
                if 3600.1 <= float(splitLine[24]) <= 4800.0 and str(splitLine[30]) == 'Divot':
                    shotCountDivotDistance76To100Yeards = shotCountDivotDistance76To100Yeards + 1
                    totalDistanceDivotDistance76To100Yeards = totalDistanceDivotDistance76To100Yeards + float(splitLine[28])
                if 3600.1 <= float(splitLine[24]) <= 4800.0 and str(splitLine[30]) == 'Good':
                    shotCountDistance76To100Yeards = shotCountDistance76To100Yeards + 1
                    totalDistanceDistance76To100Yeards = totalDistanceDistance76To100Yeards + float(splitLine[28])
                if 6000.1 <= float(splitLine[24]) <= 7200.0 and str(splitLine[30]) == 'Divot':
                    shotCountDivotDistance101To125Yeards = shotCountDivotDistance101To125Yeards + 1
                    totalDistanceDivotDistance101To125Yeards = totalDistanceDivotDistance101To125Yeards + float(splitLine[28])
                if 6000.1 <= float(splitLine[24]) <= 7200.0 and str(splitLine[30]) == 'Good':
                    shotCountDistance101To125Yeards = shotCountDistance101To125Yeards + 1
                    totalDistanceDistance101To125Yeards = totalDistanceDistance101To125Yeards + float(splitLine[28])
                if 8400.1 <= float(splitLine[24]) <= 9600.0 and str(splitLine[30]) == 'Divot':
                    shotCountDivotDistance126To150Yeards = shotCountDivotDistance126To150Yeards + 1
                    totalDistanceDivotDistance126To150Yeards = totalDistanceDivotDistance126To150Yeards + float(splitLine[28])
                if 8400.1 <= float(splitLine[24]) <= 9600.0 and str(splitLine[30]) == 'Good':
                    shotCountDistance126To150Yeards = shotCountDistance126To150Yeards + 1
                    totalDistanceDistance126To150Yeards = totalDistanceDistance126To150Yeards + float(splitLine[28])


    f.close()
#print(str(totalDistanceDivotDistance50To75Yeards))
print(str(shotCountDivotDistance50To75Yeards))
#print(str(totalDistanceDistance50To75Yeards))
print(str(shotCountDistance50To75Yeards))
print("Divot 50 to 75: ",float(totalDistanceDivotDistance50To75Yeards/shotCountDivotDistance50To75Yeards))
print("Good 50 to 75: ", float(totalDistanceDistance50To75Yeards/shotCountDistance50To75Yeards))

#print(str(totalDistanceDivotDistance76To100Yeards))
print(str(shotCountDivotDistance76To100Yeards))
#print(str(totalDistanceDistance76To100Yeards))
print(str(shotCountDistance76To100Yeards))
print("Divot 76 to 100: ",float(totalDistanceDivotDistance76To100Yeards/shotCountDivotDistance76To100Yeards))
print("Good 76 to 100: ",float(totalDistanceDistance76To100Yeards/shotCountDistance76To100Yeards))


#print(str(totalDistanceDivotDistance101To125Yeards))
print(str(shotCountDivotDistance101To125Yeards))
#print(str(totalDistanceDistance101To125Yeards))
print(str(shotCountDistance101To125Yeards))
print("Divot 101 to 125: ",float(totalDistanceDivotDistance101To125Yeards/shotCountDivotDistance101To125Yeards))
print("Good 101 to 125: ",float(totalDistanceDistance101To125Yeards/shotCountDistance101To125Yeards))

#print(str(totalDistanceDivotDistance126To150Yeards))
print(str(shotCountDivotDistance126To150Yeards))
#print(str(totalDistanceDistance126To150Yeards))
print(str(shotCountDistance126To150Yeards))
print("Divot 126 to 150: ",float(totalDistanceDivotDistance126To150Yeards/shotCountDivotDistance126To150Yeards))
print("Good 126 to 150: ",float(totalDistanceDistance126To150Yeards/shotCountDistance126To150Yeards))





