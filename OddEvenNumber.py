# Name : Finney Bado
# Date : 03/05/2024
# Description : This program displays the odd number between 1 and 20 (included) and displays the sum of those numbers



# main function for the program
def odd_number():
    NUMBER_LIST = [i for i in range(1,20) if i%2 != 0]
    sum=0
    for number in NUMBER_LIST:
        print(number)
        sum+=number
    print("----------\nTOTAL : "+str(sum))

odd_number()