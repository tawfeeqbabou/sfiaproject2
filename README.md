# sfiaproject2

* [Brief](#brief)
    * [Additional Requirements](#additional-requirements)
* [Build Instructions For Application](#build-instructions-for-application)
* [Planning](#planning)
* [Application Structure](#application-structure)
    * [Risk Assessment](#risk-assessment)
    * [Risk Assessment Updates](#risk-assessment-updates)
    * [CI Pipeline](#ci-pipeline)
* [Automated Testing](#automated-testing)
* [Front-End Design](#front-end-design)
    * [Screenshots](screenshots)
* [Issues and Challenges](issues-and-challenges)
* [Future Improvements](#future-improvements)
* [Authors](#authors)
* [Acknowledgments](#Acknowledgements)

# [(For Presentation click here)](https://drive.google.com/file/d/1HzHP5fvzp_T-OpQBZvpigLzSFkZ3x1cm/view?usp=sharing)
# Brief

The following README document takes the user through the second project we have been  <br> 
tasked with creating an application focused on executing service oriented architecture  <br> 
with four services working together.
<br></br>

This was to implement CI, cloud fundamentals and additional python skills we had learnt<br>
since our first Flask App project.
<br></br>

## Additional Requirements
We were expected to display use of the following tools and skills:

* Kanban Software
* Risk Assessment
* Source Control and appropriate use of dev and feature branches
* Webhooks to ensure code changes are updated and comtinually integrated.
* 4 seperate services interacting in unison
* Successful deployment of app
* Use of Ansible playbook 
* Use of reverse proxy
* Nginx for load balancing (recommended)<br><br>

# Build Instructions For Application
Here are build instructions for the user to set up and deploy the application.

1. Head to https://console.cloud.google.com and set up Virtual Machine instances <br>
namely: _**-Ansible-Jenkins -manager -worker -nginx**_
<br><br>
2. Make sure to generate _**SSH keys**_ and add them to Ansible-Jenkins VM in GCP with the following commands:
* ssh-keygen 
* cat ~/.ssh/id_rsa.pub
3. Head back to VSCode and open remote connection (bottom left corner) and connect to new host <br>
within Ansible-Jenkins VM with your _**username@\<VM ip address\>**_
<br><br>
4. Run the _**sudo apt update**_ command in your working terminal
<br><br>
5. Clone down your repo using the following command so that you can maintain source control requirements:
* git clone \<https github repo link\><br>
_(Step 5 will be essential for setting up your webhook within Jenkins automation)_
6. You now need to open a new host connections to run _**manager**_ and _**worker**_ VMs <br>(repeat step 2 and 3 with out ssh-keygen command)<br><br>
7. **Docker**: in order to deploy app you will need to run docker-compose.
* Create docker.sh file and enter the official script from https://get.docker.com\ <br> inside the file:
<br>i. sudo apt-get update
<br>ii. sudo apt install curl -y
<br>iii. curl https://get.docker.com | sudo bash
<br>iv. sudo usermod -aG docker $(whoami)<br><br>
8. Install _**nginx**_ and configure it using the following command:<br> * _**sudo apt install -y nginx**_ <br><br>
9. you still need to edit the nginx configuration file (nginx.conf)(which is our load balancer) use the following<br>
code in the aforementioned file:<br>

![nginxconfig](./images/nginxconfig.png)<br>
(You will need to change the ip addresses to the _**2 VM private addresses**_ you should have from _**step 6**_)<br><br>
10. Finally activate Ansible to deploy using _**ansible-playbook -i inventory.yaml playbook.yaml**_.

# Planning
Here is my Trello kanban board which shows how I planned and went <br>
about breaking user stories and sprints down into steps.<br>
![trello](./images/trello2.png)

#   Application Structure
![trello modifications](./images/trello3.png)
<br><br>
As you can see, my original plan was to have CRUD functionality and a corresponding <br>
database. My idea for the app changed as I spent increasing time troubleshooting mainly Ansible, and syntax errors.<br>
<br>

## Original app architecture vs current displayed below:
![App architecture and iteration](./images/App%20architecture%20and%20iteration.jpg)
<br><br>

# Risk Assessment
<br>
My risk assessment pertains to the risks I found to be most common for the type of app we <br>
building. I wanted to avoid including every generic possibility. I focused on adding risk assessments.

## Risk Assessment Updates
<br>

![risk assessment pic](./images/Risk%20matrix%20sfia2.jpg)
As you can see I have visited my risk assessment with new learning, considerations and <br> 
 the application of security measures.

## CI Pipeline

![CI Pipeline](./images/CI%20pipeline%20finished.png)

# Automated Testing

I successfully ran automated tests through jenkins here are my coverage reports <br>
for each service within the application.

## Test 1 For Service1 92%

![test1](./images/Jenkins%20test%201%20cov%20report.jpg)

## Test 2 For Service2 89%

![test2](./images/Jenkins%20test%202%20cov%20report.jpg)

## Test 3 For Service3 89%

![test3](./images/Jenkins%20test%203%20cov%20report.jpg)

## Test 4 For Service4 59%

![test4](./images/Jenkins%20test%204%20cov%20report.jpg)

# Front-End Design

The front-end of the application was admittedly my least focused on area, reverting to the <br>
bare bones minimal template learned early on in QA Community.<br><br>
My mainreason for this was wanting to make sure that I allocated the majority of my time to <br>
functionaity for the end user rather than fancy design.

## Screenshots

app screenshot1
![app screenshot1](./images/sfia%20pic1.png)

app screenshot2
![app screenshot2](./images/sfia%20pic2.png)

app screenshot3
![app screenshot3](./images/sfia%20pic3.png)

<br><br>

# Issues and Challenges
1. _**Ansible**_: I was unfortunately unable to implement Ansible. See error below.
* Troubleshooting: Created new VM, re wrote script in _roles folder/tasks_,
* 
2. Docker Swarm: I kept coming across an error where Docker Swarm would deploy <br>
but my web page would keep displaying web address unreachable.
    * Troubleshooting: My first approach was to check through each service and see which <br>
if not all services were failing to run.
    * Eventually it was apparent that it was only my port 5000, which was <br>running my service1 
    , not connecting. I ran _**sudo docker log ls**_ and saw that Docker wasn't replicating service1.
    <br> I went back through my docker file in service1 and identified a mispelling <br>in the username of my docker file

## Future Improvements

In the future I would like to add CRUD functionality and expand on implementing <br>
JS, CSS and advanced HTML to make the app more engaginng and increase user experience.<br>
I have grown to appreciate how much time troubleshooting issues takes and re-evaluate <br>
how much time I allocate to building apps in comparison to how long I will reserve for debugging apps.

# Authors

Tawfe'eq Babou

# Acknowledgments

I would like to extend my sincerest thank you to Ryan Wright for making learning engaging, insightful <br>
and relatable. He is the tutor I have spent the most time with and learnt the most from.<br>
Always, patient and always willing to help. Ryan has been instrumental to my increased love in tech!