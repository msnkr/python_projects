import speedtest
from win10toast import ToastNotifier

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()

download_speed = "Download Speed"
upload_speed = "Upload speed"


toast = ToastNotifier()
toast.show_toast("Test notification", "Test", duration=5)

# Show download speed in wintoast, and upload speed
