class party:
    def __init__(self,name,money):
        self.name=name
        self.money=money

    def __gt__(self,others):
        if self.money>others.money:
            return True
        else:
            return False
p1=party(name="Shree", money=2000)
p2=party(name="Uday",money=5000)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")
