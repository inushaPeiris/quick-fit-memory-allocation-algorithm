import argparse
import json
from quick_fit import QuickFit

def load_config(file_path="data/config.json"):
    """Loads configuration data from a JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Configuration file not found at: {file_path}. Using default block sizes.")
        return {"block_sizes": [64, 128, 256]}

def main():
    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Quick Fit Memory Allocator")
    parser.add_argument("--config", type=str, default="data/config.json", help="Path to configuration file.")
    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)
    block_sizes = config.get("block_sizes", [64, 128, 256])
    initial_blocks = config.get("initial_blocks", 10)

    # Initialize QuickFit allocator
    allocator = QuickFit(block_sizes, initial_blocks)

    while True:
        print()
        print("\nQuick Fit Memory Allocator")
        print("1. Allocate Memory")
        print("2. Deallocate Memory")
        print("3. View Memory Pools")
        print("4. View Dynamic Allocations")
        print("5. Exit")
        choice = input("\nSelect an option: ")

        if choice == "1":
            try:
                size = int(input("Enter size to allocate: "))
                allocator.allocate(size)
            except ValueError:
                print("Invalid input. Please enter a valid integer size.")
        elif choice == "2":
            try:
                block_id = int(input("Enter block ID to deallocate: "))
                allocator.deallocate(block_id)
            except ValueError:
                print("Invalid input. Please enter a valid block ID.")
        elif choice == "3":
            allocator.view_pools()
        elif choice == "4":
            allocator.view_dynamic_allocations()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
