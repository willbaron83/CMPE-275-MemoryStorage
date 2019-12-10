import os
from concurrent import futures

import grpc
import time
import hashlib
import sys

import chunk_pb2, chunk_pb2_grpc

CHUNK_SIZE = 1024  # 1KB // the server (receiver node) must also be configured to take the same chunk size


def get_file_chunks(filename, chunk_size):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                return
            yield chunk_pb2.Chunk(buffer=chunk)


def save_chunks_to_file(filename, chunks):
    with open(filename, 'wb') as f:
        for chunk in chunks:
            f.write(chunk.buffer)


def generate_hash_id(app_name, file_name):
    name_path = app_name + file_name
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

    def download(self, app_name, file_name, output_path):
        hash_id = generate_hash_id(app_name, file_name)
        response = self.stub.download(chunk_pb2.Request(hash_id=hash_id))
        save_chunks_to_file(output_path, response)
        print("Successfully downloaded file with hash_id: ", hash_id)

    def get_node_available_memory_bytes(self):
        return self.stub.get_available_memory_bytes(chunk_pb2.Empty_request()).bytes

    def get_node_stored_hashes_list_iterator(self):
        return self.stub.get_stored_hashes_list_iterator(chunk_pb2.Empty_request())


if __name__ == '__main__':
    sendNode = SenderNode('localhost:5555')

    if len(sys.argv) == 1:
        print("Please pass in at least one argument")
        sys.exit()

    file_p = sys.argv[1]

    app_n = "dropbox_app"
    download_file = "false"

    if len(sys.argv) > 2:
        app_n = sys.argv[2]

    if len(sys.argv) > 3:
        download_file = sys.argv[3]

    # send (upload) file request
    file_n = os.path.basename(file_p)
    file_size_bytes = os.path.getsize(file_p)

    sendNode.upload(app_n, file_n, file_p, file_size_bytes)

    print("\nSize available in bytes ", sendNode.get_node_available_memory_bytes())
    print("Hashes saved so far: ")
    for hash_ in sendNode.get_node_stored_hashes_list_iterator():
        print(hash_.hash_id)

    # download file request
    # to download data pass in the app name and file name to obtain the hash
    if "true" == "true":
        output_path = "data/test_out.txt"
        sendNode.download(app_n, file_n, output_path)
