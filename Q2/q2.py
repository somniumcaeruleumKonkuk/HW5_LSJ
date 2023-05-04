#q2
import csv
def q2():
    t_Max_dif=0
    d_Max_dif=''
    
    t_Min_dif=100
    d_Min_dif=''
    
    f = open("q2.csv", 'r', encoding='utf8')
    data = csv.reader(f)
    for i in range(8):
        next(data)
    
    for i in data:
        try:
            var = float(i[4])-float(i[3])
            if var > t_Max_dif:
                t_Max_dif = var
                d_Max_dif = (i[0]).strip()
            if var < t_Min_dif:
                t_Min_dif = var
                d_Min_dif = (i[0]).strip()
        except:
            continue
    
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print()
    print("Day with the Largest Temperature Variation: "+d_Max_dif)
    print()
    print("Maximum Temperature Difference: {0:.1f} Celsius".format(t_Max_dif))
    print()
    print("Day with the Smallest Temperature Variation: "+d_Min_dif)
    print()
    print("Minimum Temperature Difference: {0:.1f} Celsius".format(t_Min_dif))

if __name__ == "__main__":
    q2()
