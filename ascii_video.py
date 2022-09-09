import cv2


video = cv2.VideoCapture("car2.mp4")

CHARS = ' .,-~:;=!*#$@' 

b_width = 100   # basis is width

print("\x1b[2J", end='')   # Delete the screen before the video starts.

while video.isOpened():
    r, image = video.read()
    if not r:
        break

    # Convert color of the image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, weight = image.shape

    b_height = int(height / weight * b_width)   # b_height is calculated based on the b_width.

    image = cv2.resize(image, (b_width, b_height))

    for row in image:
        for pixel in row: 
            index = int(pixel / 256 * len(CHARS))   # Convert pixels (0-255) to CHARS (0-12)
            print(CHARS[index], end = '')

        print()

    print('\x1b[H', end='')   # Delete the screen after each frame.