### Final Project for REST-Oriented Architecture - Semester 4

<p>Clone the repository</p>

```bash
$ git clone https://github.com/javokhirbek1999/auction-server-side.git
```

<p>Once you have cloned the repo, make sure you have the base requirement, which is <a href="https://www.docker.com/", target="_blank">Docker</a></p>


<hr>
<p>Once you have installed the <a href="https://www.docker.com/">Docker</a>. Just run the following shell command:</p>

```bash
$ docker-compose build
```

The above shell command builds project and sets up the project automatically as a docker server.

Once the build is finished, run the following bash command:

```bash
$ docker-compose up
```

The above command basically starts the project in docker container.


The API is documented fully in Swagger for easy client side integration:

Once the project is running, you can visit the following URL to see the documentation:

```bash
http://localhost:8000/api/documentation/swagger/schema
```
You will get the following view:
![Imgur](https://imgur.com/EdjJsSv.png)

You can explore all the api endpoints and all interactively test the api by sending requests