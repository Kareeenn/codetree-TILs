k = list(map(int, input().split()))
y, m, d = k[0], k[1], k[2]

def right(y,m,d):
    if exist(y,m,d):
        season(m,d)
    else:
        return -1

def exist(y,m,d):
    if yunan(y):
        if m in [1,3,5,7,8,10,12]:
            if 1 <= d and d <= 31:
                return True
            else:
                return False
        elif m == 2:
            if 1 <= d and d <= 29:
                return True
            else:
                return False
        else:
            if 1 <= d and d <= 30:
                return True
            else:
                return False
       
    else:
        if m in [1,3,5,7,8,10,12]:
            if 1 <= d and d <= 31:
                return True
            else:
                return False
        elif m == 2:
            if 1 <= d and d <= 28:
                return True
            else:
                return False
        else:
            if 1 <= d and d <= 30:
                return True
            else:
                return False
       
def yunan(y):
    #4의 배수, 100의 배수 아님
    #4의 배수, 100의 배수, 400의 배수
    if y % 4 == 0:
        if y % 100 != 0:
            return True
        elif y % 400 == 0:
            return True
        else:
            return False
    else:
        return False


def season(m,d):
    if 3 <= m and m <= 5:
        print("Spring")
    elif 6 <= m and m <= 8:
        print("Summer")
    elif 9 <= m and m <= 11:
        print("Fall")
    else:
        print("Winter")

right(y,m,d)