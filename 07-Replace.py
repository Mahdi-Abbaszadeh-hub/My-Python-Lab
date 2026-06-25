# Replace character in string

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)  # ---> I like apples

# -----------------------------

# how to change type Variable x to float or int
x = "39,000.0129"
x = float(x.replace(",", ""))
print(x)
