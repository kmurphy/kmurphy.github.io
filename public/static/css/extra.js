<!-- Global site tag (gtag.js) - Google Analytics -->

  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-165447204-1');



function stringToHash(string) { 
            
    var hash = 0; 
    
    if (string.length == 0) return hash; 
    
    for (i = 0; i < string.length; i++) { 
        char = string.charCodeAt(i); 
        hash = ((hash << 5) - hash) + char; 
        hash = hash & hash; 
    } 
    return hash; 
} 

function checkAnswer(correct, answer) {
    if (stringToHash(answer)==correct) {
        message = "Great, answer is correct!";
    } else {
        message = "Wrong answer, try again ";// + stringToHash(answer);
    }
    document.getElementById("checkAnswerResponse").textContent = message;
}