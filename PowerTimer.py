import time
from datetime import datetime
from datetime import timedelta
import wone

def PowerTimer(hours: float, intervalInMins: float = 15, outputToCLI: object = False) -> None:
    variable1 = datetime.now()
    intervalInSec = intervalInMins * 60
    numberOfIntervals = int(hours * 60 * 60 / intervalInSec)
    wone.text2speech(
        f"You have selected {round(hours,2)} hours with interval of {intervalInMins} \
        Minutes resulting into {numberOfIntervals} intervals"
    )
    for counter in range(0, numberOfIntervals):
        variable2 = variable1 + timedelta(seconds=intervalInSec)
        time.sleep(intervalInSec - 10)
        wone.text2speech(
            f"Your higness the time right now is {datetime.strftime(datetime.now(),'%H:%M:%S')}, in this time\
            {(counter+1)*100/numberOfIntervals} Percentage of this Power Timer, is about to be completed!\
            Mention your achievements and get ready for the next phase.  Rate your experience in the next 1 minute."
        )
        while variable2 >= datetime.now():
            time.sleep(1)
        wone.bell()
        variable1 += timedelta(seconds=intervalInSec)


PowerTimer(5 / 60, 1)
