pkill -f display.py
pkill -f sound.py
pkill -f motion.py
python minimop/display.py &
python minimop/sound.py &
python minimop/motion.py &
