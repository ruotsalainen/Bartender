from multiprocessing.dummy import Pool
from time import sleep, time
from pumps import pumps
from drinks import drink_list



def test(ingredient):
    timeout = ingredient["amount"] / 3.34
    for pump in pumps:
        if pump["value"] == ingredient["ingredient"]:
            timeout_start = time()

            while time() < timeout_start + timeout:
                print(".")
                sleep(1)
            print(ingredient["ingredient"] + " ready")
            print(time() - timeout_start)
pool = Pool(6)

pool.map(test, drink_list[2]["ingredients"])
pool.close()
pool.join()