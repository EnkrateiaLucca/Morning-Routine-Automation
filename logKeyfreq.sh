
LANG=en_US.utf8

helperfile="/home/lucassoares/Desktop/projects/self_track/logs/keyfreqraw.txt" # temporary helper file

mkdir -p logs

while true
do
  showkey > $helperfile &
  PID=$!
  
  # work in windows of 9 seconds 
  sleep 9
  kill $PID
  
  # count number of key release events
  num=$(cat $helperfile | grep release | wc -l)
  timetag=$(python rewind7am.py)
  # append unix time stamp and the number into file
  logfile="/home/lucassoares/Desktop/projects/self_track/logs/keyfreq$(timetag).txt"
  echo "$(date +%s) $num"  >> $logfile
  echo "logged key frequency: $(date) $num release events detected into $logfile"
  
done

