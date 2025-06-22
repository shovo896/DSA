import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"Mining block {self.index}...")
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Increase to make mining harder

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        prev_block = self.get_latest_block()
        new_block = Block(len(self.chain), prev_block.hash, time.time(), new_data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                print("Current hash is not valid!")
                return False
            if curr.previous_hash != prev.hash:
                print("Previous hash doesn't match!")
                return False
        return True

# Run Example
my_blockchain = Blockchain()

my_blockchain.add_block("First transaction: Alice pays Bob 10 BTC")
my_blockchain.add_block("Second transaction: Bob pays Charlie 5 BTC")

print("\nBlockchain Valid?", my_blockchain.is_chain_valid())

# Print the chain
for block in my_blockchain.chain:
    print("\nBlock", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
