def SE3(sleep, wake):
    if sleep == 1:
        print("ZZz")
        return True
    elif wake == 1:
        print("wake")

# Simulate a sensor reading: movement and noise are both detected.
sleep = 1
wake = 0
SE3(sleep, wake)
