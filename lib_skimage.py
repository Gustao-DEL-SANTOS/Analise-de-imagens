from matplotlib import pyplot as plt

from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean

moon = io.imread('digital_b.jpg', as_gray=True)
img = resize(moon, (200, 200), anti_aliasing=False)
plt.imshow(moon, cmap='gray')