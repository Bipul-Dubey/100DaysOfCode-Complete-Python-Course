import colorgram
colors=colorgram.extract('image.jpg',20)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    real_color=(r,g,b)
    rgb_colors.append(real_color)

print(rgb_colors)