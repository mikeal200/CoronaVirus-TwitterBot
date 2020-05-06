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