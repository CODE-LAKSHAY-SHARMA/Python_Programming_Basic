str1 = "python is a good language"


ans = str1.split()
# split() run over WHITESPACE(space,enter, tab)
print(ans)  # by default , space remove kar deyga bas

ans1 = str1.split("g")  # g par split karna hai, remove g and print before it
print(ans1)
