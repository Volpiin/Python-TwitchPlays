import time
#By zmienić długość timera zmieńta se i = X na ładną liczbe.
def stopwatch():
    i = 5 #Value do zmiany 
    while i >= 1:
        print(i)
        i-=1
        time.sleep(1)
    return 
