# template for "Stopwatch: The Game"

import simplegui

# define global variables
counter = 0
mins = 0
sec_1 = 0
sec_2 = 0
tenth_sec = 0
attempts = 0
success = 0
sw_status = "False"
HEIGHT = 200
WIDTH = 200

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(counter):
    global mins, sec_1, sec_2, tenth_sec
    mins = counter // 600
    seconds = (counter % 600) // 10
    sec_1 = seconds // 10
    sec_2 = seconds % 10
    tenth_sec = counter % 10
    return str(mins) + ":" + str(sec_1) + str(sec_2) + "." + str(tenth_sec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global sw_status
    sw_status = "True"
    timer.start()
    
def stop():
    global success, attempts, sw_status
    if (sw_status == "True"):
        attempts += 1
        sw_status = "False"
        if (counter % 10 == 0):
            success +=1
    timer.stop()
    
def reset():
    global counter, success, attempts
    counter = 0
    attempts = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [(WIDTH/2) - 25, HEIGHT/2], 30, "white")
    canvas.draw_text(str(success) + "/" + str(attempts), [150, 30], 20, "yellow")
    
# create frame
frame = simplegui.create_frame("Stopwatch Game!", WIDTH, HEIGHT)
start_button = frame.add_button("Start", start, 50)
stop_button = frame.add_button("Stop", stop, 50)
reset_button = frame.add_button("Reset", reset, 50)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# register event handlers


# start frame
frame.start()

# Please remember to review the grading rubric
