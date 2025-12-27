class Harajatlar:
    def __init__(self):
        self.harajatlar = []      

    def qosh(self, summa, sabab="Boshqa"):
        if summa > 0:
            self.harajatlar.append([summa, sabab])
            print(f"+ {summa} so'm harajat qilindi ({sabab})")
        else:
            print("Harajat musbat bo'lishi kerak")

    def jami(self):
        return sum(h[0] for h in self.harajatlar)

    def ko_rsat(self):
        if not self.harajatlar:
            print("Hali hech qanday harajat yo'q")
            return
        
        print("\nHarajatlar ro'yxati:")
        for i, (summa, sabab) in enumerate(self.harajatlar, 1):
            print(f"{i}. {summa} so'm - {sabab}")
        print(f"\nJami harajat: {self.jami()} so'm")


xarajatlarim = Harajatlar()

xarajatlarim.qosh(45000, "Ovqat")
xarajatlarim.qosh(120000, "Transport")
xarajatlarim.qosh(30000, "Internet")
xarajatlarim.qosh(85000, "Kiyim")

xarajatlarim.ko_rsat()
