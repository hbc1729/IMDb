//set button id on click to hide first modal
$("#signin").on( "click", function() {
    $('#myModal1').modal('hide');  
});
//trigger next modal
$("#signin").on( "click", function() {
    $('#myModal2').modal('show');  
});

function myFunction() {
    var x = document.getElementById("myInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

  function smyFunction() {
    var x = document.getElementById("smyInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }


  
var btns = document.getElementsByClassName('proView')

for (i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        fetchId(productId, action)

      })
}

function fetchId(productId, action){
  
  var url = "/fetch_productId/"
  fetch(url, {
    method:"POST",
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken': csrftoken,
    },
    body:JSON.stringify({'productId':productId, 'action': action})
})
.then((response)=> {
  return response.json();
})
.then((data)=>{
  console.log("Data: ",data)
})
}


  