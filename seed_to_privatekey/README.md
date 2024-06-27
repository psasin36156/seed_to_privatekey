
# Seed Phrase to private key derivation

This repository contains a Python script that derives Ethereum private and public keys from a given BIP39 seed phrase using the BIP44 standard.


## Features

- Derives Ethereum private and public keys from a BIP39 seed phrase.
- Supports BIP44 standard for key derivation.
- Allows generating a specified number of addresses.
- Outputs the keys to text files for easy access.


## Installation

Clone the repository

```bash
  git clone https://github.com/s/seed_to_privatekey.git
  cd seed_to_privatekey
```
Install the required library

```
pip install bip-utils
```

## how-to-use

    1. Edit the seed_phrase variable in the line38
    2. Run the script 
    ```
    python derive_keys.py
    ```
    4. enter number of privatekey you need to derive
    3. The script will generate the specified number of key and address





