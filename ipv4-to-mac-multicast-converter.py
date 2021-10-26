#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    ip_address = sys.argv[1]

    # convert decimal IP address to binary format
    ip_address_binary = [bin(int(ip))[2:] for ip in ip_address.split('.')]

    # fill 0s if necessary
    ip_address_binary = [ip.zfill(8) for ip in ip_address_binary]

    print('##### Binary IP Representation #####')
    print('.'.join(ip_address_binary))
    print()

    # acquire the lower 23 bits of the binary IP address
    ip_address_binary_string = ''.join(ip_address_binary)
    ip_address_binary_lower_string = ip_address_binary_string[9:]

    # split the lower string into 7/8/8 bits
    ip_address_binary_lower_bits = [ip_address_binary_lower_string[0:7], ip_address_binary_lower_string[7:15], ip_address_binary_lower_string[15:]]

    # convert the splitted binary lower bits to hexadecimal
    ip_address_hex_lower_bits = [hex(int(bin_bits, base=2))[2:] for bin_bits in ip_address_binary_lower_bits]

    # fill 0s if necessary
    ip_address_hex_lower_bits = [hex_bits.zfill(2) for hex_bits in ip_address_hex_lower_bits]

    print('##### Binary Lower Bits to Hex Mapping #####')
    for c in range(len(ip_address_binary_lower_bits)):
        print('%s => %s' %(ip_address_binary_lower_bits[c], ip_address_hex_lower_bits[c]))
    print()

    # generate the multicast MAC address
    multicast_mac_prefix = '01:00:5e'
    multicast_mac = multicast_mac_prefix+':'+':'.join(ip_address_hex_lower_bits)

    print('##### Multicast MAC Address ######')
    print(multicast_mac)
    print()
