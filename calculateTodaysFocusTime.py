from utils import loadFocus
import pandas as pd
from datetime import datetime

today = datetime.strftime(datetime.today(),format="%Y-%m-%d")
timeStartsStamp,dateStartsStamp,durations = loadFocus()
df = pd.DataFrame(dict(dates=dateStartsStamp, durations=durations))
todayFocus = df[df["dates"]==today]["durations"].sum()
print(todayFocus)
