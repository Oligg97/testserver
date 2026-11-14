def SE1(movement, noise):
    """Return True and print a message when movement and noise are detected."""
    if movement == 1 and noise == 1:
        print("alarm activated")
        return True

    print("no alarm")
    return False


# Simulate a sensor reading: movement and noise are both detected.
movement = 1
noise = 1
SE1(movement, noise)
