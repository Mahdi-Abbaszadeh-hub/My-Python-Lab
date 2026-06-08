# Practice one
"""
برنامه‌ای بنویسید که از کاربر یک لیست از اعداد (به صورت رشته با فاصله) بگیرد و آن‌ها را به
int
تبدیل کند
اگر در بین ورودی‌ها مقدار غیرعددی بود، برنامه با
try/except
خطا را مدیریت کند و به کاربر اطلاع دهد
"""

user_input = input("please enter your text: ")
try:
    my_list = []
    for i in user_input.split():
        my_list.append(int(i))
    print(my_list)
except ValueError:
    print("i can't change type")

# --------------------------
