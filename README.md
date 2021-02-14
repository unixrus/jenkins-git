# jenkins-git

A simple project to test jenkins git integration
And it should be triggered by any change

# Enable jenkins instance in docker

start a jenkin instance in a docker container.


## docs and image
pull down a copy of the docker file for jenkins.
see [Jenkins web page](https://hub.docker.com/r/jenkins/jenkins)

## pre-requisites
docker enabled node.

## steps to start jenkins instance.

* $ mkdir $HOME/jenkins
default id of jenkins in image is 1000, so best to match it.
* $ sudo chown 1000 $HOME/jenkins
then choose which docker image to pull
* $ docker run --rm -p 8080:8080 -p 50000:50000 -v /$HOME/jenkins:/var/jenkins_home jenkins/jenkins:lts
* $ docker run --rm -p 8080:8080 -p 50000:50000 -v /$HOME/jenkins:/var/jenkins_home jenkins/jenkins:lts-centos

* connect to the docker host running jenkins in a browser
http://$containerhost:8080/
	* follow prompts to setup jenkins instance. 
	* it will ask to install some standard plugins
	* you will need access to the $HOME/jenkins/secrets/initialAdminPassword

* this generally indicates that jenkins instance is good 

2021-02-13 18:14:56.642+0000 [id=29]	INFO	jenkins.InitReactorRunner$1#onAttained: Completed initialization

2021-02-13 18:14:56.702+0000 [id=20]	INFO	hudson.WebAppMain$3#run: Jenkins is fully up and running
