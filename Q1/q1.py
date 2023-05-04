#q1.py
import csv
def func():
        a=0.0
        am=0.0
        aM=0.0
        cnt = 0
        #8
        f = open("q1.csv", "r", encoding="utf-8")
        data = csv.reader(f)
        for i in range(8):
                next(data)

        for i in data:
                try:
                        aM += float(i[4])
                        am += float(i[3])
                        a += float(i[2])
                        cnt = cnt + 1
                except:
                        continue

        aM /= cnt
        am /= cnt
        a /= cnt

        print("*** Annual Temperature Report for Seoul in 2022 ***")
        print()
        print("Average Temperature: {0: .2f} Celsius".format(a))
        print()
        print("Average Minimum Temperature: {0: .2f} Celsius".format(am))
        print()
        print("Average Maximum Temperature: {0: .2f} Celsius".format(aM))

if __name__ == "__main__":
	func()
