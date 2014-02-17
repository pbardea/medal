function MedalCtrl($scope, $http) {
  $scope.competitors = [
     {name:'Loading...', score:'Loading...', rank:'Loading...'}];

  $scope.filter = '';
  $scope.minScore = 0;

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
      nameFiltered = $scope.competitors
    }else{
      nameFiltered = _.filter($scope.competitors, function(x) {
          var country = x.name.toLowerCase();
          return country.indexOf($scope.filter.toLowerCase()) != -1;
      })
    }

    if ($scope.minScore){
      filtered = _.filter(nameFiltered, function(x) {
          return x.score >= $scope.minScore;
      })
    }
    else{
      filtered = nameFiltered;
    }

    return filtered;
  }

  $scope.getMedals();
}


// var myApp = angular.module('myApp',[])
// 
// myApp.controller('MedalCtrl', ['$scope', function($scope) {
//    $scope.countries = [{name:"Canada", score:500}, {name:"US", score:3}];
// }]);
