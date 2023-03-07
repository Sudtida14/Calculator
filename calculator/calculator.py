import json
from aiohttp import request
from web3 import Web3
from flask import Flask, jsonify, render_template

class Blockchain:
    	def __init__(self, url):
            self.web3 = Web3(Web3.HTTPProvider(url))
            abi = json.loads(""" [
                {
                    "inputs": [
                        {
                            "internalType": "uint256",
                            "name": "a",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "b",
                            "type": "uint256"
                        }
                    ],
                    "name": "add",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "uint256",
                            "name": "a",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "b",
                            "type": "uint256"
                        }
                    ],
                    "name": "divide",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "uint256",
                            "name": "a",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "b",
                            "type": "uint256"
                        }
                    ],
                    "name": "multiply",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "uint256",
                            "name": "a",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "b",
                            "type": "uint256"
                        }
                    ],
                    "name": "subtract",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "result",
                    "outputs": [
                        {
                            "internalType": "uint256",
                            "name": "",
                            "type": "uint256"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                }
            ]""") 
            abi_address = ("0x3f50Ad47845218F10b1CA7B7d0d8B3945187F531")
            self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
            self.contract = self.web3.eth.contract(address=abi_address, abi = abi)   

            def calculator(self, num1, num2, operation):
                if operation == '+':
                    return self.contract.functions.add(num1, num2).call()
                elif operation == '-':
                    return self.contract.functions.subtract(num1, num1).call()
                elif operation == '*':
                    return self.contract.functions.multiply(num1, num2).call()
                elif operation == '/':
                    return self.contract.functions.divide(num1, num2).call()  		

            def get_result():
                result = self.contract.functions.result().call()
                return result

app = Flask(__name__)
blockchain = Blockchain("http://127.0.0.1:8545")

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = int(request.json)['num1']
    num2 = int(request.json)['num2']
    operation = request.json['operation']
    result = blockchain.calculate(num1, num2, operation)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)