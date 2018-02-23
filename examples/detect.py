#!/usr/bin/env python


print("""Unicorn HAT Detect-o-matic v2.0

Note: Your Unicorn HAT must be plugged in before boot to detect properly!

""")

product = None

try:
    product = open("/proc/device-tree/hat/product","r").read().strip().replace("\x00", "")
except IOError:
    pass

if product is None:
    print(
"""We couldn't find a connected EEPROM, so we'll assume you're using a Unicorn pHAT.

You should use the following in your code:

    import unicornhat
    unicornhat.set_layout(unicornhat.PHAT)

If you're sure you've connected a HAT, use:

    import unicornhat
    unicornhat.set_layout(unicornhat.HAT)
""")

else:
    if product[:11] == "unicornhat":
        print(
"""We found a Unicorn HAT connected to your Pi.

You should use the following in your code:

    import unicornhat
    unicornhat.set_layout(unicornhat.HAT)

""")
    else:
        print(
"""Hold up, we found "{}" connected to your Pi!

Go walk the plank, landlubber! That ain't no Unicorn HAT

If this is wrong, chances are you've swapped HATs or pHATs without rebooting.

You should use the following in your code for Unicorn HAT:

    import unicornhat
    unicornhat.set_layout(unicornhat.HAT)

Or for Unicorn pHAT:

    import unicornhat
    unicornhat.set_layout(unicornhat.PHAT)
""".format(product))
