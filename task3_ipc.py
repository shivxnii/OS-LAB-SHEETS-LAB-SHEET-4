from multiprocessing import Process, Pipe

def child_process(conn):
    message = conn.recv()        # receive message from parent
    print("Child received:", message)
    conn.send("Hello from child")  # send reply to parent
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    p = Process(target=child_process, args=(child_conn,))
    p.start()

    parent_conn.send("Hello from parent")   # send message to child
    reply = parent_conn.recv()              # receive reply
    print("Parent received:", reply)

    p.join()
