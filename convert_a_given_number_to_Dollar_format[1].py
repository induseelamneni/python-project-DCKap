ones = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
        7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve',
        13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
        17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty',
        7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
illions = {1: 'Thousand', 2: 'Million', 3: 'Billion'}


def convert_number_to_word(number):
    if (number == 0):
        return ("Enter number Grater Than one")
    return get_number_position(number)

def get_number_position(number):
    if (number < 20):
        return ones[number]
    if (number < 100):
        return join_words(tens[number//10],ones[number%10])
    if (number < 1000):
        return divsion_number(number, 100, "Hundred")
    for p_number , p_name in illions.items():
        if (number < 1000 ** (p_number+1)):
            break 
    return divsion_number(number,1000**p_number, p_name)
            

def divsion_number(position,number, name):
    return join_words(get_number_position(position//number),name,get_number_position(position%number))
    
    
    
    
def join_words(*words):
    return " ".join(words)





number = int(input())
print(convert_number_to_word(number)+" dollars")