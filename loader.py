import json

class CategoryPathMatcher:
    def __init__(self, file1_path, file2_path):
        self.file1_path = file1_path
        self.file2_path = file2_path
        self.file1_data = self.load_json(self.file1_path)
        self.file2_data = self.load_json(self.file2_path)

    def load_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_json(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def compare_and_merge(self):
        output_data = []

        for f1 in self.file1_data:
            for f2 in self.file2_data:
                if str(f1["ID"]) == str(f2["supplier_old_cat_id"]):
                    merged_data = {
                        "supplier_old_cat_id": f2["supplier_old_cat_id"],
                        "supplier_cat_path": f2["supplier_cat_path"],
                        "mioga_old_cat_id": f2["mioga_old_cat_id"],
                        "Category1": f1["Category1"],
                        "Category2": f1["Category2"]
                    }
                    output_data.append(merged_data)
        
        return output_data if output_data else "No match found"