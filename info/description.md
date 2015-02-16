You are given three values.
The first is the correct starting time. 
The second is the current time displayed on the broken clock (which is incorrect). 
Time is given as strings in the format "hh:mm:ss" (Examples: "01:16:59" and "23:00:13").
The third value is a description of the clock error in the format 
`"+(-)N [second, minute, hour](s) at M [second, minute, hour](s)"` 

For Example "+1 second at 10 seconds" -- 
the clock is 1 second fast for every 10 seconds of actual time and 
"-5 minutes at 5 hours" -- the clock lags 5 minutes for every 5 hours of actual time.

You should calculate the real time with the given values.
The result should be rounded down to the nearest second (use floor or int).

Let's examine one example -- '00:00:00', '00:00:30', '+2 seconds at 6 seconds'.

- 0th step: The real and fake time is "00:00:00".
- When the real time is "00:00:06", the fake time is "00:00:08".
- At real "00:00:18", fake is "00:00:24".<br>
- At real "00:00:21", fake is "00:00:28".<br>
- At real "00:00:22", fake is "00:00:29.333...".<br>
- At real "00:00:22.5", fake is "00:00:30".<br>

So answer is "00:00:22.5" after rounding down "00:00:22"
