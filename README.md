# **ROCK, PAPER, SCISORS.eth**

### Install 

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



Add "ganache-local" into Brownie's network list: 

 ```
$ brownie networks list
$ brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=1337
```

## TODO

- Create new contrat
    - Price feed. ETH-USD

- Mediator and Player 
    - The contract's deployer (owner) will be the mediator. 

- Players can also bet NFTs 
    - Not sure how to yet 