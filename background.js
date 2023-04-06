chrome.tabs.onActivated.addListener((tab) =>{
    console.log(tab);
    chrome.tabs.get(tab.tabId,(currentTabData) =>{
        if (currentTabData.url == "https://openai.com/policies/terms-of-use") {
            var options = {
                type : "basic",
                title : "Its now in Terms and Condition page",
                message :"Check our ClearTerms Extension for a Critical Terms to be known",
                iconUrl : "save.png"
            }
            chrome.notifications.create(options,callback)
            function callback() {
                console.log("popup done!");
            }
        }
        // console.log(currentTabData);
    })
})


