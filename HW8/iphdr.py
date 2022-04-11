import socket
import struct
import binascii

class Iphdr :
    def __init__(self, sport, dport, tot_len, check) :
        self.sport = sport
        self.dport = dport
        self.tot_len = tot_len
        self.check = check

    def pack_Iphdr(self):
        packed = b''
        packed += struct.pack('!4H', self.sport, self.dport, self.tot_len, self.check)
        return packed

def unpack_Iphdr(buffer) : 
    unpacked = struct.unpack('!4H', buffer[:16])
    return unpacked
    
def getSrcPort(unpacked_ipheader) :
    return unpacked_ipheader[0]

def getDstPort(unpacked_ipheader) :
    return unpacked_ipheader[1]

def getLength(unpacked_ipheader) :
    return unpacked_ipheader[2]

def getChecksum(unpacked_ipheader) :
    return unpacked_ipheader[3]

ip = Iphdr(5555, 80, 1000, 0xFFFF)
packed_iphdr = ip.pack_Iphdr()
print(binascii.b2a_hex(packed_iphdr))

unpacked_iphdr = unpack_Iphdr(packed_iphdr)
print(unpacked_iphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}' \
    .format(getSrcPort(unpacked_iphdr), getDstPort(unpacked_iphdr), getLength(unpacked_iphdr), getChecksum(unpacked_iphdr)))