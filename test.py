from mss import mss
from PIL import Image


with mss() as sct:
    for num, monitor in enumerate(sct.monitors):
        # Get raw pixels from the screen.
        # This method will store screen size into `width` and `height`
        # and raw pixels into `image`.
        sct.get_pixels(monitor)

        # Create an Image:
        img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)

        # And save it!
        img.save('monitor-{0}.jpg'.format(num))
