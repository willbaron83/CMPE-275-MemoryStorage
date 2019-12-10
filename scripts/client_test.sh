base_dir=$(dirname "$0")/..

cd "${base_dir}"
python3 ./src/SenderNode.py "./data/test_in.txt"
python3 ./src/SenderNode.py "./data/test_in_2.txt"
#python3 ./src/SenderNode.py "./data/big_file.data"