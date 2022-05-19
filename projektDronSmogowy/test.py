import time
from rdsDB import database_handler

ins = database_handler()

to_contiune = True;
while(to_contiune):
    for value in range(1,100):
        ins.insert_values_measurement(value,2,3,4,5,6,7,8,9)
        time.sleep(1)
    if (value == 99):
        to_contiune = False



