import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-256 of the given arguments.
    """
    #if order matters, then let's remove sorted from the line below.
    stringified_args = sorted(map(lambda data: json.dumps(data),args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}")

if __name__ == '__main__':
    main()

