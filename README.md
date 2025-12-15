## Overview
With this codelab, we will demonstrate a simple, easy-to-do method for setting up AlloyDB and connecting our application to it. It is a quick L100 level learning to upgrade the developer experience for integrating advanced AI applications to sophisticated data features that AlloyDB has to offer.

## What you’ll build
A simple web application.
As part of this, you will:

1. Create an AlloyDB instance and cluster in one click installation
2. Create a sample application to connect to this instance and set up data
The application will just connect to the database setup you did in step 1 and will create a table and insert one record in it.


## Database setup
In this lab we'll use AlloyDB as the database for the test data.  It uses clusters to hold all of the resources, such as databases and logs.  Each cluster has a primary instance that provides an access point to the data. Tables will hold the actual data.  

Let’s create an AlloyDB cluster, instance and table where the test dataset will be loaded. 

1. Click the button or Copy the link below to your browser where you have the Google Cloud Console user logged in.  

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/AbiramiSukumaran/easy-alloydb-setup&cloudshell_open_in_editor=README.md)


2. Once this step is complete the repo will be cloned to your local cloud shell editor and you will be able to run the command below from with the project folder (important to make sure you are in the project directory):


#### sh run.sh



3. Now use the UI (clicking the link in the terminal or clicking the “preview on web” link in the terminal.

4. Enter your details for project id, cluster and instance names to get started.

5. Go grab a coffee while the logs scroll & you can read about how it’s doing this behind the scenes here.

## Create the sample application to test the connection

1. In the Cloud Shell Terminal, run the following command

git clone https://github.com/AbiramiSukumaran/verify-easy-alloydb-connection


2. Make changes to the verify_connection.py file for your AlloyDB setup you just configured in the last section:

# Replace this with the Private IP of your AlloyDB Instance
DB_HOST = <<>> 
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
# Replace this with your actual AlloyDB password    
DB_PASS = <<>>


If you want to test it locally or from anywhere, go to the AlloyDB instance, click “EDIT” and click “Enable Public IP” or “Public IP Connectivity” (not the outbound one) and enter “0.0.0.0/0” in “Authorized External Networks” for development purposes but once done, remove & disable public ip connectivity.

3. Deploy to Cloud Run

In the Cloud Shell Terminal make sure you are inside your main folder and within the project folder. 

Once you are sure you are in the project folder, run the following command:

gcloud beta run deploy verify-alloydb \
    --source . \
    --region=us-central1 \
    --network=easy-alloydb-vpc \
    --subnet=easy-alloydb-subnet \
    --allow-unauthenticated \
    --vpc-egress=all-traffic



Once deployed, you should receive a deployed Cloud Run Endpoint that looks like this:

https://verify-alloydb-**********-uc.a.run.app/
Demo

4. To confirm it worked you can see the result on the browser or the logs explorer. 

5. You can navigate to the AlloyDB on Google Cloud Console and open the newly created instance. Click “AlloyDB Studio” from the navigation pane on the left and connect with your credentials.

In the studio, on the left pane, refresh the database objects and you should see the newly created table with one row inserted.
