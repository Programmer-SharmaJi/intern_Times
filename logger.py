import datetime

class LogEntry:
    def __init__(self, message, timestamp=None, severity='INFO', metadata=None):
        self.message = message
        self.timestamp = timestamp if timestamp else datetime.datetime.now()
        self.severity = severity
        self.metadata = metadata if metadata else {}

class CircularLinkedList:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.head = None
        self.size = 0

    def add(self, log_entry):
        if self.size == 0:
            self.head = log_entry
            self.head.next = self.head
        else:
            log_entry.next = self.head.next
            self.head.next = log_entry
            self.head = log_entry
        self.size = min(self.size + 1, self.max_size)

    def display(self):
        current = self.head.next
        while current != self.head:
            print(f"{current.timestamp} [{current.severity}] {current.message}")
            current = current.next
        print(f"{self.head.timestamp} [{self.head.severity}] {self.head.message}")

class Logger:
    def __init__(self):
        self.log_list = CircularLinkedList()

    def log(self, message, severity='INFO', metadata=None):
        log_entry = LogEntry(message, severity=severity, metadata=metadata)
        self.log_list.add(log_entry)

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.log("This is an info message")
    logger.log("This is a warning message", severity='WARNING')
    logger.log("This is an error message", severity='ERROR')
    logger.log("This is a debug message", severity='DEBUG')
    logger.log("This is a critical message", severity='CRITICAL')
    logger.log("This is an emergency message", severity='EMERGENCY')
    logger.log("This is another info message")
    logger.log("This is a notice message", severity='NOTICE')
    logger.log("This is a different warning message", severity='WARNING')
    logger.log("This is a different error message", severity='ERROR')
    logger.log("This is a different debug message", severity='DEBUG')

    logger.log_list.display()
