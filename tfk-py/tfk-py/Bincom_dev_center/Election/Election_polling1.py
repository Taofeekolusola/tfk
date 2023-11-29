def generate_html(polling_unit_results):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Election Results</title>
    </head>
    <body>
        <h1>Election Results for {polling_unit_results['unit_name']}</h1>
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

    with open("election_results.html", "w") as file:
        file.write(html_content)

# Sample election results (replace this with your actual data)
polling_unit_results = {
    'unit_name': 'Polling Unit 001',
    'party_a': 150,
    'party_b': 120,
    'party_c': 80,
}
#Generate HTML file
generate_html(polling_unit_results)
