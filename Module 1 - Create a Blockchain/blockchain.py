import datetime, hashlib, json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous='0')

    def create_block(self, proof, previous):
        
