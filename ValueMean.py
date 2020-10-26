## Author: Feras
## Description: implement a method named valueMean that accpets a list of integer and return the mean value of the list
## Formula: mean = sum / n where n is the size of the list

def valueMean(mylist):
    for n in mylist:
        sum = 0
        sum += n
        mean = sum / n
    return mean
print(valueMean([1,2,3,4,5,6,7,8,9]))