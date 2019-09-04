$(document).ready(function(){
 $(document).on("click", "#button", function(){
  var url = '/cgi-bin/http.cgi';
  var input = document.getElementById("data_input").value;
  var postData = {test:'ok',input:input};
  $.get(url, postData).done( function (data, status) {
    $("#myModal").modal('show');
    $("#html").html("<h3>"+data+"</h3>");
  });
 });
});
