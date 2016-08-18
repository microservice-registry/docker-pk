# Docker Microservice template

Docker microservice template project for [CookieCutter](https://github.com/audreyr/cookiecutter)

* GitHub repo: https://github.com/microservice-registry/docker-pk
* Free software: GNU GPL license

## Features

* Initialize new microservice app based on docker
* Prepare git local repo with your remote hub
* Prepare Docker image container to install tools and launch there

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::
```shell
    pip install -U cookiecutter
```

Generate a Docker image project::
```shell
    cookiecutter https://github.com/microservice-registry/docker-pk.git
```

Generate a Docker image project from specific branch::
```shell
    cookiecutter https://github.com/microservice-registry/docker-pk.git --checkout <branch>
```

Then:

* Create a repo on your github account.
* Run ```cd <project_slug>```.
* Run ```sh gitinit.sh```.

For more details, see the [cookiecutter-pypackage tutorial](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html).

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Visit [microservice-registry](https://github.com/microservice-registry) for find more apps based on microservice projects template

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.
