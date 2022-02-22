from platform import node
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    

class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
    
    def pop_front(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            return self.head.data
    
    def peek(self):
        if(self.head != None):
            return self.head.data
        

lista = LinkedList()

@app.route('/')
def home():
    return render_template('')

@app.route('/add/<song>', methods=["GET","POST"])
def add(song):
    lista.add_first(Node(song))
    print(lista)
    return str(lista)


@app.route('/play', methods=["GET"])
def play():
    return str(lista.peek())

@app.route('/getlist', methods=["GET"])
def list():
    return str(lista)

@app.route('/prev', methods=["GET"])
def prev():
    pass

@app.route('/next', methods=["GET", "DELETE"])
def next():
    return str(lista.pop_front())

@app.route('/delete/<song>', methods=["DELETE"])
def delete(song):
    lista.remove_node(Node(song))
    return str(lista)



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)
