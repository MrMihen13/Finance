# Finance


- [Technical requirements for developers](#technical-requirements-for-developers)
- [Local run](#local-run)
    - [Local run without](#local-run-without-docker-compose)
    - [Local run with docker-compose](#local-run-with-docker-compose)
- [Project documentations](#project-documentation)
- [Environments and dependencies](#environments-and-dependencies)

-------------------------------------------------------------------------

## Technical requirements for developers

[Technical requirements for developers](./docs/technical_requirements.md)

-------------------------------------------------------------------------

## Local run

### Local run without docker-compose

1. Create `.env` file, copy there environment variable from `.emv.template` and set values for environments and dependencies
2. Creating virtual [environment](#environments)
3. Run command `>> python manage.py migrate` for complete project migrations
4. Run command `>> python manage.py collectstatic` for collect project`s static files
5. Run command `>> python manage.py runserver` for run local server

If you did everything correctly, you will see this text in your console.

```
System check identified no issues (0 silenced).
April 17, 2022 - 18:46:34
Django version 4.0.4, using settings 'finance.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Local run with docker-compose

For [run](#up-containers) this project with using docker-compose, use the commands below.

***Warning!***

***To run the following commands, you must be in the root folder of the project.***

#### Build containers

```commandline
 docker-compose build
```

#### Up containers

```commandline
 docker-compose up
```

#### Down containers

``` commandline
 docker-compose down
```

#### Remove containers

```commandline
 docker-compose rm finance
```

-------------------------------------------------------------------------

## Environments and dependencies

### Environments

The project uses [Pipenv](https://docs.pipenv.org/) to create a virtual environment. If Pipenv is not installed on uour computer, you need [install](https://docs.pipenv.org/install/#installing-pipenv) it.

 For create a virtual environment, enter the following command in the root folder of the project.

```commandline
 pipenv shell
```

 This command creates a virtual environment using Python version 3.10. If you do not have this version installed, you need to [install](https://www.python.org/downloads/release/python-3108/) it. 
 
 After creating a virtual environment, you need to install all the dependencies from the [Pipfile](#dependencies).

 ``` commandline
 pipenv install
 ```


### Dependencies

Information about dependencies is available in the [Pipfile](./Pipfile)

-------------------------------------------------------------------------

## Project documentation

Project documentations is avaliable [here](./docs/project_documentations.md)

-------------------------------------------------------------------------