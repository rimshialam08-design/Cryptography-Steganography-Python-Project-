# **Project Overview**
This project is a simple yet effective implementation of Steganography—the art of hiding a message within another non-secret medium. Using this tool, 
you can take a standard image and inject a secret message into its pixels.

## **🛠️ How it Works**

### **Binary Translation:** 
The script converts your text into a stream of 8-bit binary numbers.
Pixel Manipulation: It iterates through the pixels of the source image and modifies the Red color channel. It changes the "Least Significant Bit" to match the bits of your message.

### **Invisible Changes:**
Because it only changes the color value by a magnitude of 1 (e.g., from 180 to 181), the change is invisible to the human eye.
Extraction: The decoder scans the image, checks if the Red values are even or odd, and reassembles the bits back into text.

## **Key Technical Concepts**

### **Bitwise Operators:** 
Uses & (AND) and | (OR) for precise binary manipulation.

### **Lossless Compression:**
Uses PNG format to prevent data corruption that occurs with JPEG compression.

### **Data Termination:**
Uses a "Null Byte" sequence to signal the end of the hidden message.
