let tryFunc = (list) =>  {
    for (let i = 0; i < list.length; i++) {
        let url = `https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/start?q=select%20${list[i]}%20from%20readme`
        fetch(url).then(function(response) {
            return response.json();
          }).then(function(data) {
            console.log(data);
          }).catch(function() {
            console.log("Booo");
          });
    }
}