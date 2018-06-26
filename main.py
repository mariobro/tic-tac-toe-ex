# We use ZMQ to talk to the game server. The basic
# communication is set up so you shouldn't need to worry about it much
import zmq
import sys

PORT = 5556

# Connect to the game server,
# Make sure it is running
print("Connecting to server")

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(f'tcp://127.0.0.1:{PORT}')

print("Connected!")

# Connect to the server using it's API
socket.send_string('start')

# Make this function!
def get_move():
    return '0,0'

while True:
    sys.stdout.flush()

    # Get the next message from the server. Note that it may be multi-line
    message = socket.recv_string()

    # If the server replies 'done', the game is finished
    if message == 'done':
        break

    # Message contains game state information,
    # You'll want to parse message and construct
    # a valid response
    reply = get_move()

    # Send reply to the server
    socket.send_string(reply)
