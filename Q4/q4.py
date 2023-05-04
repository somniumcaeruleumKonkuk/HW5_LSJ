#q4
import csv
def q4():
    f = open("q4.csv", 'r', encoding='utf8')
    data = csv.reader(f)
    next(data)

    print('*** Subway Report for Seoul on March 2023 ***')
    print('')

    line_tag = ['1호선','2호선','3호선','4호선']
    
    line = [dict(), dict(), dict(), dict()]
    
    for i in data:
        for L in data: #1: line number
            if L[1] == line_tag[0]:
                if L[3] in line[0].keys():
                    line[0][L[3]] += L[4] + L[5]
                else:
                    line[0][L[3]] = L[4] + L[5]
            elif L[1] == line_tag[1]:
                if L[3] in line[1].keys():
                    line[1][L[3]] += L[4] + L[5]
                else:
                    line[1][L[3]] = L[4] + L[5]
            elif L[1] == line_tag[2]:
                if L[3] in line[2].keys():
                    line[2][L[3]] += L[4] + L[5]
                else:
                    line[2][L[3]] = L[4] + L[5]
            elif L[1] == line_tag[3]:
                if L[3] in line[3].keys():
                    line[3][L[3]] += L[4] + L[5]
                else:
                    line[3][L[3]] = L[4] + L[5]
    for i in range(4):
        print('Line '+str(i+1)+':')

        station= list((line[i]).keys())
        
        b = station[0]
        l = station[0]

        for j in range(len(station)):
            if int(line[i][b]) < int(line[i][station[j]]):
                b = station[j]
            if int(line[i][l]) > int(line[i][station[j]]):
                l = station[j]
        
        print('Busiest Station: '+ b+" "+ line[i][b])
        print('Least used Station: '+ l + " " + line[i][l])
        
if __name__ == "__main__":
    q4()
