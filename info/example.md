**Example:**

```python
broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') ==  '00:00:10'
broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') ==  '06:10:30'
broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') ==  '14:00:00'
broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') ==  '07:05:05'
broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') ==  '00:00:22'
```
