# Vehicle Record Management System 

def main():
    vehicles = []

    while True:
        print("Vehicle Record System ")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Search Vehicle")
        print("4. Vehicle Statistics")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        # Module 1: Add Vehicle
        if choice == '1':
            v_num = input("Enter Vehicle Number: ") 
            owner = input("Enter Owner Name: ")
            v_type = input("Enter Vehicle Type (Car/Bike/Truck): ") 
            
            record = {"number": v_num,
                "owner": owner,
                "type": v_type }
            
            vehicles.append(record)
            print("Vehicle added successfully!")

        # Module 2: View Vehicles
        elif choice == '2':
            if not vehicles:
                print("No records found.")
            else:
                print("All Vehicle Records:") 
                for v in vehicles:
                    print(f"Number: {v['number']}, Owner: {v['owner']}, Type: {v['type']}")

        # Module 3: Search Vehicle
        elif choice == '3':
            search_num = input("Enter Vehicle Number to search: ") 
            found = False
            for v in vehicles:
                if v['number'].lower() == search_num.lower():
                    print(f"Found! Owner: {v['owner']}, Type: {v['type']}")
                    found = True
                    break
            if not found:
                print("Vehicle not found.")

        # Module 4: Vehicle Statistics 
        elif choice == '4':
            if not vehicles:
                print("No data available for statistics.")
                continue
            
            total = len(vehicles)
            
            # Count vehicles by type 
            type_counts = {}
            for v in vehicles:
                if v['number']==v_num:
                    print('vehicle already exists')
                    break
                v_type = v['type']
                type_counts[v_type] = type_counts.get(v_type, 0) + 1
            
            print(f"Total Vehicles: {total}")
            print("Vehicles by Type:", type_counts)
            print(f"First Added: {vehicles[0]['number']}") 
            print(f"Last Added: {vehicles[-1]['number']}") 

        # Module 5: Exit 
        elif choice == '5':
            print("Exiting safely. Goodbye!") 
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

