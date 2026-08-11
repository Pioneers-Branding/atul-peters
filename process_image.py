from PIL import Image
import numpy as np

try:
    # Load the image
    img = Image.open('C:/Users/Manish Kushwaha/.gemini/antigravity-ide/brain/02cce9e5-47cf-4850-8c27-1c55530764c5/sketch_atul_peters_1786076872870.png').convert('RGBA')
    data = np.array(img)

    # Calculate luminance
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    luminance = 0.299 * r + 0.587 * g + 0.114 * b

    # White is 255 (alpha=0), black is 0 (alpha=255)
    new_alpha = np.clip(255 - luminance, 0, 255)

    # Set RGB to theme color #1D5D95 (Dark Blue/Teal)
    data[:,:,0] = 29
    data[:,:,1] = 93
    data[:,:,2] = 149
    data[:,:,3] = new_alpha

    # Save the new transparent PNG
    new_img = Image.fromarray(data.astype('uint8'), 'RGBA')
    new_img.save('e:/atul-peters/atul-peters/assets/img/sketch_atul_peters_transparent.png')
    print("Image processed successfully!")
except Exception as e:
    print(f"Error: {e}")
