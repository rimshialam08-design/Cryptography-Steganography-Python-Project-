from PIL import Image
import os

def text_to_bits(text):
  bits = []
  for char in text:
    bin_val = bin(ord(char))[2:].zfill(8)
    bits.extend([int(b) for b in bin_val])
  bits.extend([0] * 8)
  return bits

def bits_to_text(bits):
  chars = []
  for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    char_code = int("".join(map(str, byte)), 2)
    if char_code == 0:  
      break
    chars.append(chr(char_code))
  return "".join(chars)

def encode_message():
  print("--- MANUAL LSB ENCODER ---")
  path = input("Enter source image path: ").strip().strip('"')
  if not os.path.exists(path): return None

  message = input("Enter secret message: ")
  output_name = input("Enter output name (e.g., manual.png): ")

  img = Image.open(path).convert('RGB')
  pixels = img.load()
  width, height = img.size
    
  bits = text_to_bits(message)
  bit_index = 0

  for y in range(height):
    for x in range(width):
      if bit_index < len(bits):
        r, g, b = pixels[x, y]
                
        r = (r & 254) | bits[bit_index]
        bit_index += 1
                
        pixels[x, y] = (r, g, b)
      else:
        img.save(output_name)
        print(f"Success! Saved to {output_name}")
        return output_name

def decode_message(path):
  print("\n--- MANUAL LSB DECODER ---")
  img = Image.open(path).convert('RGB')
  pixels = img.load()
  width, height = img.size
    
  extracted_bits = []
  for y in range(height):
    for x in range(width):
      r, g, b = pixels[x, y]
      extracted_bits.append(r & 1)
            
      if len(extracted_bits) % 8 == 0:
        if extracted_bits[-8:] == [0, 0, 0, 0, 0, 0, 0, 0]:
          print(f"Hidden Message: {bits_to_text(extracted_bits)}")
          return

saved_file = encode_message()
if saved_file:
  decode_message(saved_file) 