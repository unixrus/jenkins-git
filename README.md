# Enable jenkins instance in docker

instructions to initialize a jenkin instance in a docker/podman container to learn the tool.


## docs and image
see [Jenkins web page](https://hub.docker.com/r/jenkins/jenkins) for jenkins container publisher and details.

## node pre-requisites
docker enabled node OR use podman in centos 8. if using podman, alias podman to docker and continue with the next steps or substitute podman in place of docker in the commands.

## steps to start jenkins instance.

* this dir will persist all your work done with the jenkins container. even if you delete the container.
	- $ mkdir $HOME/jenkins

* default id of jenkins in image is 1000, so best to match it.
	- $ sudo chown 1000 $HOME/jenkins

* then run the jenkins docker instance (needs internet to download container image)
	- $ docker run -p 8080:8080 -p 50000:50000 -v /$HOME/jenkins:/var/jenkins_home jenkins/jenkins:lts-centos

* connect to the container host running jenkins via a browser
	- typically http://localhost:8080 )
	- follow prompts to setup jenkins instance. 
        - you will need access to the localhost:$HOME/jenkins/secrets/initialAdminPassword
        - create the admin and regular user.
        - it will ask to install some standard plugins.
       
* a functional jenkins instance is now ready. login with the freshly created jenkins user logins 

* FYI- this generally indicates that jenkins instance is good 

2021-02-13 18:14:56.642+0000 [id=29]	INFO	jenkins.InitReactorRunner$1#onAttained: Completed initialization

2021-02-13 18:14:56.702+0000 [id=20]	INFO	hudson.WebAppMain$3#run: Jenkins is fully up and running
