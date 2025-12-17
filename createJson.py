import os
import json

# Root folder containing all recipes
ROOT_DIR = "recipes"  # Change this to your folder path

def scan_recipes(root_dir):
    recipes = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip the root folder itself
        if dirpath == root_dir:
            continue

        recipe_name = os.path.basename(dirpath)
        recipe = {
            "name": recipe_name,
            "folder": os.path.relpath(dirpath, root_dir).replace("\\", "/"),  # relative path
            "ingredients": None,
            "steps": None,
            "images": []
        }

        for file_name in filenames:
            lower_name = file_name.lower()
            if lower_name == "ingredients.md":
                recipe["ingredients"] = file_name
            elif lower_name == "steps.md":
                recipe["steps"] = file_name
            elif lower_name.endswith((".jpg", ".jpeg", ".png", ".gif")):
                recipe["images"].append(file_name)

        # Only add if it has at least Ingredients or Steps
        if recipe["ingredients"] or recipe["steps"]:
            recipes.append(recipe)

    return recipes

if __name__ == "__main__":
    recipes = scan_recipes(ROOT_DIR)
    output_file = "recipes.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(recipes, f, indent=2, ensure_ascii=False)

    print(f"Generated {output_file} with {len(recipes)} recipes.")
