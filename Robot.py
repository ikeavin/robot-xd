import Greet
import Walk
import Bake

LAST_STATE = "START"
health = 5
anger = 6

while True:
    if LAST_STATE == "START":
        Greet.main()
        LAST_STATE = "Greet"
        continue
        
    if LAST_STATE == "Greet":
        Walk.main()
        LAST_STATE = "Walk"
        continue
        
    break