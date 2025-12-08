from parse import Parser

def main():
    parser = Parser()
    parser.parse_file_to_db('src/day_05/data/input.txt')
    fresh_count = 0
    spoiled_count = 0
    total_items = len(parser.items)
    print(f"Total items to check: {total_items}")
    for item in parser.items:
        # Log status every 50 items
        if (fresh_count + spoiled_count) % 50 == 0:
            print(f"Checked {fresh_count + spoiled_count} items so far...")
        if parser.is_item_valid(item):
            print(f"Item ID {item} is valid.")
            fresh_count += 1
        else:
            print(f"Item ID {item} is invalid.")
            spoiled_count += 1
    
    print(f"Total valid items: {fresh_count}")
    print(f"Total invalid items: {spoiled_count}")

    print("Cleaning ID ranges for part 2...")
    parser.clean_ranges()
    total_valid_ids = parser.count_valid_items()
    print(f"Total valid item IDs after cleaning ranges: {total_valid_ids}")

if __name__ == "__main__":
    main()
