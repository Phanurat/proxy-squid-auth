import requests

# http_port 0.0.0.0:3128
# http_port 0.0.0.0:3129
# http_port 0.0.0.0:3130
# http_port 0.0.0.0:3131
# http_port 0.0.0.0:3132
# http_port 0.0.0.0:3133
# http_port 0.0.0.0:3134
# http_port 0.0.0.0:3135
# http_port 0.0.0.0:3136
# http_port 0.0.0.0:3137
# http_port 0.0.0.0:3138
# http_port 0.0.0.0:3139
# http_port 0.0.0.0:3140

# Proxy settings (basic auth)
proxy = {
    "http": "http://phanurat:1111@192.168.1.152:3128",
    "https": "http://phanurat:1111@192.168.1.152:3128"
}

# Target HTTPS URL
url = "https://example.com"

try:
    response = requests.get(url, proxies=proxy, timeout=10)
    print("Status Code:", response.status_code)
    print("Handshake successful. Content length:", len(response.content))
except requests.exceptions.ProxyError as e:
    print("Proxy Error:", e)
except requests.exceptions.SSLError as e:
    print("SSL Handshake Error:", e)
except Exception as e:
    print("Other Error:", e)
