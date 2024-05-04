# Name : Finney Bado
# Date : 04/05/2024
# Description : This programs detect "tom" and "tim" sequences in a string and return True or False if they match or
# False if they don't (number of occurrence of "tim" must match "tom" ' s )




######################################################################
#                               MAIN BODY
#####################################################################

def match(string: str)-> bool:


    tim_counter=0
    tom_counter=0
    cursor1=0
    cursor2=0


    while cursor1 != -1 and cursor2 != -1:
        if cursor1!=-1:
            cursor1 = string.find("tom",cursor1)
            if cursor1 == -1:
                pass
            else:
                tom_counter+=1
                cursor1+=3
        if cursor2!=-1:
            cursor2 = string.find("tim",cursor2)
            if cursor2 == -1:
                pass
            else:
                tim_counter+=1
                cursor2+=3

    return tim_counter==tom_counter


######################################################################
#                               TEST
#####################################################################

def test_match():
    assert match("tomtimtomtim") == True
    assert match("tomtimtom") == False
    assert match("tomtimtomtim tom et tim") == True
    assert match("tom et tom et tim") == False


test_match()
