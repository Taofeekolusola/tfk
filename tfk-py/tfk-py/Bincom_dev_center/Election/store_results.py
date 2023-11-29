def get_input():
    unit_name = input("Enter the polling unit name: ")

    # Get votes for each party
    party_a_votes = int(input("Enter the votes for Party A: "))
    party_b_votes = int(input("Enter the votes for Party B: "))
    party_c_votes = int(input("Enter the votes for Party C: "))

    # Create a dictionary to store results
    polling_unit_results = {
        'unit_name': unit_name,
        'party_a': party_a_votes,
        'party_b': party_b_votes,
        'party_c': party_c_votes,
    }

    return polling_unit_results

def generate_html(polling_unit_results):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Polling Unit Results</title>
    </head>
    <body>
        <h1>Results for Polling Unit: {polling_unit_results['unit_name']}</h1>
        <table border="1">
            <tr>
                <th>Party</th>
                <th>Votes</th>
            </tr>
            <tr>
                <td>Party A</td>
                <td>{polling_unit_results['party_a']}</td>
            </tr>
            <tr>
                <td>Party B</td>
                <td>{polling_unit_results['party_b']}</td>
            </tr>
            <tr>
                <td>Party C</td>
                <td>{polling_unit_results['party_c']}</td>
            </tr>
        </table>
    </body>
    </html>
    """

    with open(f"{polling_unit_results['unit_name']}_results.html", "w") as file:
        file.write(html_content)
        print(f"Results stored in {polling_unit_results['unit_name']}_results.html")

# Get input from the user
new_results = get_input()

# Generate HTML file
generate_html(new_results)
