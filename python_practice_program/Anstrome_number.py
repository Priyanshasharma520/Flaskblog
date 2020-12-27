print("Hello")
class anstrome_numer():
    def __init__(self):
        pass
    def getting_numbers(self,number):
        number_list=[]
        while number!=0:
            p=number%10
            number_list.append(p)
            number=number//10
        return number_list

    def finding_anstrome(self,number):
        number_list=self.getting_numbers(number)
        length_of_number=len(number_list)
        counter=0
        for digit in number_list:
            counter=counter+digit**length_of_number
        if counter == number:
            return True
        else:
            return False

obj = anstrome_numer()
print("Hello")
print(obj.finding_anstrome(100))