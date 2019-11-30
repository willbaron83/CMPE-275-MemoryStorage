import sys
sys.path.append('~/school/cmpe-275/CMPE-275-MemoryStorage/')

from concurrent import futures

import grpc
import time
import math
import chunk_pb2, chunk_pb2_grpc
from src.MemoryManager import MemoryManager


class ReceiverNode(chunk_pb2_grpc.FileServerServicer):
    memory_manager = None
    num_of_chunks = None

    def __init__(self, memory_node_bytes, page_memory_size_bytes):
        self.memory_manager = MemoryManager(memory_node_bytes, page_memory_size_bytes)

        def save_chunks_to_memory(chunks, hash_id, chunk_size, data_size):
            self.memory_manager.put_data(chunks, hash_id, chunk_size, data_size)
            return True

        class Servicer(chunk_pb2_grpc.FileServerServicer):

            def upload(self, request_iterator, context):
                hash_id = ""
                chunk_size = 0
                data_size = 0

                for key, value in context.invocation_metadata():
                    if key == "key-hash-id":
                        hash_id = value
                    elif key == "key-chunk-size":
                        chunk_size = int(value)
                    elif key == "key-data-size":
                        data_size = int(value)

                assert hash_id != ""
                assert chunk_size != 0
                assert data_size != 0

                success = save_chunks_to_memory(request_iterator, hash_id, chunk_size, data_size)
                return chunk_pb2.Reply(success=success)

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        chunk_pb2_grpc.add_FileServerServicer_to_server(Servicer(), self.server)

    def start(self, port):
        self.server.add_insecure_port(f'[::]:{port}')
        self.server.start()

        try:
            while True:
                time.sleep(60*60*24)  # should infinity
        except KeyboardInterrupt:
            self.server.stop(0)


if __name__ == '__main__':
    total_memory_node_bytes = 1024 * 1024 * 1024  # start with 1 GB
    total_page_memory_size_bytes = 1024  # start with 1 KB
    receiver_node = ReceiverNode(total_memory_node_bytes, total_page_memory_size_bytes)
    print("Node is READY")
    receiver_node.start(5555)
