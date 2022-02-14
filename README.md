# **ROCK, PAPER, SCISORS.eth**

### Requirements 

Web3
     - ``` pip install web3```.

Pipx
    - ``` python3 -m pip install --user pipx```
    - ``` python3 -m pipx ensurepath```.

Brownie
    - ``` pipx install eth-brownie```.

Ganache
    - [Truffle Ganache](https://trufflesuite.com/ganache/)

Ganache-cli
    - ``` npm install -g ganache-cli```

## Quickstart

1. Install all the dependencies listed above. 

2. Add "ganache-local" into Brownie's network list: 

```
$ brownie networks list
$ brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=1337
```

3. Deploy the smart contract calling the *deploy.py* script, located in the scrips repository, to the ganache-local network.
```
$ brownie run scripts/deploy.py --network ganache-local
```

4. Run the game with the *play_game.py* sccript, also located in the cripts repository, to the ganache-local network.
```
$ brownie run scripts/play_game.py --network ganache-lacal



# .env File
- PRIVATE_KEY=
- WEB3_INFURA_PROJECT_ID

## TODO

- Create new contrat
    - Price feed. ETH-USD

- Mediator and Player 
    - The contract's deployer (owner) will be the mediator. 

- Players can also bet NFTs 
    - Not sure how to yet 