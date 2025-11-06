# Simple WebSocket Client-Server

This project is a simple number-collecting client-server system using Python and WebSockets.

---

## Setup

1. **Clone or copy the project** to your machine.
2. **Create a virtual environment** in the project folder:

```bash
python3 -m venv venv
```
3. **Activate the virtual environment:**
```bash
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```
4. **Install dependencies:**
```bash
pip install -r requirements.txt
```
## Run the Server
In one terminal:
```bash
python server.py
```
The server will start and listen on `ws://localhost:8765`.
##Run the Client
In another terminal:
```bash
python client.py
```
- Enter numbers one by one.

- Type q when done.

- The client sends the numbers to the server and prints the server's response along with round-trip latency.
