#q3
import csv
def func():
    f = open("q3.csv", 'r', encoding="utf8")
    data = csv.reader(f)
    next(data)
    
    line_tag = []
    for i in range(9):
        line_tag += [str(i+1)+"호선"]
    
    line=[0,0,0,0,0,0,0,0,0]
    
    for i in data:
        try:
            for j in range(9):
                if i[1] == line_tag[j]:
                    line[j] = line[j] + int(i[4]) + int(i[5])
        except:
             continue
    
    M = line[0]
    M_i=0
    m = line[0]
    m_i=0
    
    for i in range(9):
        if M < line[i]:
            M = line[i]
            M_i = i
        if m > line[i]:
            m = line[i]
            m_i = i
        
    M1 = M_i
    m1 = m_i
    
    M = line[0]
    M_i=0
    m = line[0]
    m_i=0
    
    if M_i == M1:
        M_i = 1
        M = line[1]
    if m_i == m1:
        m_i = 1
        m = line[1]
    
    for i in range(8):
        if M < line[i]:
            if i != M1:
                M = line[i]
                M_i = i
        if m > line[i]:
            if i != m1:
                m = line[i]
                m_i = i

    M2 = M_i
    m2 = m_i

    print('*** Subway Report for Seoul on March 2023 ***')
    print()
    print('1st Busiest Line: Line '+str(M1+1))
    print()
    print('2st Busiest Line: Line '+str(M2+1))
    print()
    print('1st Least used Line: Line '+str(m1+1))
    print()
    print('2st Least used Line: Line '+str(m2+1))

if __name__ == "__main__":
    func()


    
