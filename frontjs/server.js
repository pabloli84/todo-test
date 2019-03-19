const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const app = express();

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs')

app.get('/', function (req, res) {
  res.render('index', {weather: null, error: null});
})





app.post('/createTask', function (req, res) {
  let taskName = req.body.taskName;
  let taskDescription = req.body.taskDescription;
  let taskAssignee = req.body.taskAssignee;
  let taskStartDate = req.body.taskStartDate;
  let taskEndDate = req.body.taskEndDate;
  
  // JSON to be passed to the QPX Express API
    var requestData = {
    "task_name": taskName,
    "description": taskDescription,
    "assignee": taskAssignee,
    "start_date": taskStartDate,
    "end_date": taskEndDate
}
  let url = `https://damp-eyrie-62274.herokuapp.com/tasks`

  request({
    url: url,
    method: "POST",
    json: requestData,
    }, function (error, response, responseBody) {
       if (!error && response.statusCode === 201) {
            console.log(responseBody)
        }
        else {

            console.log("error: " + error)
            console.log("response.statusCode: " + response.statusCode)
            console.log("response.statusText: " + response.statusText)
        }
    res.statusCode = 201;
    res.setHeader('Content-Type', 'application/json');
    res.responseBody = responseBody;
    res.end(JSON.stringify(responseBody));
  });
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})