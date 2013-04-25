FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

#Your code here
#You can import some modules or create additional functions


def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    d1 = {'0':'', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}
    d2 = {'2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}

    data = number
    string = ''
    hun = data/100
    remind = data%100
    if hun >= 1:
        string += d1[str(hun)] + ' hundred '
    tenth = remind/10
    if tenth >= 2:
        string +=  d2[str(tenth)]
        remind = remind%10
        if remind > 0:
            string += ' ' + d1[str(remind)]
    else:
        string += d1[str(remind)]
    #replace this for solution
#    return 'string representation of n'
    string = string.strip()
    return string
#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
