#!/usr/bin/env python

import unicornhat as unicorn


print("""Detect

Note: Your Unicorn HAT must be plugged in before boot to detect properly!

""")


print("Trying to detect if you have a Unicorn HAT or Unicorn pHAT")
unicorn.set_layout(unicorn.AUTO)
print("Autodetection finished, let's see the result...")
print("")

width,height=unicorn.get_shape()

if height == width:
   print("Your height is equal to your width, so you must have a HAT.")
else:
   print("Your height is NOT equal to your width, so you must have a pHAT.")

print("")
print("If your hardware has been properly detected, it should be safe to use the following in your code:")
print("unicorn.set_layout(unicorn.AUTO)")
print("")
print("Otherwise use one of the following in our code:")
print("")
print("unicorn.set_layout(unicorn.PHAT)")
print("unicorn.set_layout(unicorn.HAT)")
print("")
