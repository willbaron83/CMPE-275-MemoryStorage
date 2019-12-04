## How to run it

### run receiver node:
#### Start the receiver Node in one terminal window 
```
python3 ./src/ReceiverNode.py
```
Sample Output at start:
```
python3 ./src/ReceiverNode.py
Number of pages in memory 1048576
Node is READY
```

### run sender node:
#### Run the sender Node in another terminal window 

```
python3 ./src/SenderNode.py
```
Sample output from client:
```
./src/SenderNode.py
Successfully saved the data with hash_id:  d38c538381efe472606b98f7764dc9526c365e06
Successfully downloaded file with hash_id:  d38c538381efe472606b98f7764dc9526c365e06
```
Sample output from server:
```
Writing new hash_id:  d38c538381efe472606b98f7764dc9526c365e06
Enough pages available to save the data
Successfully saved the data in 4 pages: 
Free pages left:  1048572
Returning: data for d38c538381efe472606b98f7764dc9526c365e06 composed of 4 pages.
```
What did it do?
Given input file "test_in.txt" and app name "dropbox_app"
1. The client sent (uploaded) a file that contains numbers (test_in.txt) and it was saved in memory in the server.
2. The client retrieved (downloaded) the same file that was stored in the server memory. We only need to pass the same all and filename.


### Current features:
1. Upload a file in chunks given a file name and an application name. Chunks size is set to 1024 bytes.
2. Download a file given a file name and an application name. 

### Work in Progress features:
1. Function to list all files stored in a server given an application name
2. List the memory available in the server in bytes. This will be useful to decide if a file can fit into that server. 
3. Function to rename a file stored in a server 

Note that this example uses files but it can be anything as long as it can be converted to chunks of bytes. 
See function `get_file_chunks(...)` in the client script