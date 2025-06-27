import socks, socket
from concurrent.futures import ThreadPoolExecutor

def check(proxy):
    ip, port = proxy.split(":")
    try:
        s = socks.socksocket()
        s.set_proxy(socks.SOCKS5, ip, int(port))
        s.settimeout(5)
        s.connect(("www.google.com", 80))
        print(f"[LIVE] {proxy}")
        return proxy
    except:
        return None

with open("proxies.txt") as f:
    proxies = [line.strip() for line in f if line.strip()]

live = []
with ThreadPoolExecutor(max_workers=50) as ex:
    results = list(ex.map(check, proxies))
    live = [r for r in results if r]

with open("live_proxies.txt", "w") as f:
    f.write("\n".join(live))

print(f"Found {len(live)} working proxies.")
