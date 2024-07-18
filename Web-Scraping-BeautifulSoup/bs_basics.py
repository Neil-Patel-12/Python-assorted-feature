from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

# Beautifulsoup(html_string, "html.parser") - parse HTML

soup = BeautifulSoup(html, "html.parser")

d = soup.find_all(class_="special")
print(d, "\n")

# select - returns a list of elements matching a CSS selector
# select by id: #foo
# select by class: .bar
# select children: div > p
# select descendents: div p
d = soup.select("[data-example]")
print(d, "\n")

d = soup.select("#first")
print(d, "\n")

d = soup.find_all(attrs={"data-example": "yes"})
print(d, "\n")


"""
Accessing Data in Elements
-> get_text: access the inner text in an element
-> name: tag name
-> attrs: dictionary of attributes
-> can also access attribute values using brackets!
"""

m = soup.select(".special")[0].get_text()
print(m, "\n")