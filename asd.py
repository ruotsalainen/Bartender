from multiprocessing.dummy import Pool
from time import sleep

drinks = [{"name": "GT", "ingredients":[{"value": "gin", "amount":20},{"value":"tonic", "amount": 50}]}]

def test(ingredient):
    for _ in range(5):
        print(ingredient["value"])
        sleep(1)
    return ingredient["value"]

pool = Pool(4)

results = pool.map(test, drinks[0]["ingredients"])
pool.close()
pool.join()