const header = document.getElementById('ModalScrollableTitle');
const body = document.getElementById('TableBody');
console.log(body);


function residents(clickedId) {
    header.innerText = `Residents of ${clickedId}`;
    body.innerHTML = '';
    let path = window.location.origin;
    let URL = path + `/residents/${clickedId}`;
    let httpRequest = new XMLHttpRequest();

    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4 && httpRequest.status === 200) {

            let data = JSON.parse(httpRequest.response);
            console.log(data);
            let tableBodyHTML = '';

            for (let row of data) {
                tableBodyHTML += '<tr>';

                for (let rowItem of row) {
                    tableBodyHTML += `<td>${rowItem}</td>`;
                }
            tableBodyHTML += '</tr>';
            }
        body.innerHTML = tableBodyHTML;
        }
    };

    httpRequest.open("GET",URL, true);
    httpRequest.send();
}