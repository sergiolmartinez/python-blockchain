import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp':1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
            )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_json(self):
        """
        Serialize the block into a dictionary of its attributes
        """
        return self.__dict__

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data, until a block has is found that meets the leading zeros proof of work requirement.
        """
        #here for difficulty lets change time stamp to time_to_min_block from last_block
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        # Here lets calculate the time it takes to mine this block, compare to the previous block and adjust difficulty
        # Other improvements could take the average of all previous blocks and compare time to mine this block to the average
        while hex_to_binary(hash)[0:difficulty] !='0' * difficulty:
            nonce += 1 
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)


        return Block(timestamp, last_hash, hash, data, difficulty, nonce)
    
    @staticmethod
    def genesis():
        """
        Generate the genesis block
        """
        # return Block(
        #     timestamp = GENESIS_DATA['timestamp'],
        #     last_hash = GENESIS_DATA['last_hash'],
        #     hash = GENESIS_DATA['hash'],
        #     data = GENESIS_DATA['data']           
        #     )
        return Block(**GENESIS_DATA)

    @staticmethod
    def from_json(block_json):
        """
        Deserialized a block's json representation back into a block instance.
        """
        return Block(**block_json)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        Calculate the adjusted difficulty according to the MINE_RATE. Increase the difficulty for quickly mined blocks. Decrease the difficulty for slowly mined blocks
        """
        # Adjust this to algorithm to change the difficulty based on the time to mine a block. Will need to stored time_to_mine_block for the last_block and compare to the time_to_mine_block of this block.
        # Currently this adjust_difficulty is checking timestamps from previous block to new block that can introduce error if blocks are not mined frequently, therefore we should check for amount of time 
        # to mine a block instead. Add timestamps to the beginning of the mine_block method and end of mine_block to determine elapsed time. Save this as time_to_mine_block and add it to the block or 
        # blockchain. Then pull this time into the difficulty adjustment.
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        
        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1
        return 1
    @staticmethod
    def is_valid_block(last_block, block):
        """
        Validate block by enforcing the following rules:
        - the block must have the proper last_hash reference
        - the block must meet the proof of work requirement
        - the difficulty must only adjust by 1
        - the block hash must be a valid combination of the block fields
        """
        if block.last_hash != last_block.hash:
            raise Exception('The block last_hash must be correct')
        
        if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('The proof of work requirement was not met')

        if abs(last_block.difficulty - block.difficulty) > 1:
            raise Exception('The block difficulty must only adjust by 1')

        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty
        )

        if block.hash != reconstructed_hash:
            raise Exception('The block hash must be correct')

def main():
    genesis_block = Block.genesis()
    # good_block = Block.mine_block(Block.genesis(), 'foo')
    bad_block = Block.mine_block(Block.genesis(), 'foo')
    bad_block.last_hash = 'evil_data'
    try:
        # Block.is_valid_block(genesis_block, good_block)
        Block.is_valid_block(genesis_block, bad_block)

    except Exception as e:
        print(f'is_valid_block: {e}')



if __name__ == '__main__':
    main()