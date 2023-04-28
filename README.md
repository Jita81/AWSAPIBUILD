# AWSAPIBUILD

A lightweight Python product that allows users to deploy multiple instances of the same microservice architecture with different names. The product will include a simple way to test each deployed microservice using the API service from the app itself. The solution will be divided into two parts: a backend and a frontend.

Backend: AWS Infrastructure and Deployment

app.py: This file contains the Flask web application, handling user inputs, and triggering deployment using the AWS CDK.
cdk_app.py: This file contains the AWS CDK app definition.
microservice_stack.py: This file defines the AWS CloudFormation Stack and its resources.
requirements.txt: Lists all required Python packages.
templates/: Directory containing HTML template files.
index.html: The main HTML file for the frontend.
static/: Directory containing static files like JavaScript and CSS.
main.js: JavaScript file handling user inputs and making API calls.
The backend will be responsible for deploying and managing the microservices using AWS services. The primary AWS services used will be:

AWS Lambda: Running the microservice logic.
Amazon API Gateway: Exposing the Lambda functions as APIs.
AWS Cognito: Handling user authentication and registration.
Amazon S3: Hosting the static frontend files.
AWS Secrets Manager: Storing and retrieving API keys securely.

Frontend: User Interface and Testing

index.html: Main HTML file with a form for users to enter microservice configuration details and deploy the service.
test.html: HTML file that provides an interface for users to enter their API key and test the deployed microservice.
main.js: JavaScript file responsible for handling form submissions, deploying microservices, and performing API tests.
The frontend will be a simple web application with two pages. The first page will allow users to enter the microservice configuration details and deploy the service. The second page will provide an interface for users to test the deployed microservice by entering their API key and making API calls.

Technical Design:

The product will use Flask for the backend and a simple HTML/CSS/JavaScript frontend. The AWS infrastructure will be deployed using the AWS CDK.

Users will access the frontend hosted on Amazon S3 to enter the required configuration details for the microservice, such as service name, AWS region, and other relevant parameters.
Upon form submission, the frontend will send the configuration details to the Flask backend, which will then trigger the AWS CDK to deploy the microservice using the provided configuration.
The AWS CDK app will create a CloudFormation Stack that includes resources such as Lambda functions, API Gateway, Cognito User Pool, and Secrets Manager.
Once the deployment is complete, the user will receive a confirmation message.
Users can then navigate to the test page, where they can enter their API key and make API calls to test the deployed microservice.
The test page will use JavaScript to make AJAX calls to the microservice's API Gateway, which will forward the requests to the corresponding Lambda function.
The Lambda function will process the request, interact with the OpenAI API if required, and return the appropriate response to the frontend.
Users can see the response in the test page and verify that the microservice has been deployed correctly.
