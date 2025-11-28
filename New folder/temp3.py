# inp=1
# x="sad"
# # x=2
# print(type(x))
# if type(x)==type("dasd"):
#     print(True)
# else:
#     print(False)

list_val = [i**2 for i in range(10) if i > 5]
# print(list_val)

para = "Qualcomm values its relationships with our customers, consultants, candidates, and always strives to create a welcoming environment where our partners around the world can collaborate and interact with our employees. However, due to the growing scope of the COVID-19 outbreak, we have decided to conduct all interviews via video conferencing at this time. We hope you understand that this is for everyone’s health and safety. You will shortly receive confirmation of your interview and instructions for the video conference.   Thank you for your interest in working at Qualcomm. Below are the details and instructions for your interview via video conference. We look forward to speaking with you. "

para_list = para.split(" ")
# print(para_list)
dic_temp = {}

for i in para_list:
    if i in dic_temp:
        dic_temp[i] += 1
    else:
        dic_temp[i] = 1
# print(dic_temp)


# class vehicle():

#     def __init__(self,name,type) -> None:
#         self.name=name
#         self.type=type


# class two_v(vehicle):
#     pass

# class three_v(vehicle):
#     def __init__(self, name, type,wheels) -> None:
#         self.name=name
#         self.wheels=wheels


# v1=vehicle("xyz","car")
# v2=vehicle("abc","bike")

# print(v1.name,v1.type)
# print(v2.name, v2.name)


def temp(name, *arg, **kwargs):
    print(name)
    print(arg)
    print(kwargs)


temp("sudh", 123, "qualcom", {"val", 123, 563})
