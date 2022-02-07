// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;


contract NewGame{

    uint256 public gameID;
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;

    constructor() public {
        owner = msg.sender;
    }


    function fund() public payable {
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public payable onlyOwner{
        msg.sender.transfer(address(this).balance);
    }

    function contracts_balance() public view onlyOwner returns(uint256) {
        return address(this).balance;
    }
}