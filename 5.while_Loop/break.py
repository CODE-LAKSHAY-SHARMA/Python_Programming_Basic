def func():
    i = 1
    while i <= 5:
        print("hello")
        if i == 3:
            # break  # yeh function se bhaar break nhi hoga sirf loop se break hoga aur DONE print karega at the end
            return  # this will not print DONE
        i = i + 1
    print("done")


func()
