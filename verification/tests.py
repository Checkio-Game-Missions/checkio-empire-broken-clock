"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["00:00:00", "00:00:15", "+5 seconds at 10 seconds"],
            "answer": "00:00:10"
        },
        {
            "input": ["06:10:00", "06:10:15", "-5 seconds at 10 seconds"],
            "answer": "06:10:30"
        },
        {
            "input": ["13:00:00", "14:01:00", "+1 second at 1 minute"],
            "answer": "14:00:00"
        },
        {
            "input": ["01:05:05", "04:05:05", "-1 hour at 2 hours"],
            "answer": "07:05:05"
        },
        {
            "input": ["00:00:00", "00:00:30", "+2 seconds at 6 seconds"],
            "answer": "00:00:22"
        },
        {
            "input": ["03:14:10", "10:20:30", "+4 minutes at 2 hours"],
            "answer": "10:06:44"
        },
        {
            "input": ["11:02:00", "20:30:10", "-5 seconds at 1 hour"],
            "answer": "20:30:57"
        },
        {
            "input": ["12:10:00", "14:00:30", "+23 minutes at 1 hour"],
            "answer": "13:29:52"
        },
        {
            "input": ["01:10:00", "23:10:30", "-2 seconds at 2 hours"],
            "answer": "23:10:52"
        },
        {
            "input": ["13:02:00", "15:00:30", "+1 hour at 3 hours"],
            "answer": "14:30:52"
        },
        {
            "input": ["03:48:20", "08:54:30", "-2 hours at 3 hours"],
            "answer": "19:06:50"
        },
        {
            "input": ["04:46:04", "10:03:30", "+5 minutes at 14 minutes"],
            "answer": "08:39:57"
        },
        {
            "input": ["01:16:43", "04:22:30", "+1 minute at 150 seconds"],
            "answer": "03:29:25"
        },
        {
            "input": ["18:20:11", "20:20:30", "+1 hour at 123 minutes"],
            "answer": "19:41:03"
        },
        {
            "input": ["13:21:11", "20:20:30", "-1 hour at 10600 seconds"],
            "answer": "23:56:08"
        }
    ],
    "Extra": [
        {
            "input": ["03:14:10", "10:20:30", "+3 minutes at 2 hours"],
            "answer": "10:10:06"
        },
        {
            "input": ["11:02:00", "20:30:10", "-6 seconds at 1 hour"],
            "answer": "20:31:06"
        },
        {
            "input": ["12:10:00", "14:00:30", "+13 minutes at 1 hour"],
            "answer": "13:40:49"
        },
        {
            "input": ["01:10:00", "23:10:30", "-21 seconds at 2 hours"],
            "answer": "23:14:21"
        },
        {
            "input": ["13:02:00", "15:00:30", "+1 hour at 4 hours"],
            "answer": "14:36:48"
        },
        {
            "input": ["03:48:20", "08:54:30", "-2 hours at 5 hours"],
            "answer": "12:18:36"
        },
        {
            "input": ["04:46:04", "10:03:30", "+4 minutes at 34 minutes"],
            "answer": "09:30:05"
        },
        {
            "input": ["01:16:43", "04:22:30", "+1 minute at 250 seconds"],
            "answer": "03:46:32"
        },
        {
            "input": ["18:20:11", "20:20:30", "+1 hour at 135 minutes"],
            "answer": "19:43:28"
        },
        {
            "input": ["13:21:11", "20:20:30", "-1 hour at 12000 seconds"],
            "answer": "23:20:12"
        }
    ]
}
