import struct
import math

# Create an empty list to hold the hex values
hex_values = []

# Generate sine values
for i in range(360):
    sine_val = int((math.sin(i * math.pi / 180) + 1) * (2**8-1) / 2)
    hex_val = format(sine_val, '02x')
    # print(hex_val)
    hex_values.append(hex_val)

print(hex_values)

# Create the hex file
with open("eeprom_data.hex", "w") as f:
    f.write(":020000040000FA\n")
    for i in range(0, len(hex_values), 16):
        # address = 0x10001 + i // 2
        address =i
        byte = hex_values[i] + hex_values[i+1]+hex_values[i+2]+hex_values[i+3]+hex_values[i+5]+hex_values[i+6]+hex_values[i+7]+hex_values[i+8]+hex_values[i+9]+hex_values[i+10]+hex_values[i+11]+hex_values[i+12]+hex_values[i+13]+hex_values[i+14]+hex_values[i+15]
        line = ":10{:04X}00{}".format(address, byte)
        checksum = (~(int(line[1:], 16)) & 0xff)
        line += "{:02X}\n".format(checksum)
        f.write(line)
