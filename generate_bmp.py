#!/usr/bin/env python3

def create_green_square_bmp(filename, size=24):
    """Create a simple BMP file with a green square."""
    
    # BMP file structure:
    # - File Header (14 bytes)
    # - Info Header (40 bytes) 
    # - Pixel data (size * size * 3 bytes for 24-bit RGB)
    
    # Calculate sizes
    pixel_data_size = size * size * 3  # 3 bytes per pixel (RGB)
    # Add padding to make each row a multiple of 4 bytes
    row_size = ((size * 3 + 3) // 4) * 4
    padded_pixel_data_size = row_size * size
    file_size = 54 + padded_pixel_data_size  # 54 = header sizes
    
    # BMP File Header (14 bytes)
    file_header = bytearray([
        0x42, 0x4D,  # "BM" signature
        *file_size.to_bytes(4, 'little'),  # File size
        0x00, 0x00, 0x00, 0x00,  # Reserved
        0x36, 0x00, 0x00, 0x00   # Offset to pixel data (54 bytes)
    ])
    
    # BMP Info Header (40 bytes)
    info_header = bytearray([
        0x28, 0x00, 0x00, 0x00,  # Header size (40)
        *size.to_bytes(4, 'little'),  # Width
        *size.to_bytes(4, 'little'),  # Height
        0x01, 0x00,  # Color planes (1)
        0x18, 0x00,  # Bits per pixel (24)
        0x00, 0x00, 0x00, 0x00,  # Compression (none)
        *padded_pixel_data_size.to_bytes(4, 'little'),  # Image size
        0x13, 0x0B, 0x00, 0x00,  # X pixels per meter (2835)
        0x13, 0x0B, 0x00, 0x00,  # Y pixels per meter (2835)
        0x00, 0x00, 0x00, 0x00,  # Colors used (0 = all)
        0x00, 0x00, 0x00, 0x00   # Important colors (0 = all)
    ])
    
    # Create pixel data (green color: BGR format in BMP)
    # Green = (0, 255, 0) in RGB, but BMP uses BGR so it's (0, 255, 0)
    pixel_data = bytearray()
    padding = row_size - (size * 3)
    
    for y in range(size):
        for x in range(size):
            pixel_data.extend([0x00, 0xFF, 0x00])  # BGR: Blue=0, Green=255, Red=0
        # Add padding bytes to make row size multiple of 4
        pixel_data.extend([0x00] * padding)
    
    # Write the BMP file
    with open(filename, 'wb') as f:
        f.write(file_header)
        f.write(info_header)
        f.write(pixel_data)
    
    print(f"Created {filename} - a {size}x{size} green square BMP file")

if __name__ == "__main__":
    create_green_square_bmp("test/assets/green_square.bmp", 24)