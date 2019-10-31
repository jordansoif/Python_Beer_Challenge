How to run:

1. To run app.py: Enter "python app.py" in the terminal.

2. The terminal will load input lines, in which you can answer them and receive the results.

3. To run tests(test_app.py): Enter "python test_app.py" or "python -m unittest" in the terminal

Design choices explained:

1. I put beers.csv and breweries.csv in the folder so the information can be accessed at anytime even if the website they originated from goes down.

2. Type checking is used throughout app.py to ensure that each function will run as expected and has the necessary error/ return message in case an input is not what it is supposed to be.

3. Functions have the input lines outside of them and take them in as arguments which makes for easier testing. Also, input lines only return strings so testing with different types gives me the ability to test for issues that may arrise from these different arguments.

4. I am only using input in this situation for ease of use. I wanted to make the app so it is very easy to run in the terminal.
