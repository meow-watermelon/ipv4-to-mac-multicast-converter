# Multicast IPv4 Address to MAC Address Converter

## Intro

Multicast IPv4 Address to MAC Address Converter is a small utility to convert a multicast IP address to the MAC address.

## Python Module Dependencies

Following Python modules is needed to run this utility:

```
sys
```

# Usage

```
$ ipv4-to-mac-multicast-converter.py multicast_ip_address
```

# Example

```
$ ./ipv4-to-mac-multicast-converter.py 224.0.64.32
##### Binary IP Representation #####
11100000.00000000.01000000.00100000

##### Binary Lower Bits to Hex Mapping #####
0000000 => 00
01000000 => 40
00100000 => 20

##### Multicast MAC Address ######
01:00:5e:00:40:20

$ ./ipv4-to-mac-multicast-converter.py 224.128.64.32
##### Binary IP Representation #####
11100000.10000000.01000000.00100000

##### Binary Lower Bits to Hex Mapping #####
0000000 => 00
01000000 => 40
00100000 => 20

##### Multicast MAC Address ######
01:00:5e:00:40:20

```
