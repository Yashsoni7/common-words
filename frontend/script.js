
function get_url() {
	let urlValue;
	urlValue = document.getElementById('url').value;
	console.log(urlValue);
	send_data({"url":urlValue});
}

function send_data(data){
	fetch('http://127.0.0.1:8000/', {
			method: 'POST', // or 'PUT'
            headers: {
				'Content-Type': 'application/json',
			},
			json:true,
			body: JSON.stringify(data),
        })
		.then((response) => { return response.json()})
		.then((json_data)=>{
			renderQuery(json_data);
		})
		.catch((error) => {
			console.error('Error:', error);
		});
}

function renderQuery(data) {
	console.log(data.length);
	
    if (data.length) {
		var my_list = new Array();
		my_list.push(["Word","Frequency"]);
		for(i=0;i<data.length;i++){
			console.log(i);
			my_list.push([data[i]["word"],data[i]["freq"]])
		}
		console.log("Array is ",my_list);
		
		var table = document.createElement("TABLE");
        table.border = "1";
 
        var columnCount = my_list[0].length;
 
        var row = table.insertRow(-1);
        for (var i = 0; i < columnCount; i++) {
            var headerCell = document.createElement("TH");
            headerCell.innerHTML = my_list[0][i];
            row.appendChild(headerCell);
        }
 
        for (var i = 1; i < my_list.length; i++) {
            row = table.insertRow(-1);
            for (var j = 0; j < columnCount; j++) {
                var cell = row.insertCell(-1);
                cell.innerHTML = my_list[i][j];
            }
        }
 
        var dvTable = document.getElementById("myTable");
        dvTable.innerHTML = "";
        dvTable.appendChild(table);
    }
    else {
		console.log("No Value");
    }	

}
