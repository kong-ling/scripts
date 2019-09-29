from PyCRC.CRC16 import CRC16
from PyCRC.CRC16DNP import CRC16DNP
from PyCRC.CRC16Kermit import CRC16Kermit
from PyCRC.CRC16SICK import CRC16SICK
from PyCRC.CRC32 import CRC32
from PyCRC.CRCCCITT import CRCCCITT
#import PyCRC
input = '1234567890'
print('%s' % CRC16().calculate(input))
print('%s' % CRC16DNP().calculate(input))
print('%s' % CRC16Kermit().calculate(input))
print('%s' % CRC16SICK().calculate(input))
print('%s' % CRC32().calculate(input))
print('%s' % CRCCCITT().calculate(input))
