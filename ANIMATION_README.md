# Animated GIF Creator

This project creates an animated GIF where a blue bar moves up and down continuously over an interface mockup background.

## Files

- `create_animated_gif.py` - Main script to generate the animated GIF
- `test_animation.py` - Test script to verify the animation was created correctly
- `interface_mockup.png` - Background interface mockup image
- `blue_bar.png` - Blue bar element that moves in the animation
- `animated_bar.gif` - Final animated GIF result

## Usage

### Generate the Animation

Run the main script to create the animated GIF:

```bash
python3 create_animated_gif.py
```

This will create:
- `interface_mockup.png` - A simple interface mockup with header, content area, and sidebar
- `blue_bar.png` - A blue bar with rounded corners and highlight effect
- `animated_bar.gif` - The final animated GIF with smooth up/down movement

### Test the Animation

Verify the animation was created correctly:

```bash
python3 test_animation.py
```

## Animation Details

- **Dimensions**: 400x300 pixels
- **Frame count**: 60 frames for smooth animation
- **Duration**: 100ms per frame (6 seconds total loop)
- **Movement**: Sine wave pattern for smooth up/down oscillation
- **Loop**: Infinite continuous loop

## Customization

You can modify the animation by editing `create_animated_gif.py`:

- Change `num_frames` for different smoothness
- Modify `duration` for faster/slower animation
- Adjust `max_y_movement` for different movement range
- Customize colors and dimensions in the image creation functions

## Requirements

- Python 3.x
- Pillow (PIL) library

Install requirements:
```bash
pip install Pillow
```

## Technical Implementation

The animation uses:
1. **PIL/Pillow** for image manipulation and GIF creation
2. **Sine wave mathematics** for smooth oscillating movement
3. **Alpha blending** for proper transparency handling
4. **Frame-by-frame animation** with consistent timing