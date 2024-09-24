from flask import Flask, redirect, abort
import scrape

app = Flask(__name__)

# Dictionary to map problem numbers to their LeetCode problem URLs
problem_map = scrape.scraper()

# Route to handle rerouting based on the problem number
@app.route('/<int:problem_number>')
def reroute(problem_number):
    if problem_number in problem_map:
        # Generate the LeetCode problem URL
        problem_name = problem_map[problem_number]
        leetcode_url = f"https://leetcode.com/problems/{problem_name}/description/"
        return redirect(leetcode_url)
    else:
        # If the problem number is not found, return a 404 error
        return abort(404, description="Problem number not found.")

if __name__ == '__main__':
    app.run(debug=True)
