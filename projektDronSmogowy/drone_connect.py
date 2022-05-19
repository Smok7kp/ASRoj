from pymavlink import mavutil
import sys
import time

# the_connection = mavutil.mavlink_connection('/dev/ttyACM0')

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
# the_connection.wait_heartbeat()
# print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

    
# try: 
#     altitude=the_connection.messages['GPS_RAW_INT'].alt  # Note, you can access message fields as attributes! 
#     longtitude = the_connection['GPS_RAW_INT'].long
#     latitude = the_connection['GPS_RAW_INT'].lat
#     timestamp=the_connection.time_since('GPS_RAW_INT')
#     print("alit")
#     print(altitude)
#     print("Time is " + str(timestamp))
#     print("Longitutde"+ str(longtitude))
#     print("Latitude is "+ str(latitude))
   

# except:
#     print('No GPS_RAW_INT message received')


# master = mavutil.mavlink_connection('/dev/ttyACM0')
# # Wait a heartbeat before sending commands
# master.wait_heartbeat()

# # Request all parameters



# try: 
#     altitude = master.messages['GPS_RAW_INT'].alt  # Note, you can access message fields as attributes!
#     timestamp = master.time_since('GPS_RAW_INT')
# except:
#     print('No GPS_RAW_INT message received')






############33


from pymavlink import mavutil

# Start a connection listening to a UDP port
the_connection = mavutil.mavlink_connection('/dev/ttyACM0')

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link

to_continue = True
while(to_continue):
    the_connection.wait_heartbeat()
    print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))
    if(the_connection.target_system == 0):
        the_connection.wait_heartbeat()
    else:
        time.sleep(1)
        altitude = the_connection.messages['GPS_RAW_INT'].lat  # Note, you can access message fields as attributes!
        longtitude = the_connection.messages['GPS_RAW_INT'].lon 
        satelite = the_connection.messages['GPS_RAW_INT'].satellites_visible
        timestamp = the_connection.time_since('GPS_RAW_INT')
        print(longtitude)
        print(altitude)
        print(satelite)
