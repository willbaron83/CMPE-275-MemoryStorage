import os
from concurrent import futures

import grpc
import time
import hashlib

import chunk_pb2, chunk_pb2_grpc

CHUNK_SIZE = 1024   # 1MB // the server (receiver node) must also be configured to take the same chunk size


def get_file_chunks(filename, chunk_size):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                return
            yield chunk_pb2.Chunk(buffer=chunk)


def generate_hash_id(app_name, file_name):
    name_path = app_name+file_name
    hash_object = hashlib.sha1(name_path.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


class SenderNode:
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.stub = chunk_pb2_grpc.FileServerStub(channel)

    def upload(self, app_name, file_name, file_path, file_data_size_bytes):

        hash_id = generate_hash_id(app_name, file_name)

        metadata = (
            ('key-hash-id', hash_id),
            ('key-chunk-size', str(CHUNK_SIZE)),
            ('key-data-size', str(file_data_size_bytes))
        )

        chunks_generator = get_file_chunks(file_path, CHUNK_SIZE)
        response = self.stub.upload(chunks_generator, metadata=metadata)
        if response.success:
            print("Successfully saved the data with hash_id: ", hash_id)
        else:
            print("Failed saved the data with hash_id", hash_id)


if __name__ == '__main__':
    sendNode = SenderNode('localhost:5555')

    # simulate send request
    app_n = "dropbox_app"
    file_p = './IMG_0610.jpg'
    file_n = os.path.basename(file_p)
    file_size_bytes = os.path.getsize(file_p)

    sendNode.upload(app_n, file_n, file_p, file_size_bytes)
