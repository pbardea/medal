function MedalCtrl($scope, $http) {
  $scope.competitors = [
    {name:'Canada', score:500},
    {name:'US', score:3}];

  $scope.filter = '';

  $scope.getMedals = function() {
   $http({method: 'GET', url: '/scores'}).
      success(function(data, status, headers, config) {
        $scope.competitors = data;
      }).
      error(function() {
        alert("Bad stuff happened!");
      });
  }

  $scope.filteredCompetitors = function() {
    if ($scope.filter == ''){
      return $scope.competitors;
    }
    filtered = _.filter($scope.competitors, function(x) {
          var country = x.name.toLowerCase();
          return country.indexOf($scope.filter.toLowerCase()) != -1;

        })
    return filtered;
  }

  $scope.getMedals();
}


// var myApp = angular.module('myApp',[])
// 
// myApp.controller('MedalCtrl', ['$scope', function($scope) {
//    $scope.countries = [{name:"Canada", score:500}, {name:"US", score:3}];
// }]);
