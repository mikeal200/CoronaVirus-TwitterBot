def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_date = str(file_read.read().strip())
    file_read.close()
    return last_seen_date

def store_last_seen(FILE_NAME, last_seen_date):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_date))
    file_write.close()
    return

def store_prev_confirmed(FILE_NAME, prev_confirmed):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(prev_confirmed))
    file_write.close()
    return

def read_prev_confirmed(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    prev_confirmed = str(file_read.read().strip())
    file_read.close()
    return prev_confirmed