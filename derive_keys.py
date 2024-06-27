from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

def seed_phrase_to_ethereum_keys(seed_phrase: str, account: int = 0, change: Bip44Changes = Bip44Changes.CHAIN_EXT, num_addresses: int = 20):
    # Generate seed from the seed phrase
    seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
    
    # Create BIP44 master key specifically for Ethereum
    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    
    keys = []
    
    for address_index in range(num_addresses):
        # Derive BIP44 account, change and address index keys
        bip44_acc = bip44_mst.Purpose().Coin().Account(account).Change(change).AddressIndex(address_index)
        
        # Get the private key in hex format
        private_key = bip44_acc.PrivateKey().Raw().ToHex()
        
        # Get the Ethereum address
        address = bip44_acc.PublicKey().ToAddress()
        
        # Append the keys to the list
        keys.append({
            'private_key': private_key,
            'address': address
        })
    
    return keys

# Function to write keys to files
def write_keys_to_files(keys, private_key_file, address_file):
    with open(private_key_file, 'w') as pk_file, open(address_file, 'w') as addr_file:
        for key in keys:
            pk_file.write(key['private_key'] + '\n')
            addr_file.write(key['address'] + '\n')

# Example usage
seed_phrase = "paste_your_seedphrase_here"
num_addresses = int(input("Enter the number of addresses to generate: "))
keys = seed_phrase_to_ethereum_keys(seed_phrase, num_addresses=num_addresses)

# Write the keys to files
write_keys_to_files(keys, 'private_keys_file.txt', 'addresses_file.txt')

# Print confirmation
print("Private keys and addresses created successfully")
