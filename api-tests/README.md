# API tests 

API test are written using cypress.io JS framework. 

Tests located in folder ```cypress/integration```

## How to run test for debugging 
``./node_modules/.bin/cypress open`` or
``cypress open``

## How to run tests headless

``npm test`` or ``./node_modules/.bin/cypress run``

## Config 

File is cypress.json 
Currently only baseUrl is configured

#### How to path your own config 

``npm test --config baseUrl=https://myapp.com``
