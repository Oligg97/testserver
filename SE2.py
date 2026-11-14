def SE2(stod, fald):
    """Print a sensor message and return whether a fall was detected."""
    if fald == 1:
       #print("stod")
        return True

    elif stod == 1:
        #print("fald")
        return False

    elif stod == 0 and fald == 0:
        print("OK")
        return False


# Simulate a sensor reading.
stod = 0
fald = 1
SE2(fald, stod)
