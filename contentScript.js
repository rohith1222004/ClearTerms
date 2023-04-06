var paragraphs = document.getElementsByTagName('p');

// Iterate over the p tags and extract their text content
var paragraphText = " "
for (var i = 0; i < paragraphs.length; i++) {
  paragraphText =  paragraphs[i].textContent
  console.log(paragraphText);
}
//sending a data to the index.js
const data = {data : paragraphText}
fetch('http://127.0.0.1:5000/data',{
  method:'POST',
  body:JSON.stringify(data),
  headers:{'content-Type':'application/json'}
})
.then(Response =>Response.json())
.then(
    (data)=>{console.log(data.choices[0].text)
      chrome.runtime.sendMessage({data: data.choices[0].text})
    }
    

  )
.catch(err =>{console.error("ERROR",err)})

chrome.runtime.sendMessage({data: "hello from content script"});








