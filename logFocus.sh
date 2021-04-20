logfile="/home/lucassoares/Desktop/projects/self_track/logs/focus.txt"
start="$(date +%s)"
echo "Started logging focus"
read stop
echo "Stopped recording focus"
echo "Calculating focus time"
end="$(date +%s)"
echo "$start $end" >> $logfile
/home/lucassoares/anaconda3/envs/main/bin/python /home/lucassoares/Desktop/projects/self_track/scripts/calculateTodaysFocusTime.py
