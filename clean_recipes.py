# Standard library imports
import json
import os


def load_recipes():
    json_path = os.path.join("data", "bbcgoodfood_json.json")
    with open(json_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines


def get_dish_titles(lines):
    # Lists of each recipe title
    all_titles = []
    breakfast_titles = []
    dinner_titles = []
    lunch_titles = []
    snack_titles = []
    dessert_titles = []

    # Iterate through and get recipe
    for line in lines:
        json_recipe = json.loads(line)
        ingredients = json_recipe["page"]["recipe"]["ingredients"]
        # Encode and decode to remove bad characters 
        dish = json_recipe["page"]["title"].encode("ascii", "ignore").decode() + "\n"
        recipe_courses = json_recipe["page"]["recipe"]["courses"]
        all_titles.append(dish)
        if ("Dinner" in recipe_courses or "Main course" in recipe_courses
            or "Supper" in recipe_courses or "Pasta course" in recipe_courses):
            dinner_titles.append(dish)
        if ("Lunch" in recipe_courses or "Side dish" in recipe_courses
            or "Starter"  in recipe_courses or "Soup course" in recipe_courses):
            lunch_titles.append(dish)
        if ("Snack" in recipe_courses or "Buffet" in recipe_courses
            or "Afternoon tea"  in recipe_courses or "Canapes" in recipe_courses):
            snack_titles.append(dish)
        if "Dessert" in recipe_courses or "Treat" in recipe_courses:
            dessert_titles.append(dish)
        if "Brunch" in recipe_courses or "Breakfast" in recipe_courses:
            breakfast_titles.append(dish)
    
    # Write each list to a file
    write_list(all_titles, "allrecipes")
    write_list(breakfast_titles, "breakfast")
    write_list(dinner_titles, "dinner")
    write_list(lunch_titles, "lunch")
    write_list(snack_titles, "snack")
    write_list(dessert_titles, "dessert")


def calc_courses(lines):
    courses_dict = {}
    for line in lines:
        json_recipe = json.loads(line)
        recipe_courses = json_recipe["page"]["recipe"]["courses"]
        for course in recipe_courses:
            if course in courses_dict.keys():
                courses_dict[course] += 1
            else:
                courses_dict[course] = 1
    # Sorts courses by how popular they are
    courses = sorted(courses_dict, key=lambda x: courses_dict[x], reverse=True)
    courses_dict = {course : courses_dict[course] for course in courses}
    return courses_dict


def write_list(recipe_list: list, filename: str):
    recipes_path = os.path.join("data", filename+".txt")
    with open(recipes_path, "w+", encoding="utf-8") as f:
        f.writelines(recipe_list)


if __name__ == "__main__":
    lines = load_recipes()
    print(calc_courses(lines))
    get_dish_titles(lines)