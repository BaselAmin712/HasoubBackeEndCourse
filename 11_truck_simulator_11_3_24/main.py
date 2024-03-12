from truck_simulator import TruckSimulator
import sys

def main():
    truck_simulator = TruckSimulator()
    num1,num2,operator = sys.argv[1:]
    print(truck_simulator.update_driving_changes(truck,road))
    
if __name__ == "__main__":
    main()