# Serverless-Feedback-System

A **cloud-native, serverless feedback collection system** built using **AWS services**, designed to seamlessly collect, store, and notify administrators about user feedback.  
This system can be easily integrated into **multiple websites** using a single feedback link.

---

## Project Overview

The **Serverless Feedback System** allows users to submit feedback through a simple web interface.  
The backend is completely **serverless**, ensuring **high scalability, low operational cost, and minimal maintenance**.

Once feedback is submitted:
- Data is securely stored in DynamoDB
- Admins are notified instantly via email
- The system scales automatically based on traffic

---

## Key Features

- Fully **serverless architecture**
- Scalable and cost-efficient AWS solution
- Real-time email notifications to admin
- Secure API endpoints using AWS API Gateway
- Easy integration with multiple websites
- High availability and fault tolerance

---

## Tech Stack

| Component            | Technology Used            |
|---------------------|----------------------------|
| Frontend Hosting    | Amazon EC2                 |
| API Layer           | Amazon API Gateway (REST)  |
| Backend Logic       | AWS Lambda (Python)        |
| Database            | Amazon DynamoDB            |
| Email Notification  | Amazon SES                 |
| IAM & Security      | AWS IAM Roles & Policies   |

---

## Workflow

1. User submits feedback via the web interface
2. API Gateway receives the request
3. AWS Lambda processes the feedback
4. Feedback data is stored in DynamoDB
5. Amazon SES sends a notification email to the admin
6. Admin can review feedback anytime from the database

---

## AWS Services Used

- **Amazon API Gateway** – Handles incoming HTTP requests
- **AWS Lambda** – Serverless backend processing
- **Amazon DynamoDB** – NoSQL database for feedback storage
- **Amazon SES** – Sends email notifications on new feedback
- **Amazon EC2** – Hosts the frontend web application
- **AWS IAM** – Manages permissions and security

---

## Security Considerations

- IAM roles with least privilege access
- Secure API Gateway endpoints
- No hardcoded credentials
- Encrypted data storage in DynamoDB

---

## Scalability & Performance

- Auto-scales automatically with traffic
- No server management required
- Handles high traffic with minimal latency
- Pay-as-you-go cost model

---

## Use Cases

- Website feedback collection
- Product reviews
- Customer satisfaction surveys
- Internal company feedback systems
- Support & contact forms

---

## Future Enhancements

- Admin dashboard for viewing feedback
- User authentication (Cognito)
- Analytics and reporting
- Multi-language support
- Spam protection (reCAPTCHA)

---

If you like this project, don’t forget to star ⭐ the repository!

