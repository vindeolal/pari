![N|Solid](https://ruralindiaonline.org/static/img/logo.png)    **People's Archive Of Rural India**

**[PARI](https://ruralindiaonline.org/)** is a digital journalism platform in India, founded by veteran journalist and former rural affairs editor of 'The Hindu', **Palagummi Sainath**. **PARI** is a volunteer-run rural journalism platform.

## Dev Setup
***
#### Clone Repositories
To start with the dev box setup, clone the pari_ansible repository.
```sh
$ git clone https://github.com/PARINetwork/pari-ansible.git
$ git clone https://github.com/PARINetwork/pari.git
```
#### Setup the Vagrant Box
Install vagrant in your machine.
Proper package for your operating system and architecture can be found here - https://www.vagrantup.com/downloads.html
After downloading and installing Vagrant, get the Vagrant box up and running as below:

```sh
$ cd pari
$ sudo vagrant up
```

To get the private key of the vagrant box, use the following command. From the console output, note the value of IdentityFile, which is the private key of vagrant box.

```sh
$ sudo vagrant ssh-config
```

Now to install the application in the vagrant box, run the ansible_playbook commands from  **pari_ansible** folder,
Commands to run the set up the application,
```sh
$ cd pari-ansible
$ pip install ansible
Create a file local.py
$ touch roles/django/templates/local.py
Add a single line "DEBUG=True" in the file local.py
$ ansible-playbook --private-key=path-of-private-key -l vagrant -u vagrant -i hosts.yml site.yml
```

The ansible-playbook command will setup all the dependencies and create a environment.
### Open pari admin and local web console
Now you can open pari admin user web console ,

    http://0.0.0.0/admin/
**Username and Password**

    username: pari
    pass: !abcd1234

and user face of the pari web page

    http://0.0.0.0


Lets look at how to use the vagrant box.

Get into the vagrant box from the pari project folder.
```sh
$ cd pari
$ sudo vagrant ssh

From within the vagrant box, to access shell,

$ cd /vagrant
$ source pari_env/bin/activate
$ python manage.py shell
```

To access database
```sh
$ cd /vagrant
$ source pari_env/bin/activate
$ python manage.py dbshell
Password: pari
```

**Basic command for psql**
> **\c**  -   to connect db
> **\dt**   -   list tables
> **\x**    -   for turning on the Expanded display

**Note**
To come out from the environment you can run
```sh
$ deactivate
```
All dependencies like gunicorn, elasticSearch and nginx are up and running in the virtual box.
```sh
To restart gunicorn
$ sudo supervisorctl restart pari:gunicorn_pari
To restart nginx
$ sudo service nginx restart
```
### Tech stack:

* [Django](https://www.djangoproject.com/) - Ease the creation of complex, database-driven websites.
* [Wagtail](https://wagtail.io/) - CMS on top of Django framework
* [Python](https://www.python.org/) - Features a dynamic type system and automatic memory management and supports multiple programming paradigms.
* [Bootstrap](http://getbootstrap.com/) - Great UI boilerplate for modern web apps
* [jQuery](https://jquery.com/)

## How to contribute ?
***

##### Sign up for stories
Pickup stories from  [Pari Projects](https://github.com/PARINetwork/pari/projects/1) and sign up. Choose the stories that are **ready for Dev**. Drag and drop the story you picked in to **In Dev** column. Make sure that, task you done on the story staisfies the acceptance criteria(In scope) of the story. If you want to sign up for specific stories feel free to ask through the **Collaboration channels**.

##### Completion of stories
After you completes stories you can drag and drop the story to **Ready For QA** column.

## Collaboration channels
----
To keep in tech with technical team and the pari team,you can use the [**google group**](). If you thought of contributing to **PARI** this is one of the media that you can use. In the case of doubts and queries you can use the group.
And you can participate in the IPM's and showcase for the PARI project.

## Roadmap of features
---

### Goals
- Increase discoverability of Pari's content
- Increase interactions on social media
- Increase donations on the site
- Increasing content contributed by existing volunteers
- Sign up of new volunteers who contribute content

### Roadmap

| Realease 1 features|
|:--------:|
|`CI/CD setup`|
|`Make Development OSS Friendly`|
|`CMS - Data structure`|
|`Information architecture of website` |
|`Website UI revamp`|
|`Setting the default style`|
|`Optimising SEO for regional language translations for articles `|
|`SEO for pari website`|
|**Realease 2 features**|
|`Articles`|
|`Faces`|
|`Resources`|
|`Talking albums`|
|`Videos`|
|`Audios`|
|`Albums (pics, talking pics)`|
|`Maps`|
|`One-offs`|
|**Realease 3 features**|
|`Language selection `|
|`Translations`|
|`Improve elastic search`|
|`Improve search for specifc data on website`|
|`Social Sharing`|
|`Contributions`|
|`PARI Analytics`|
|`Editing articles for publishing `|
|**Realease 4 features**|
|`Editing articles for publishing `|
|`CMS - Bulk upload`|
|`CMS - Data language`|
|`CMS - Editing `|
|`Showcase grindmill content`|
|`Manage Grindmill Content`|







### Copyright
---
Licensed under the 3-clause BSD License. Please refer the LICENSE.txt for details.
