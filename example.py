#import module
import comm_anode
import time

#create object to control
my_seven_segment_display = comm_cathode.digits(0, 1, 2, 3, 4, 5, 6, 7)

#control object
my_seven_segment_display.demo()

#display different numbers
my_seven_segment_display.one()
time.sleep(1)
my_seven_segment_display.four()
time.sleep(1)

#turn the display off
my_seven_segment_display.reset()