## Questioner
[![Build Status](https://travis-ci.org/wathigo/Questioner.svg?branch=develop)](https://travis-ci.org/wathigo/Questioner)

This is a platform where users can post questions that they want addressed during a meetup. Those who want to  attend can then upvote or downvote the question. Users can also comment to a question.
Here are the concepts that are necessary for completion of this project:

1. Pivotal tracker [here](https://www.pivotaltracker.com/n/projects/2235674)
2. Test Driven Development(TDD).
4. Object Oriented Programming.
5. Data structures.
6. Continous Integration with TavisCl.
7. Flask-restful.

### Getting Started
This project requires a number of the following packages installed.

### Prerequisites
1. Pip
2. Python 3.6

### How to run API
1. Enter 'git clone https://github.com/wathigo/Questioner.git' to clone this repository.
2. Install a virtual environment 'pip install virtualenv'.
3. Create a virtual environment 'virtualenv myenv'.
4. Activate the environment 'source myenv/bin/activate'.
5. Install the necessary packages 'pip install -r requirements.txt'.
6. Enter 'Flask run' to test the API.

### Running Tests
Enter 'coverage run --source=app -m pytest && coverage report' command to run tests.
