import heapq

employee = [(7, 'bharath'), (8, 'pradeep'), (3, 'prabha'), (4, 'chitra'),
            (9, 'akesh'), (6, 'raj'), (1, 'ram'), (2, 'kumar')]
print(employee)
heapq.heapify(employee)
print(employee)
