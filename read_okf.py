import yaml
import glob

def load_all_departments():
    departments = []
    files = glob.glob("okf/departments/*.md")

    for filepath in files:
        with open(filepath, "r") as f:
            content = f.read()
        parts = content.split("---")
        yaml_data = yaml.safe_load(parts[1])
        description = parts[2].strip()
        yaml_data["description"] = description
        departments.append(yaml_data)

    return departments


def search_okf(query):
    all_depts = load_all_departments()
    query_lower = query.lower()
    results = []

    for dept in all_depts:
        # Check if the department name appears anywhere in the question
        if dept["department"].lower() in query_lower:
            results.append(dept)

    return results


# Test it
if __name__ == "__main__":
    question = "Where is the Cardiology department?"
    matches = search_okf(question)

    if matches:
        for m in matches:
            print(f"Department: {m['department']}")
            print(f"Location: {m['location']}")
            print(f"Head: {m['head']}")
            print(f"Timings: {m['timings']}")
    else:
        print("No matching department found.")
    
        