def change(b, c, d):
    def a(x):
        return b(c(d(x)))
    return a


def kilometer2meter(dist):
    """ Function that converts km to m. """
    print("Converting km to m")
    return dist * 1000


def meter2centimeter(dist):
    """ Function that converts m to cm. """
    print("Converting m to cm")
    return dist * 100


def centimeter2feet(dist):
    """ Function that converts cm to ft. """
    print("Converting cm to ft")
    return dist / 30.48


if __name__ == '__main__':
    transform = change(centimeter2feet, meter2centimeter, kilometer2meter)
    e = transform(565)
    print(e)