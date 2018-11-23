custom_process.py is a class that holds the logic that a worker thread would need to manage its own clock and merging with other clocks

test.py holds all the tests. They are divided into unit tests and end to end tests. The unit tests checks if the specific functions of comparing vector clocks work by hard coding the vectors and checking if the algorithms can correctly identify which vector clocks are before, after, and which are concurrent. The next part is to run a simulation as follows:

0 does an event and then tells 1 about it, after this it continues to do another event  
1 receives the message from 0 and sends messages to 0 and 2  
At this point 1 has moved on in the vector clock and so has 2. 0 has also moved on as it did an event without notifying the others, so when 2 sends a message to 0, 0 has to take into account 1's new clock, and 2's new clock, while keeping it's own new clock. It does so successfully in the test.
