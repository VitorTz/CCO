import datetime


MONTHS_TO_NUM = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

NUM_TO_MONTH = {
    v: k for k, v in MONTHS_TO_NUM.items()
}


def main():
    n = int(input())    
    for i in range(n):
        d: list[str] = input().split('-')
        d1 = datetime.date(int(d[0]), int(MONTHS_TO_NUM[d[1]]), int(d[2]))        
        days = int(input())        
        d2 = d1 + datetime.timedelta(days=days)
        print(f"Case {i+1}: {d2.year}-{NUM_TO_MONTH[str(d2.month).zfill(2)]}-{d2.day:02}")
        
    

if __name__ == "__main__":
    main()