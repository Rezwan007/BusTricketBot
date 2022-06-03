
travelType = input("Please Enter Bus or Train or Launch")
for travelTypeValid in travelType:
    if travelType == "Bus":
        exec(open('shohoz_bus.py').read())
    if travelType == "Train":
        exec(open('shohoz_train.py').read())
    if travelType == "Launch":
        exec(open('shohoz_launch.py').read())
    if travelType == 0:
        print("Please Enter a Valid Travel type")
        travelType = input("Please Enter Bus or Train")
        # quit()