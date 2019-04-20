# Priority-Message-Retriever


# Write Up
 - I created my 2 classes one for logging and one for logReading
    - The logging class initializes the queues and takes in all the logs using the .log(message, priority) function
      - In the logging class I used 3 queues one for each priority level
    - The logReader class is initialized using an instance of the logging class and reads all the logs using the .get() function
    
# Answers
 - We don’t want memory to increase unbounded. How will you solve this? How will you make it aware when this happens?
    - We use queues in the classes so when the logReader class reads the logs the log will be popped off the queue
    - This will happen every time the .get() function is called within the logReader class
 - How would you decorate the retrieved log message with other information? Such as date, time, priority, thread name, class name, etc..
    - As you can see I included date, time and priority when reading the logs with the LogReader class
    - To add the thread name and class name
      - I would just append those values to the list the would be put into the queues
      - Then when reading the logs I would include the class name and thread name information

 
