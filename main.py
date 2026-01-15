
class Mashina:
    def __init__(self,rang,model,tezlik):
        self.rang = rang
        self.model = model
        self.tezlik = tezlik
car1 = Mashina('Qora','BMW M5','300')
car2 = Mashina('Qora','BMW i8','250')
car3 = Mashina('Qora','BMW M4', '250')

print('-'*30)
print(f'-'*4,"MASHINALAR RO'YXATI",'-'*5)
print('-'*30)
print(f"Mashina rangi: {car1.rang}"
      f"\nMashina modeli: {car1.model}"
      f"\nMashina tezligi: {car1.tezlik}")
print('-'*30)
print(f"Mashina rangi: {car2.rang}"
      f"\nMashina modeli: {car2.model}"
      f"\nMashina tezligi: {car2.tezlik}")
print('-'*30)
print(f"Mashina rangi: {car3.rang}"
      f"\nMashina modeli: {car3.model}"
      f"\nMashina tezligi: {car3.tezlik}")
print('-'*30)