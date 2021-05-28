class Stock:
    def __init__(self,name,price,supply,high52,low52):
        self.name = name
        self.price = price
        self.supply = supply
        cap = price*supply
        self.high52 = high52
        self.low52 = low52

    def operate():
        pricehist.append(self.price)
        if self.price >= self.high52:
            self.high52 = self.price
        if self.price <= self.low52:
            self.low52 = self.price

    def stockinfo() :
        print(f"the stock {name} is currently at {} with a market cap of %d with a high of %d and a low of %d"%(self.name,self.price,self.cap,self.high52,self.low52))

x= Stock("xd",52,1000000,100,32)

x.stockinfo()
