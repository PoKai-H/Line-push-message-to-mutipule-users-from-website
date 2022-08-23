# Line_Pushing-Message-to-Mutiple-Users
<h3>Using Django to Create a Web server for managing and pushing message to group users<h3>
<h6>
Step1:Add your channel access token to the AccessToken.py<br>
Step2:Print out event and get userids from message events (you will get different userID from different linebots)<br>
Step3:Create groups and add userid to those group in sqlite by visiting 127.0.0.1:3000/admin<br>
Step4:Create messages you like to push and choose which group to push by visiting 127.0.0.1:3000/Message/create<br>
Step5:Press submit than users in the group you choose will get the message you sent
