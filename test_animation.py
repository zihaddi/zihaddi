#!/usr/bin/env python3
"""
Test script to verify the animated GIF was created correctly.
"""

from PIL import Image
import os

def test_animated_gif():
    """Test that the animated GIF was created with correct properties."""
    gif_path = 'animated_bar.gif'
    
    if not os.path.exists(gif_path):
        print(f"❌ ERROR: {gif_path} not found!")
        return False
    
    try:
        # Open the GIF
        gif = Image.open(gif_path)
        
        # Check basic properties
        print(f"✅ GIF file found: {gif_path}")
        print(f"   Dimensions: {gif.size}")
        print(f"   Format: {gif.format}")
        print(f"   Mode: {gif.mode}")
        
        # Count frames
        frame_count = 0
        try:
            while True:
                gif.seek(frame_count)
                frame_count += 1
        except EOFError:
            pass
        
        print(f"   Frame count: {frame_count}")
        
        # Check if it's animated (more than 1 frame)
        if frame_count > 1:
            print("✅ Animation confirmed: Multiple frames detected")
        else:
            print("❌ ERROR: Only one frame found - not animated")
            return False
        
        # Test that we can read the first and last frames
        gif.seek(0)
        first_frame = gif.copy()
        gif.seek(frame_count - 1)
        last_frame = gif.copy()
        
        print(f"✅ Successfully read first and last frames")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR: Failed to analyze GIF: {e}")
        return False

def test_static_images():
    """Test that the static images were created correctly."""
    images = ['interface_mockup.png', 'blue_bar.png']
    
    for img_path in images:
        if not os.path.exists(img_path):
            print(f"❌ ERROR: {img_path} not found!")
            return False
        
        try:
            img = Image.open(img_path)
            print(f"✅ Static image found: {img_path}")
            print(f"   Dimensions: {img.size}")
            print(f"   Format: {img.format}")
            print(f"   Mode: {img.mode}")
        except Exception as e:
            print(f"❌ ERROR: Failed to open {img_path}: {e}")
            return False
    
    return True

if __name__ == "__main__":
    print("Testing animated GIF creation...")
    print("=" * 50)
    
    static_ok = test_static_images()
    print()
    gif_ok = test_animated_gif()
    
    print("\n" + "=" * 50)
    if static_ok and gif_ok:
        print("✅ All tests passed! Animation created successfully.")
    else:
        print("❌ Some tests failed!")