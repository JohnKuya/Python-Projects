# # define a python a functions is the value of the argument is over 50 otherwise
# # should it find it is over 50 it gives success otherwise it gives fail
#
# def english(score):
#     if score > 70:
#         print("success")
#     else:
#         print("fail")
# english(score=50)
#
def score():
    x = int(input("Please enter your marks:"))
    if x >= 50:
        print(f"{x} is successfull")
    else:
        print(f"{x} is failed")

score()
