// SPDX-License-Identifier: MIT

pragma solidity ^0.8.2;

contract NewGame {
    mapping (address => uint256) public balances;

    address public arbiter;
    address public player1;
    address public player2;

    // TO DO 
    // Assign players. Player 1 as balances[0] and player 2 to balances[1]
    
    mapping(address => uint256) public deposits; 

    modifier onlyArbiter() {
        require (msg.sender != arbiter, "Must be arbiter!");
             _;
    }

    constructor() {
        arbiter = msg.sender;
    }

    function depositToGame() external payable {
        deposits[msg.sender] += msg.value;
    }

    function player1Deposit() external payable{
        player1 = msg.sender;
        deposits[msg.sender] += msg.value;

    }

    function player2Deposit() external payable {
        player2 = msg.sender;
        deposits[msg.sender] += msg.value;
    }

    // function winner(address payable _winner) external payable onlyArbiter {
    //     if(_winner == player1){
    //         winners == payable player1;
    //         winners.transfer(address(this).balance);
    //     }
    //     else(_winner == player2) {
    //         winner == payable player2;
    //         winner.transfer(address(this).balance);
    //     }
    // }

    function totalGameBalance() public view returns (uint256) {
        return address(this).balance;
    }

}

