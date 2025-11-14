# Calculates storage needed for a file in blocks of 4096 bytes
def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size  # Full blocks used
    partial_block_remainder = filesize % block_size  # Check for remainder

    if partial_block_remainder > 0:  # If remainder, add one more block
        return (full_blocks + 1) * block_size
    return full_blocks * block_size  # Otherwise, return full blocks

print(calculate_storage(1))    # 1 byte → 4096 bytes
print(calculate_storage(4096)) # 4096 bytes → 4096 bytes
print(calculate_storage(4097)) # 4097 bytes → 8192 bytes
print(calculate_storage(6000)) # 6000 bytes → 8192 bytes