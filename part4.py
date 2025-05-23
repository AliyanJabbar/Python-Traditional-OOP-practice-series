# Class Variables and Class Methods
# Assignment: Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Meezan hai apna bank"

    def change_bank_name(cls, name):
        Bank.bank_name = name


bank1 = Bank()
print(f"The bank's name before update is {bank1.bank_name}")
bank2 = Bank()
print(f"The bank's name before update is {bank2.bank_name}")
bank3 = Bank()
print(f"The bank's name before update is {bank3.bank_name}")

# showing that it affects all instances
bank1.change_bank_name("JS")
print(f"The bank's name after update is {bank1.bank_name}")
print(f"The bank's name after update is {bank2.bank_name}")
print(f"The bank's name after update is {bank3.bank_name}")


# to solve this issue that only the desired instance change the name

# class Bank:
#     def __init__(self,bank_name):
#         self.bank_name = bank_name

#     def change_bank_name(self,name):
#         self.bank_name = name

# bank1 = Bank("Meezan")
# print(f"The bank's name before update is {bank1.bank_name}")
# bank2 = Bank("Alfalah")
# print(f"The bank's name before update is {bank2.bank_name}")
# bank3 = Bank("UBL")
# print(f"The bank's name before update is {bank3.bank_name}")

# # showing that it will not affect all instances
# bank2.change_bank_name("JS")
# print(f"The bank's name after update is {bank1.bank_name}")
# print(f"The bank's name after update is {bank2.bank_name}")
# print(f"The bank's name after update is {bank3.bank_name}")
