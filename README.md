# proxy-squid-auth

## /etc/squid/passwd

#       WELCOME TO SQUID 5.9
#       ----------------------------
# กำหนด port ของ proxy
http_port 0.0.0.0:3128
http_port 0.0.0.0:3129

# ตั้งค่า basic authentication
auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic realm Proxy
auth_param basic credentialsttl 2 hours

# สร้าง ACL สำหรับผู้ใช้ที่ authenticated
acl authenticated proxy_auth REQUIRED

# อนุญาตเฉพาะผู้ใช้ที่ authenticated
http_access allow authenticated

# ปฏิเสธทุกคนอื่น
http_access deny all
