import cv2
import numpy as np


def is_similar(image1, image2):
    return image1.shape == image2.shape and not (np.bitwise_xor(image1, image2).any())


stage = cv2.imread("Stage.png")
images = []
for i in range(0, stage.shape[0], 16):
    for j in range(0, stage.shape[1], 16):
        new_image = True
        for image in images:
            if is_similar(image, stage[i:i + 16, j:j + 16]):
                new_image = False
        if new_image:
            images.append(stage[i:i + 16, j:j + 16].copy())

for index, image in enumerate(images, start=1):
    cv2.imwrite(f"images/{index}.png", image)

cnt = 0
with open("tiles.txt", "w") as f:
    for i in range(0, stage.shape[0], 16):
        row = []
        for j in range(0, stage.shape[1], 16):
            for index, image in enumerate(images, start=1):
                if not is_similar(stage[i:i + 16, j:j + 16], image):
                    continue
                row.append(index)
                if index == 1 or index == 11:
                    cnt+=1
        f.write(' '.join(map(str, row))+'\n')

print(cnt)