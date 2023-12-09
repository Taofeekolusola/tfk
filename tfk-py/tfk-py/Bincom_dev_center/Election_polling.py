from http.server import SimpleHTTPRequestHandler
import socketserver
import os

# Sample election results (you can replace this with your actual data)
polling_unit_results = {
    'unit_name': 'Polling Unit 001',
    'party_a': 150,
    'party_b': 120,
    'party_c': 80,
}

# Create a simple HTML page dynamically
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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

# Write the HTML content to a file
with open('index.html', 'w') as f:
    f.write(html_content)

# Set up a simple HTTP server to serve the HTML file
Handler = SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('127.0.0.1', 8000), Handler)

print("Open your web browser and go to http://127.0.0.1:8000/")
httpd.serve_forever()
