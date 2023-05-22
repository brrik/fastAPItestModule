const mainURL = "https://my-fast-api-app.onrender.com/";
let http = new XMLHttpRequest();

http.onreadystatechange = function() {
    if(http.readyState === 4 && http.status === 200) {
        let x = null;
        let res = null;
        res = http.responseText;
        x = JSON.parse(res);
        console.log(x);
        if(x == null || x == undefined || Object.keys(x).length == 0){

            console.log("nothing");
            while(divElem.lastChild){
                divElem.removeChild(divElem.lastChild);
            }

        }else{
            let objKey = Object.keys(x)
            if(objKey[0]=="c1"){
                document.getElementById("selectOutput").style.display = "block";
                document.getElementById("freeOutput").style.display = "none";

                for(let i = 0;i<objKey.length;i++){
                    let keyName = objKey[i];
                    document.getElementById(keyName).innerText = x[keyName];
                }

            }else{
                document.getElementById("selectOutput").style.display = "none";
                document.getElementById("freeOutput").style.display = "block";

                let divElem = document.getElementById("freeOutput");
                try{
                    while(divElem.lastChild){
                        divElem.removeChild(divElem.lastChild);
                    }
                }catch(exceptionVar){
                    console.log(exceptionVar)
                }finally{
                    for(let i = 0; i<objKey.length;i++){
                        let keyName = objKey[i];
                        console.log(keyName)
                        let newElem = document.createElement("h2");
                        newElem.innerText = x[keyName];
                        y = divElem.appendChild(newElem)
                    }
                }
            }
        }
    }
}

function resetData(){
    http.open("GET", mainURL + "reset");
    http.send();
}

function getData(){
    http.open("GET", mainURL + "result");
    http.send();
}

let timerID = setInterval(getData, 1000);
