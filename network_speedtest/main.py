import speedtest
from plyer import notification


def senf_notification(download, upload):
    bits = 8
    mbs_conversion = 1 / 1_000_000

    new_download = download * bits * mbs_conversion
    new_upload = upload * bits * mbs_conversion

    notification.notify(
        title="Your speeds",
        message=f"Download: {new_download:.2f}\nUpload: {new_upload:.2f}",
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
