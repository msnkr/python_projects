from datetime import datetime
from plyer import notification, temperature


title = "This is a title"
message = "This is a message"


notification.notify(title, message, toast=True, timeout=3)
