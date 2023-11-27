import speedtest
from plyer import notification


def senf_notification(download, upload):

    new_download = download * 8 / 10 ** 6
    new_upload = upload * 8 / 10 ** 6

    notification.notify(
        title="Your speeds",
        message="Download: {:.2f}mbs\nUpload: {:.2f}mbps".format(
            new_download, new_upload),
        timeout=5
    )


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
senf_notification(results_dict["download"], results_dict["upload"])
