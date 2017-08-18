# Animated weather icons for the unicorn-hat

Handmade weather animations for unicorn-hat made by pimoroni. each animation is made of 8-16 handmade mini-mini pictures, combined to a sprite.

Please use a diffuser for best quality of the animations and for your own safety of course too. 

`draw_animation(image)` is same as in the 'show-png' example but put into a tiny little function.

Put in your image object and you're done.

[pimoroni's show-png example](https://github.com/pimoroni/unicorn-hat-hd/blob/master/examples/show-png.py "pimoroni's show-png example")

The `draw_animation()` function will loop through all images in the sprite and it will look like a tiny animation. Awesome !!

You can change the 'fps' by changing the `cycle_time` variable (0.25 is very smooth)

`loop()` loops through all png images in a folder (you might have guessed it) so you can see all possibilities.

Usage:

```sudo python weather-icons.py options```
    
options:
- loop
- image-file.png

example:

```sudo python weather-icons.py loop```

```sudo python weather-icons.py clear-day.png```


## unicorn-hat animations 8x8

|                                | old unicornhat                             |                                                |
|:------------------------------:|:------------------------------------------:|:----------------------------------------------:|
| fog                            | partly-cloudy-day                          | partly-cloudy-night                            |
| ![fog][fog-sd]                 | ![partly-cloudy-day][partly-cloudy-day-sd] | ![partly-cloudy-night][partly-cloudy-night-sd] |
| clear-night                    | clear-day                                  | cloudy                                         |
| ![clear-night][clear-night-sd] | ![clear-day][clear-day-sd]                 | ![cloudy][cloudy-sd]                           |
| rain                           | snow                                       | windy                                          |
| ![rain][rain-sd]               | ![snow][snow-sd]                           | ![windy][windy-sd]                             |
| error                          | raspberry                                  | pimoroni pirate                                |
| ![error][error-sd]             | ![raspberry][raspberry-sd]                 | ![pimoroni_pirate][pimoroni_pirate-sd]         |


[clear-day-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/clear-day.gif "clear-day"
[clear-night-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/clear-night.gif "clear-night"
[cloudy-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/cloudy.gif "cloudy"

[fog-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/fog.gif "cloudy"
[partly-cloudy-day-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/partly-cloudy-day.gif "partly-cloudy-day"
[partly-cloudy-night-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/partly-cloudy-night.gif "partly-cloudy-night"

[rain-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/rain.gif "rain"
[snow-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/snow.gif "snow"
[windy-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/windy.gif "windy"

[error-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/error.gif "error"
[raspberry-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/raspberry.gif "raspberry"
[pimoroni_pirate-sd]: https://github.com/LoveBootCaptain/unicornhat_weather_icons/blob/master/animation/SD/pimoroni.gif "pimoroni pirate"

[Buy the old Unicorn HAT on Pimoroni](https://shop.pimoroni.com/products/unicorn-hat "Buy the old Unicorn HAT on Pimoroni")

For more animations and icons (also in 16x16 for new unicorn-hat-hd) please visit and support the original project by LoveBootCaptain:

[unicornhat_waether_icons by LoveBootCaptain](https://github.com/LoveBootCaptain/unicornhat_weather_icons "Contribute") 





