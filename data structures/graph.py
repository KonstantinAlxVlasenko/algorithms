from graphviz import Digraph

dot = Digraph(comment='The Round Table')

dot.node('hello')
dot.node('world')
dot.edge('hello', 'world')
dot.edge('world', 'third')
dot.edge('hello', 'second')

print(dot)