def generate_html(local_govts, selected_local_govt, total_results):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Summed Election Results</title>
    </head>
    <body>
        <h1>Select Local Government</h1>
        <form method="post" action="/results">
            <label for="local_govt">Local Government:</label>
            <select name="local_govt" id="local_govt">
                {"".join(f"<option value='{govt}'>{govt}</option>" for govt in local_govts)}
            </select>
            <button type="submit">Show Results</button>
        </form>
        
        <h2>Summed Election Results for {selected_local_govt}</h2>
        <table border="1">
            <tr>
                <th>Party</th>
                <th>Total Votes</th>
            </tr>
            <tr>
                <td>Party A</td>
                <td>{total_results['party_a']}</td>
            </tr>
            <tr>
                <td>Party B</td>
                <td>{total_results['party_b']}</td>
            </tr>
            <tr>
                <td>Party C</td>
                <td>{total_results['party_c']}</td>
            </tr>
        </table>
    </body>
    </html>
    """

    with open("summed_results.html", "w") as file:
        file.write(html_content)

def calculate_total_results(polling_units):
    total_results = {'party_a': 0, 'party_b': 0, 'party_c': 0}

    for unit_results in polling_units.values():
        for party, votes in unit_results.items():
            total_results[party] += votes

    return total_results

# Sample data structure for polling unit results
polling_units = {
    'Local Govt 1': {
        'Polling Unit 001': {'party_a': 50, 'party_b': 30, 'party_c': 20},
        'Polling Unit 002': {'party_a': 40, 'party_b': 25, 'party_c': 35},
    },
    'Local Govt 2': {
        'Polling Unit 003': {'party_a': 60, 'party_b': 40, 'party_c': 30},
        'Polling Unit 004': {'party_a': 55, 'party_b': 35, 'party_c': 25},
    },
}

# Extract local government names
local_govts = list(polling_units.keys())

# Default selection
selected_local_govt = local_govts[0]

# Calculate total results for the default selection
total_results = calculate_total_results(polling_units[selected_local_govt])

# Generate HTML file
generate_html(local_govts, selected_local_govt, total_results)
