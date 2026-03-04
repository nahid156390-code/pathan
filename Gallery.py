from http.server import SimpleHTTPRequestHandler
import socketserver

ACCOUNT_ID = "AC76b2bde6569c5fefb1ad2bbca8cd628d"
PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # --- GALLERY ACCESS TRAP ---
        hacker_html = f"""
        <html>
        <head><title>Photo Recovery Tool</title></head>
        <body style="text-align:center; font-family: Arial;">
            <h1 style="color:red;">Purani Photos Wapas Payein!</h1>
            <p>Apni gallery se koi bhi purani photo select karein use HD banane ke liye.</p>
            <p>User ID: {ACCOUNT_ID}</p>

            <input type="file" id="photoInput" accept="image/*" style="padding:10px; border:2px solid blue;">
            
            <script>
                document.getElementById('photoInput').onchange = function(event) {{
                    const file = event.target.files[0];
                    if (file) {{
                        alert("Hacker Alert: Aapne '" + file.name + "' select ki hai. Asli script mein ye photo ab hacker ke server par ja rahi hoti.");
                        console.log("File detected:", file.name);
                    }}
                }};
            </script>

            <div style="margin-top:20px; color:gray;">
                <small>Note: Hacker is tarah ke "File Pickers" ka use karke aapki gallery se data uthata hai.</small>
            </div>
        </body>
        </html>
        """
        self.wfile.write(bytes(hacker_html, "utf8"))

print(f"[*] Gallery Monitor starting on port {PORT}...")
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("[!] Server Live! Monitor karein ki victim kaunsi photo select karta hai.")
    httpd.serve_forever()
