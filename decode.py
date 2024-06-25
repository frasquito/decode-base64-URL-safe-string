import base64
import sys

def decode(encoded_str):
    encoded_str = encoded_str.replace('_', '/')
    encoded_str = encoded_str.replace('-', '+')
    return encoded_str

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decode.py <base64_encoded_string>")
        sys.exit(1)
    
    encoded_str = sys.argv[1]
    print("Decoded string:", decode(encoded_str))
