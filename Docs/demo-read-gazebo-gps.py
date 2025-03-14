from pymavlink import mavutil
master = mavutil.mavlink_connection('udp:localhost:14540')

master.wait_heartbeat()

while True:
    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    if msg:
        lat = msg.lat / 1e7
        lon = msg.lon / 1e7
        alt = msg.alt / 1e3
        print(f"Lat: {lat} Lon: {lon} Alt: {alt}")