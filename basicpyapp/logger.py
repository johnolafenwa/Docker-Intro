from io import open
import os
import uuid

#Path to store the logs
DATA_DIR = "/logs"

#Create the path if it doesn't exist
if os.path.exists(DATA_DIR) == False:
    os.mkdir(DATA_DIR)

#Number of logs previously created
num_logs = len(os.listdir(DATA_DIR))

print("Number of Logs : {}".format(num_logs))

#Filename for new log
new_log_file_name = str(uuid.uuid4()) + ".txt"

#Write new log file to data dir
open(os.path.join(DATA_DIR,new_log_file_name),mode="w")