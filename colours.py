import webcolors


palette_2 = ['#1A82FF', '#FF9E06']
palette_4 = ['#007929', '#024E68', '#A65500', '#A61A00']
my_palette = ['#00BB3F',	'#238C47',	'#007929',	'#37DD6F',	'#63DD8D',
              '#06799F',	'#216278',	'#024E68',	'#3AAACF',	'#61B4CF',
              '#FF8300',	'#BF7930',	'#A65500',	'#FFA240',	'#FFBB73',
              '#FF2800',	'#BF4630',	'#A61A00',	'#FF5D40',	'#FF8973']


def to_hex(t):
    a = '#'
    for y in t:
        a += '%02x' % y
    return a


def opacity_conv(palette, alpha):
    weaker = [webcolors.hex_to_rgb(h) for h in palette]
    weaker = [make_rgb_transparent(h, alpha) for h in weaker]
    weaker = [to_hex(h) for h in weaker]
    return weaker


def make_rgb_transparent(rgb, alpha):
    return tuple(int(alpha * c1 + (1 - alpha) * c2) for (c1, c2) in zip(rgb, (255, 255, 255)))
