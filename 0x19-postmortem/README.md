# Postmortem
![image](https://github.com/Stellanwae/alx-system_engineering-devops/assets/99267699/fc03e086-5daf-49bc-a016-56f4f5273e45)


On the 7th of August, our server infrastructure got an outage that resulted in our clients' inability to use our services. We apologise for any inconvenience incurred during this time.
# Issue Summary
![image](https://github.com/Stellanwae/alx-system_engineering-devops/assets/99267699/e9392653-72ac-4ea2-9e18-8d6a13f8ce42)

Our server experienced a downtime which lasted for two hours. Following this, our clients received a http 500 error thus affecting their normal operation in our site.
The impleemnted upgrades were not properly tested before pushing the production servers.

![image](https://github.com/Stellanwae/alx-system_engineering-devops/assets/99267699/ab125474-c025-4533-9ea8-202e8fb476f6)

* Performed a rolllback on servers
* Upgraded the current version on our servers

![image](https://github.com/Stellanwae/alx-system_engineering-devops/assets/99267699/840b70d2-d322-47c4-b73f-d765a14fe30c)


* Pushing all changes in the test environment as well as the life server
* Increase server performance by putting necessary measures to alert on-call engineers in case of a server crash

Anyhow, programmers need to continue coding because without code there would be no bugs
