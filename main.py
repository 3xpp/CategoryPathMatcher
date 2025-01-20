import loader
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python compare_json.py <file1.json> <file2.json> <output.json>")
        sys.exit(1)
    
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    output_path = sys.argv[3]
    
    matcher = loader.CategoryPathMatcher(file1_path, file2_path)
    result = matcher.compare_and_merge()
    matcher.save_json(result, output_path)
    print(f"Result saved to {output_path}")
