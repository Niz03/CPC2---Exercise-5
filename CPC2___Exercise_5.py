# Main content
welcome = "Welcome to My First HTML Program Using Python!"
name = "My name is Nizar Arjoun!"
gratitude = "Shukran! (Arabic for Thank You!)"

# Arrangement of said content
html_content = f"<html> <head> </head> <h1> {welcome} " \
               f"</h1> <h2> {name} </h2> <p> {gratitude} </p>  <body>  </body>  </html>"

# File creation
with open("exercise#5.html", "w") as html_file:
    html_file.write(html_content)
    print("HTML file created successfully !!")
