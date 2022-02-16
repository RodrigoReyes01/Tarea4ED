from crypt import methods
from flask import Flask 
from jinja2 import Template, FileSystemLoader, Environment

templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

def to_list(self):
    l = []
    if self.head is None:
        return l
    node = self.head
    while node:
        l.append(node.data)
        node = node.next_node
    return l

def insert_beginning(self, data):
    new_node = Node(data, self.head)
    self.head = new_node

def insert_at_end(self, data):
    if self.head is None:
        return self.insert_beginning(data)

    node = self.head
    while node.next_node:
        node = node.next_node
        node.next_node = Node(data, None)

def print_ll(self):
    ll_string = ''
    node = self.head
    if node is None:
        print(None)
        while node:
            ll_string += f'{str(node.data)} ->'
            node = node.next_node
            ll_string += ' None'
            print(ll_string)



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('aaa.html')

@app.route('add to list', method=["GET","POST"])
def add():
    pass

@app.route('play now', methods=["GET"])
def play():
    pass

@app.route('get list', methods=["GET"])
def list():
    pass

@app.route('play previous', methods=["GET"])
def prev():
    pass

@app.route('play next', method=["GET"])
def next():
    pass

@app.route('delete song', methods=["DELETE"])
def delete():
    pass



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)
