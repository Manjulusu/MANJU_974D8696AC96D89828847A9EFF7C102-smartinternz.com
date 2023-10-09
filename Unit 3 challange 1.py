def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices


products = ["apple", "banana", "apple", "grape", "apple"]
print(products)
for i in range(0,10):
  num=int(input("if you appand a word enter 1,not enter 2\n"))
  if num==1:
    a=input("enter the word\n")
    products.append(a)
  else:
    print("no word you apppend\n")
    break
target = input("enter the target word\n")
result = linear_search_product(products, target)
if result==[]:
  print("unknown word ")
else:
  print(result)