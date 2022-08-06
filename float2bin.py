import struct
from ast import literal_eval

def float2bin(in_fileName, out_file):

    with open(in_fileName) as f:
        lines = [line.rstrip() for line in f]
    lines_f = [float(line) for line in lines]
    lines_hex = [hex(struct.unpack('<I', struct.pack('<f', f))[0]) for f in lines_f]
    lines_bin = [bin(literal_eval(hx))[2:] for hx in lines_hex]
    with open(out_file, 'w') as fp:
        for item in lines_bin:
            fp.write("%s\n" % item)


in_fileName = 'cos_256_real.txt'
out_file = r'cos_256_bin.txt'
float2bin(in_fileName, out_file)

in_fileName = 'sin_256_imag.txt'
out_file = r'sin_256_bin.txt'
float2bin(in_fileName, out_file)