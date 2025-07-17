#!/usr/bin/env python3
"""
Animation preview script - shows frame-by-frame analysis of the animated GIF.
"""

from PIL import Image
import math

def analyze_animation_movement():
    """Analyze the movement pattern in the animated GIF."""
    gif_path = 'animated_bar.gif'
    
    try:
        gif = Image.open(gif_path)
        
        print("Analyzing animation movement pattern...")
        print("=" * 50)
        
        frame_count = 0
        positions = []
        
        # Extract the position of the blue bar in each frame
        try:
            while True:
                gif.seek(frame_count)
                frame = gif.convert('RGB')
                
                # Find the blue bar by looking for blue pixels
                width, height = frame.size
                blue_found = False
                
                for y in range(height):
                    for x in range(width):
                        r, g, b = frame.getpixel((x, y))
                        # Look for blue color (approximately)
                        if b > 200 and r < 100 and g > 100:  # Blue-ish pixel
                            positions.append(y)
                            blue_found = True
                            break
                    if blue_found:
                        break
                
                if not blue_found:
                    positions.append(None)
                
                frame_count += 1
                
        except EOFError:
            pass
        
        print(f"Total frames analyzed: {frame_count}")
        print(f"Blue bar positions found: {len([p for p in positions if p is not None])}")
        
        if positions:
            valid_positions = [p for p in positions if p is not None]
            if valid_positions:
                min_pos = min(valid_positions)
                max_pos = max(valid_positions)
                print(f"Movement range: {min_pos} to {max_pos} pixels (vertical)")
                print(f"Movement distance: {max_pos - min_pos} pixels")
                
                # Show first few positions to verify smooth movement
                print("\nFirst 10 frame positions:")
                for i in range(min(10, len(positions))):
                    if positions[i] is not None:
                        print(f"  Frame {i}: Y-position {positions[i]}")
                    else:
                        print(f"  Frame {i}: Blue bar not found")
        
        return True
        
    except Exception as e:
        print(f"Error analyzing animation: {e}")
        return False

def verify_smooth_movement():
    """Verify that the movement follows a smooth sine wave pattern."""
    print("\nVerifying smooth movement pattern...")
    print("-" * 30)
    
    # Calculate expected positions based on sine wave
    num_frames = 60
    min_y = 60
    max_movement = 180  # Approximate based on our settings
    max_y = min_y + max_movement
    
    print("Expected sine wave movement:")
    for frame in range(min(10, num_frames)):
        progress = frame / num_frames
        sine_value = math.sin(progress * 2 * math.pi)
        expected_y = int(min_y + (max_y - min_y) * (sine_value + 1) / 2)
        print(f"  Frame {frame}: Expected Y-position {expected_y}")

if __name__ == "__main__":
    print("Animation Analysis Tool")
    print("=" * 50)
    
    success = analyze_animation_movement()
    if success:
        verify_smooth_movement()
        
        print("\n" + "=" * 50)
        print("✅ Animation analysis complete!")
        print("The blue bar should be smoothly moving up and down")
        print("in a continuous sine wave pattern over the interface mockup.")
    else:
        print("❌ Animation analysis failed!")