from serial import Serial
import pynmea2
import serial.tools.list_ports


PORT = "/dev/ttyUSB0"
BAUD = 4800


def enumerate_usb():
    # Enumerate available USB deives
    for port in serial.tools.list_ports.comports():
        print(f"FOUND DEVICE {port.vid:04x}:{port.pid:04x} {port.device:15} ", end="")
        print(f"{port.manufacturer} {port.product} {port.serial_number}")


def read_gps(port, baud):
    # read gps output and forward to home assistant
    with Serial(port, baud) as dev:
        while True:
            line = dev.readline().decode()
            # print(line)
            try:
                msg = pynmea2.parse(line)
                print(f"{msg.num_sats}/{msg.gps_qual}", end="") 
                print(f" {msg.timestamp}", end="")
                print(f" {msg.latitude:7.3f}{msg.lat_dir}/{msg.longitude:8.3f}{msg.lon_dir}", end="")
                print(f" {msg.altitude:.0f}m")
            except (AttributeError, pynmea2.ParseError):
                pass
                # print(" ERR")


enumerate_usb()
print("connect to GPS", PORT)
read_gps(PORT, BAUD)