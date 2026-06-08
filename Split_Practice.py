"""
برنامه‌ای بنویسید که یک ورودی متن را با استفاده از
input
از کاربر گرفته
سپس تعداد کارکتر های عددی و حروف را شمارش کرده و سپس در یک دیکشنری تعداد بدست آمده راقرار داده
"""


def slicing():
    """ """
    user_input = input("enter your text: ")
    my_list = user_input.split()
    my_dic = {}
    for i in my_list:
        if i not in my_dic:
            my_dic[i] = 1
        else:
            my_dic[i] += 1
    return my_dic


print(slicing())
