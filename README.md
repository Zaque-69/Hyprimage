<p align = "left">
  <img width="300" alt="webui" src="https://github.com/Zaque-69/Hyprimage/blob/main/hyprimage.png">
</p>

# Hyprimage

<b>Hyprimage</b> it's a Python script to get the main colors from an image and build a theme for your Hyprland configuration. Don't try to understand the code, it's pretty trashy.

Update 16.12.2024 : The code is still trash, now organised in functions 🤯

# Commands

```
python main.py -p /path/to/your/image
```
- after running the previous command, a directory will be created ( local ). There will be 4 different color palettes. After have you decided what palette you like the most, you need to run the following command to change the style of your Hyprland apps, also including Kitty : 

```
python main.py -c { number_of_palette }
```
- generating configurations for the apps : "kitty", "wlogout", "wofi". Nr = number of palette image (from 0 to 1000). ex :

```
python main.py -t { number_of_configuration }
```
- Here are your configurations of your images. In "backgrounds" save your image with ".png" extension and with the same name as your image write a file in "theme" with a list of colors, one on each line
