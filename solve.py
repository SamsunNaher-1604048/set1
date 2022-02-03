class bussiness:
    def __init__(self):
        self.product_list = []  #list
        self.balance = 0

    def addproduct(self):
        while True:
            print('Press 1 if you  went to add product.')
            print('Or press any key for exit from add product')
            a=int(input('press number: '))
            if a == 1:
                pro = {}
                pro['name'] = input('Product name: ')
                pro['buy'] = int(input('Buy price: '))
                pro['sell'] = int(input('Sell prince: '))
                pro['avail'] = int(input('Available number of product: '))
                pro['profit'] = int(input('Total profit selling the product '))
                self.product_list.append(pro)
                print("Successfully add of product")
                print('--------*--------------*---------')
            else:
                self.manu()
                break
    def delete(self):
        while True:
            print('Press 1 if you  went to delete product.')
            print('Or press any key for exit from delete product')
            a = int(input('Press number: '))
            if a == 1:
                b = input('Enter item name: ')
                for i in range(len(self.product_list)):
                    if self.product_list[i]['name'] == b:
                        del self.product_list[i]
                        print('Successfully delete of product')
                        print('------*----------------*-----------')
                    else:
                        print('Not in product list')
                        print('-------*-----------------*-----------')
            else:
                self.manu()
                break
    def buyproduct(self):
        while True:
            print('Press 1 if you  went to buy product.')
            print('Or press any key for exit from buy product')
            a = int(input('Press number: '))
            if a == 1:
                b = input('Enter item mane: ')
                c = int(input('Enter total number of product: '))
                d = int(input('Price of the product'))
                d=c*d
                if self.balance > d:
                    for i in range(len(self.product_list)):
                        if self.product_list[i]['name'] == b:
                            self.product_list[i]['avail'] = self.product_list[i]['avail']+c
                            self.balance = self.balance-d
                            print('successfully buy')
                            print('----------*-----------------*-------')
                else:
                    print('balance is not sufficient')
                    print('----------*-----------------*-------')
            else:
                self.manu()
                break

    def sellproduct(self):
        while True:
            print('Press 1 if you  went to sell product.')
            print('Or press any key for exit from sell product')
            a = int(input('Press number: '))
            d=0
            if a == 1:
                b = input('Enter the name of product: ')
                c = int(input('Number of product: '))
                for i in range(len(self.product_list)):
                    if self.product_list[i]['name'] == b  and  self.product_list[i]['avail'] >= c:
                        self.product_list[i]['avail'] = self.product_list[i]['avail']-c
                        self.balance = self.balance+(self.product_list[i]['sell']*c)
                        v = 1
                        break
                if v == 1:
                    print('Successfully sell')
                    print('------*---------------*--------------')
                else:
                    print('not sufficient amount')
                    print('------*---------------*--------------')
            else:
                self.manu()
                break

    def listproduct(self):
            print("Name"+" "+"Buy"+" "+"Sell"+" "+"Available"+" "+"Profit")
            for i in range(len(self.product_list)):
                print(self.product_list[i]['name'] +"   "+str(self.product_list[i]['buy'])+"   "+str(self.product_list[i]['sell'])
                      +"        "+str(self.product_list[i]['avail'])+"       "+str(self.product_list[i]['profit']))
                print('\n')
            print('-----*---------------*-----------')
            self.manu()

    def blance(self):
            print('balance is: ')
            print(self.balance)
            print('-------*-------------------*------------')
            self.manu()


    def manu(self):
        print('1.add a product')
        print('2.delete a product')
        print('3.buy a product')
        print('4.sell a product')
        print('5.see the list of product')
        print('6.see available balance')
        print('-----------------------------------------------')
        print('enter number what you need?')


product = bussiness()
product.manu()

while True:
    val = input()
    if val == '1':
        product.addproduct()
    elif val == '2':
        product.delete()
    elif val == '3':
        product.buyproduct()
    elif val == '4':
        product.sellproduct()
    elif val == '5':
        product.listproduct()
    elif val == '6':
        product.blance()
    else:
        product.manu()
