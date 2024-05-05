# Name : Finney Bado
# Date : 04/05/2024
# Description : Program that triple every character in a string
# Ex : f("Finney") ==> "FFFiiinnneeeyyy"


############################################################
#                   MAIN BODY
###########################################################


def tripple(string: str) -> str:

    result_string = ""

    for letter in string:
        result_string+=letter*3

    return result_string

############################################################
#                  TEST FUNCTIONS
############################################################

def test_tripple():
    assert tripple("Finney") == "FFFiiinnnnnneeeyyy"
    assert tripple("Hey!") == "HHHeeeyyy!!!"

test_tripple()