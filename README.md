## How to run it

### run receiver node:
#### Start the server Node in one terminal window 
```
cd scripts

./server_test.sh 
```
Sample Output at start:
```
Starting Storage Manager.
[MemoryManager] Number of pages available in memory 1048576 of size 1024 bytes.
Storage Manager is READY.
```

### run sender node:
#### Run the client Node in another terminal window 

```
cd scripts

./client_test.sh 
```
Sample output from client:
```
./client_test.sh 
Running job: 0
Hash_id exists:  False
Successfully saved the data with hash_id:  dd9bc75bfdb83da4b5a2abdeddd9afe1d561eaf8

Size available in bytes  1073737728.0
Hashes saved so far: 
Successfully downloaded file with hash_id:  dd9bc75bfdb83da4b5a2abdeddd9afe1d561eaf8
Successfully saved the data with hash_id:  297beb01dd21c5a2aad009da6abb91d4bc0fdc6d
Successfully downloaded file with hash_id:  297beb01dd21c5a2aad009da6abb91d4bc0fdc6d
```
Sample output from server:
```
[MemoryManager] Writing new data with hash_id: dd9bc75bfdb83da4b5a2abdeddd9afe1d561eaf8.
[MemoryManager] Looking for 4 available pages... 
[SpaceBinaryTree] Number of chunks needed = 4
[MemoryManager] Enough pages available to save the data. Took 0.021489 seconds.
[MemoryManager] Successfully saved the data in 4 pages. Bytes written: 4096. Took 0.000587 seconds.
[MemoryManager] Free pages left: 1048572. Bytes left: 1073737728

```
What did it do?
Given input file "test_in.txt" and app name "dropbox_app"
1. The client sent (uploaded) a file that contains numbers (test_in.txt) and it was saved in memory in the server.
2. The client retrieved (downloaded) the same file that was stored in the server memory. We only need to pass the same hash_id.


### Current features:
1. Upload a file in chunks (as stream) given a hash_id. Chunks size is set to 1024 bytes.  
```
rpc upload_chunk_stream(stream Chunk) returns (Reply) {}
```
2. Upload a single chunk given a hash_id. Chunks size is set to 1024 bytes.  
```
rpc upload_single_chunk(Chunk) returns (Reply) {}
```
3. Download data in (as chunk stream) given a hash_id. 
```
rpc download_chunk_stream(Request) returns (stream Chunk) {}
```
4. List the memory available in the server in bytes. This will be useful to decide if a file can fit into that server. 
```
rpc get_available_memory_bytes(Empty_request) returns (Reply_double) {}
```
5. Function to list all files stored in a server given an application name
```
rpc get_stored_hashes_list_iterator(Empty_request) returns (stream Reply_string) {}
``` 
6. Check if a hash_id exists in memory
```
rpc hash_id_exists_in_memory(Request) returns (Reply) {}
```

  
### Work in Progress features:
1. Function to rename a file stored in a server 

Note that this example uses files but it can be anything as long as it can be converted to chunks of bytes. 
See function `get_file_chunks(...)` in the client script

## Group Members
- Miguel Covarrubias
- William Baron

