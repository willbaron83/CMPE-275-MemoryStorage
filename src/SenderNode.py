import os
from concurrent import futures

import grpc
import time

import chunk_pb2, chunk_pb2_grpc

CHUNK_SIZE = 1024   # 1MB

def get_file_chunks(filename, chunk_size):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                return
            yield chunk_pb2.Chunk(buffer=chunk)


class SenderNode:
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.stub = chunk_pb2_grpc.FileServerStub(channel)

    def upload(self, file_path, chunk_size):
        chunks_generator = get_file_chunks(file_path, chunk_size)
        response = self.stub.upload(chunks_generator)
        print("Was sending file successful: ", response.success)
        assert response.success


if __name__ == '__main__':
    sendNode = SenderNode('localhost:5555')

    # pick the file to se send to the receiving node
    file_path = 'IMG_0610.jpg'
    sendNode.upload(file_path, CHUNK_SIZE)