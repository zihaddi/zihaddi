#!/usr/bin/env python3
"""
Animated GIF Creator
Creates an animated GIF where a blue bar moves up and down over an interface mockup background.
"""

from PIL import Image, ImageDraw
import os

def create_interface_mockup(width=400, height=300):
    """Create a simple interface mockup as background."""
    img = Image.new('RGB', (width, height), color='#f0f0f0')  # Light gray background
    draw = ImageDraw.Draw(img)
    
    # Header bar
    draw.rectangle([0, 0, width, 50], fill='#2c3e50')  # Dark blue header
    
    # Title text area
    draw.rectangle([20, 15, 200, 35], fill='#3498db')  # Blue title placeholder
    
    # Navigation buttons
    for i in range(3):
        x = 220 + i * 60
        draw.rectangle([x, 15, x + 50, 35], fill='#34495e')  # Dark gray buttons
    
    # Content area
    draw.rectangle([20, 70, width-20, height-20], fill='white', outline='#bdc3c7')
    
    # Some content lines
    for i in range(5):
        y = 90 + i * 25
        draw.rectangle([40, y, width-40, y+15], fill='#ecf0f1')  # Light content lines
    
    # Sidebar
    draw.rectangle([width-100, 70, width-20, height-20], fill='#ecf0f1', outline='#bdc3c7')
    
    return img

def create_blue_bar(width=80, height=20):
    """Create a blue bar that will move up and down."""
    img = Image.new('RGBA', (width, height), color=(52, 152, 219, 255))  # Blue bar with transparency
    draw = ImageDraw.Draw(img)
    
    # Add a subtle border
    draw.rectangle([0, 0, width-1, height-1], outline=(41, 128, 185, 255), width=2)
    
    # Add a highlight effect
    draw.rectangle([2, 2, width-3, height//2], fill=(93, 173, 226, 128))  # Lighter blue highlight
    
    return img

def create_animated_gif(output_path='animated_bar.gif'):
    """Create the animated GIF with the blue bar moving up and down."""
    
    # Create the background interface mockup
    background = create_interface_mockup()
    bg_width, bg_height = background.size
    
    # Create the blue bar
    blue_bar = create_blue_bar()
    bar_width, bar_height = blue_bar.size
    
    frames = []
    num_frames = 60  # Number of frames for smooth animation
    
    # Calculate movement parameters
    max_y_movement = bg_height - bar_height - 100  # Leave some margin
    min_y = 60  # Start below the header
    max_y = min_y + max_y_movement
    
    for frame in range(num_frames):
        # Create a copy of the background
        frame_img = background.copy()
        
        # Calculate the y position using a sine wave for smooth movement
        import math
        progress = frame / num_frames
        sine_value = math.sin(progress * 2 * math.pi)  # One complete cycle
        y_position = int(min_y + (max_y - min_y) * (sine_value + 1) / 2)
        
        # Position the blue bar (centered horizontally)
        x_position = (bg_width - bar_width) // 2
        
        # Paste the blue bar onto the background
        frame_img.paste(blue_bar, (x_position, y_position), blue_bar)
        
        frames.append(frame_img)
    
    # Save as animated GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=100,  # Duration per frame in milliseconds
        loop=0  # Infinite loop
    )
    
    print(f"Animated GIF created: {output_path}")
    print(f"Frames: {num_frames}")
    print(f"Duration per frame: 100ms")
    print(f"Total animation duration: {num_frames * 100 / 1000:.1f} seconds")

def create_static_images():
    """Create static versions of the images for reference."""
    # Create and save the interface mockup
    interface = create_interface_mockup()
    interface.save('interface_mockup.png')
    print("Created: interface_mockup.png")
    
    # Create and save the blue bar
    bar = create_blue_bar()
    # Create a larger canvas to better show the blue bar
    canvas = Image.new('RGBA', (200, 100), color=(255, 255, 255, 0))
    canvas.paste(bar, (60, 40), bar)
    canvas.save('blue_bar.png')
    print("Created: blue_bar.png")

if __name__ == "__main__":
    print("Creating animated GIF with moving blue bar...")
    
    # Create static reference images
    create_static_images()
    
    # Create the animated GIF
    create_animated_gif()
    
    print("\nFiles created:")
    print("- interface_mockup.png (background image)")
    print("- blue_bar.png (moving element)")
    print("- animated_bar.gif (final animated result)")