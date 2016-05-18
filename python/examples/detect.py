#!/usr/bin/env python

import unicornhat as unicorn

print("Trying to detect if you have a Unicorn HAT or Unicorn pHAT")
unicorn.set_layout(unicorn.AUTO)
print("Autodetection finished, let's see the result...")
print("")

width,height=unicorn.get_shape()

if height == 4:
   print("Your height is 4, so you must have a pHAT.")
else:
   print("Your height is not 4, so you must have a HAT.")

print("")
print("If your hardware has been properly detected, it should be safe to use the following in your code:")
print("unicornhat.set_layout(unicornhat.AUTO)")
print("")
print("Otherwise use one of the following in our code:")
print("")
print("unicornhat.set_layout(unicornhat.PHAT)")
print("unicornhat.set_layout(unicornhat.HAT)")
print("")
