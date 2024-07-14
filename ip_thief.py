import socket
#Get IP Address Tool Developed By Maimo Harris
print("""
Name:IP-THIEF
Author:MAIMO HARRIS
Contact:+237680226898
""")
print("For Multiple Domain names input Separate Using ',' ")
def get_ip(url):
    ip=socket.gethostbyname(url)
    return ip
link=''
while link!='quit':
    print("Type quit to exit")
    try:
        link=input("Enter site name:")
        for i in link:
            if i==',':
                splited=link.split(",")
                for splits in splited:
                    print(f"{splits}")
                    print(get_ip(splits))
        site_ip=get_ip(link)
        print(site_ip)

    except socket.gaierror:
        print("INVALID INPUT")
print("Exiting Tool")