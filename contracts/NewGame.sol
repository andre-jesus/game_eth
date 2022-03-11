// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract NewGame {
    mapping (address => uint256) public balances;

    address public arbiter;
    address public player1;
    address public player2;

    // TO DO 
    // Assign players. Player 1 as balances[0] and player 2 to balances[1]
    
    mapping(address => uint256) public deposits; 

    modifier onlyArbiter() {
        require (msg.sender == arbiter, "Must be arbiter!");
            _;
    }

    constructor() public {
        arbiter = msg.sender;
    }

    function depositToGame() external payable {
        deposits[msg.sender] += msg.value;
    }

    function player1Deposit() external payable {
        player1 = msg.sender;
        deposits[msg.sender] += msg.value;
    }

    function player2Deposit() external payable {
        player2 = msg.sender;
        deposits[msg.sender] += msg.value;
    }

    function winner(address payable _winner) external payable onlyArbiter {
        if(_winner == player1){
            winners == payable player1;
            winners.transfer(address(this).balance);
        }
        else(_winner == player2) {
            winner == payable player2;
            winner.transfer(address(this).balance);
        }
    }


}


// contract NewGame {

//     uint256 public gameID;
//     mapping(address => uint256) public addressToAmountFunded;
//     address[] public funders;
//     address public owner;
//     uint256 public balance;
//     address public player;

//     constructor() public {
//         owner = msg.sender;
//         balance = address(this).balance;
//     }
//      // add Player1 and Player2 and Sender = owner

//     function fund() public payable {
//         addressToAmountFunded[msg.sender] += msg.value;
//         funders.push(msg.sender);
//     }

//     modifier onlyOwner() {
//         require(msg.sender == owner);
//         _;
//     }

//     // function withdraw(_player) public payable onlyOwner{
//     //     player.transfer(address(this).balance);
//     // }

//     function contracts_balance() public view returns(uint256) {
//         return address(this).wei_balance;
//     }
// }