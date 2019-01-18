## Questioner
[![Build Status](https://travis-ci.org/wathigo/Questioner.svg?branch=develop)](https://travis-ci.org/wathigo/Questioner)
[![Coverage Status](https://coveralls.io/repos/github/wathigo/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/wathigo/Questioner?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/0da9658aa1c161eacb9b/maintainability)](https://codeclimate.com/github/wathigo/Questioner/maintainability)

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

### API Endpoints(v1)
| **HTTP METHOD**  | **URI**                                    |  **DESCRIPTION**           |
| -----------      | -----------                                |  ---------------           |
| **POST**         | /api/v1/auth/signup                        |  Create a new user.        |  
| **POST**         | /api/v1/auth/login                         |  Login a user.             |
| **POST**         | /api/v1/meetups                            |  Create a new meetup.      |
| **GET**          | /api/v1/meetups/upcoming                   |  Get all the meetups.      |
| **GET**          | /api/v1/meetups/<int:id>                   |  Get a specific meetup.    |
| **PUT**          | /api/v1/meetups/<int:id>                   |  Update a meetup record.   |
| **POST**         | /api/v1/meetups/<int:id>/rsvps             |  Reserve for a meetup.     |
| **POST**         | /api/v1/meetups/<int:id>/questions         |  Create a question record. |
| **PATCH**        | /api/v1/questions/<int:id>/upvote          |  Upvote a qustion.         |
| **PATCH**        | /api/v1//questions/<int:id>/downvote       |  Downvote a question.      |

### Running Tests
Enter 'coverage run --source=app -m pytest && coverage report' command to run tests.
