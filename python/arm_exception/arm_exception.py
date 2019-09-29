# data abort analysis based on registers
# recorded at: http://www.keil.com/support/docs/3080.htm

#if application is trying to read or write an illegal memory location,
# Data Abort will be triggered

#link registers
R14 = 0x0000021e
print('R14 contents:[ 0x%08X ]' % R14)

# the instuction that caused the exception
illegal_memory_location = R14 - 8
print('instuction caused the exception:[ 0x%08X ]' % illegal_memory_location)

#disasemble the instuction using the Unassemble debug command in JTAG debug(ULINK)
# View - Command Window
print('please type: "U 0x%08X" in Command window' % illegal_memory_location)
