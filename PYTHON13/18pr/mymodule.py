#FOR 1!
import bisect

def hello():
 print('Hello, world!')
def fib(n):
 a = b = 1
 for i in range(n - 2):
    a, b = b, a + b
 return b

#FOR 2!
def filter_list(list_a, k):

  list_b = []
  for element in list_a:
    if element != k:
      list_b.append(element)

  return list_b

#FOR 3!
def insert_in_ordered_list(list_a, value_k):

  index = bisect.bisect_left(list_a, value_k)

  list_a.insert(index, value_k)

  return list_a

#FOR 4!
def fill_list(list_a, num_elements, value):
  
    if not list_a:
        raise ValueError("Список не может быть пустым.")

    if num_elements > len(list_a):
        raise ValueError("Количество элементов для заполнения не может превышать длину списка.")

    for i in range(num_elements):
        list_a[i] = value

    return list_a