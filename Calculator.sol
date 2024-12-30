// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;
contract Calculator{

    function Add(uint256 a,uint256 b) pure public returns(uint256) {
        return a+b;
    }

    function Subtract(uint256 a,uint256 b) pure public returns(uint256) {
        return a-b;
    }

    function Multiply(uint256 a,uint256 b) pure public returns(uint256) {
        return a*b;
    }

    function Divide(uint256 a,uint256 b) pure public returns(uint256) {
        return a/b;
    }

    function Exponential(uint256 a,uint256 b) pure public returns(uint256) {
        return a^b;
    }

    function Percentage(uint256 total,uint256 percent) pure public returns(uint256) {
        return (total*percent)/100;
    }

    function Modulus(uint256 a,uint256 b) pure public returns(uint256) {
        require(b!=0,"That division is undefined");
        return a%b;
    }

    function Factorial(uint256 n) pure public returns(uint256) {
        require(n>=0,"Input must be a non negative integer");
        if(n==0) return 1;
        uint256 result=1;
        for(uint256 i=1;i<=n;i++) {
            result=result*i;
        }
        return result;
    }

    uint256 private recentResult;

    function storeResult(uint256 result) public {
        recentResult = result;
    } 

    function getLastResult() public view returns(uint256) {
        return recentResult;
    }

}