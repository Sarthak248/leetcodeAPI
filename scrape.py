import json

def scraper():
    result = {}

    f = open("data.json", "r")
    string = f.read()
    content = json.loads(string)

    listOfProblems = content.get("problemsetQuestionList")
    problem = 0

    for problem in listOfProblems:
        problemNum = int(problem.get("questionFrontendId"))
        titleSlug = problem.get("titleSlug")
        result[problemNum] = titleSlug
    return result
