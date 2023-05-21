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

            document.getElementById("main_div").style.display = "none";
            console.log("nothing");

        }else{
            let objKey = Object.keys(x)
            for(let i = 0;i<objKey.length;i++){
                console.log(x[objKey[i]]);
            }
        }
    }
}

function clicked(n){
    document.getElementById("MainDiv").style.display = "none";
    document.getElementById("CompDiv").style.display = "block";
    http.open("GET", mainURL + "add/" + n);
    http.send();
}

function freeInput(){
    let inputData = document.getElementById("freeInput").value;
    document.getElementById("MainDiv").style.display = "none";
    document.getElementById("CompDiv").style.display = "block";

    http.open("GET",mainURL + "free/" + inputData);
    http.send();
}