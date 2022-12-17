import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# import the modules
import os
import json
from os import listdir

# get the path/directory
folder_dir = "/Users/binayatripathi/Desktop/chifi/genart-take2/generative-art-nft/cumulative_code/Day One Individual NFT/regular foil"

# myFont_name = ImageFont.truetype('/Users/binayatripathi/Desktop/chifi/genart-take2/generative-art-nft/texttopng/FONT/futura/futura medium condensed bt.ttf', 32)
# myFont_type = ImageFont.truetype('/Users/binayatripathi/Desktop/chifi/genart-take2/generative-art-nft/texttopng/FONT/futura_mdcn_bt/FuturaMediumCondensedBT.ttf', 20)
# myFont_set = ImageFont.truetype('/Users/binayatripathi/Desktop/chifi/genart-take2/generative-art-nft/texttopng/FONT/futura_mdcn_bt/FuturaMediumCondensedBT.ttf', 16)
# myFont_hp = ImageFont.truetype('/Users/binayatripathi/Desktop/chifi/genart-take2/generative-art-nft/texttopng/FONT/impact/impact.ttf', 20)
# myFont_punch_kick_slam = ImageFont.truetype('/Users/binayatripathi/Desktop/chifi/genart-take2/generative-art-nft/texttopng/FONT/impact/impact.ttf', 22)


file = open("/Users/binayatripathi/Desktop/chifi/genart-take2/generative-art-nft/cumulative_code/attributes_stats_master.json")

data = json.load(file)


# print(data)
print(len(data))
print(data[0]["Health"])

for images in listdir(folder_dir):
    # Open an Image
    img = Image.open(images)
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    file_name = os.path.basename(file_path)


    for i in data:
            # Add Text to an image
        I1.text((337, 455), data[i]["Punch"], fill=(255, 255, 255), font = myFont_punch_kick_slam, stroke_width=2, stroke_fill='black')
        I1.text((275, 523), data[i]["Slam"], fill=(255, 255, 255), font = myFont_punch_kick_slam, stroke_width=2, stroke_fill='black')
        I1.text((397, 523), data[i]["Kick"], fill=(255, 255, 255), font = myFont_punch_kick_slam, stroke_width=2, stroke_fill='black')
        I1.text((108, 115), data[i]["Health"], fill=(255, 255, 255), font = myFont_hp, stroke_width=2, stroke_fill='black')
        I1.text((90, 45), data[i]["Card Name"], fill=(23, 23, 23), font = myFont_name, stroke_width=2, stroke_fill='white')
        I1.text((320, 30), "CHIFIBOT", fill=(34, 32, 32), font = myFont_type, stroke_width=2, stroke_fill='white')
        I1.text((340, 600), "DAYONE", fill=(30, 30, 30), font = myFont_set, stroke_width=1, stroke_fill='white')

        img.save(file_name + ".png", "PNG")

