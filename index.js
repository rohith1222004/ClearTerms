  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.data) {
      var dataElement = document.getElementById("data");
      dataElement.textContent = request.data;
    }
  });

  console.log(data);


  
  
  
  