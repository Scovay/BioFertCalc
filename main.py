class fertilizerUtility:
    def __init__(self, size=0, percent=0) -> None:
        self.lawnArea = size
        self.nitrogenPercentage = percent
        self.nitrogenTable = {
            1:100, 2:50, 3:33.3, 4:25, 5:20, 6:16.7, 7:14.3, 8:12.5, 9:11.1,
            10:10, 11:9.1, 12:8.3, 13:7.7, 14:7.1, 15:6.7, 16:6.3, 17:5.9, 18:5.6, 19:5.3,
            20:5, 21:4.8, 22:4.5, 23:4.3, 24:4.2, 25:4, 26:3.8, 27:3.7, 28:3.6, 29:3.4,
            30:3.3, 31:3.2, 32:3.1, 33:3.0, 34:2.9, 35:2.9, 36:2.8, 37:2.7, 38:2.6, 39:2.6,
            40:2.5, 41:2.4, 42:2.4, 43:2.3, 44:2.3, 45:2.2, 46:2.2
        }

    def fertilizerCalc(self):
        self.nitrogenPercentage = int(input("What is the nitrogen percentage of your fertilizer: "))

        while True:
            helpltr = str(input("Do you need help calculating your area (y/n): ")).lower()
            if helpltr == "y":
                print("If your lawn is an awkward shape try subdiving it into smaller portions before adding it together")
                print("Variables: ")
                print("""
    A - Area
    W - Width
    L - Length
    B - Base
    r - Radius
                """)
                print("Area Calc for Common Shapes:")
                print("""
    Rectangle: A = L x W
    Triangle: A = (B x W)/2
    Circle: A = 3.14 x r^2
                """)
                break
            elif helpltr == "n":
                break
            else:
                print("Invalid input try again")
        self.lawnArea = float(input("Enter your lawn area in sq ft: "))

        poundPer1000 = self.nitrogenTable[self.nitrogenPercentage]
        poundPerft = poundPer1000/1000

        print("Fertilizer Values (In pounds):")
        print("Fertilizer per sq ft-", poundPerft)
        print("Fertilizer per 1000 sq ft-", poundPer1000)
        print("Total fertilizer amount-", poundPer1000*(self.lawnArea/1000))

if __name__ == "__main__":
    funcCall = None
    lawn = fertilizerUtility()
    print("Fertilzers for a cause!\n")
    while True:
        try:
            print("When was the last time you fertilized your lawn?")
            time = int(input("Please enter the value in DAYS: "))
        except ValueError:
            print("Invalid input, make sure your value is an INTEGER.")
        else:
            if time >= 49:
                break
            else:
                print("Fertilize again in", 49-time, "day(s).")
                quit()
    
    lawn.fertilizerCalc()