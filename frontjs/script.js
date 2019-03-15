var testApp = angular.module("testApp", []);
var appAddr = "http://127.0.0.1:5001"
testApp.controller("testController", function($scope, $http) {
  $scope.home = "This is the homepage";

  $scope.getUsers = function() {
    console.log("I've been pressed!");
    $http.get(appAddr.concat("/users")).then(
      function successCallback(response) {
        $scope.response = response;
      },
      function errorCallback(response) {
        console.log("Unable to perform get request");
      }
    );
  };
  $scope.addUser = function(user_name) {
    let data = {"user_name": user_name}
    console.log("going to add ", data)
    $http.post(appAddr.concat("/users"), data).then(
      function successCallback(response) {
        console.log("Successfully POST-ed data");
      },
      function errorCallback(response) {
        console.log("POST-ing of data failed");
      }
    );
  };
});