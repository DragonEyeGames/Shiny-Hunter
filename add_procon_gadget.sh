#!/bin/bash
cd /sys/kernel/config/usb_gadget/

mkdir -p procon
cd procon

echo 0x057e > idVendor
echo 0x2009 > idProduct
echo 0x0200 > bcdDevice
echo 0x0200 > bcdUSB

mkdir -p strings/0x409
echo "000000000001" > strings/0x409/serialnumber
echo "Nintendo Co., Ltd." > strings/0x409/manufacturer
echo "Pro Controller" > strings/0x409/product

mkdir -p configs/c.1/strings/0x409
echo "Pro Controller" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

mkdir -p functions/hid.usb0
echo 0 > functions/hid.usb0/protocol
echo 0 > functions/hid.usb0/subclass
echo 64 > functions/hid.usb0/report_length

# CLEAN SWITCH PRO CONTROLLER REPORT DESCRIPTOR
xxd -r -ps << 'EOF' > functions/hid.usb0/report_desc
0501150009050C0A380215002501750195018102950175088101050109000A000095017508150025017501950881020501090001A1000930093109320935150025FF750895048100C0
EOF

ln -s functions/hid.usb0 configs/c.1/

# bind gadget
UDC=$(ls /sys/class/udc | head -n 1)
echo $UDC > UDC