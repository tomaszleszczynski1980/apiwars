const header = document.getElementById('ModalScrollableTitle');
const body = document.getElementById('TableBody');

function residents(clickedId) {
    header.innerText = `Residents of ${clickedId}`;
    body.innerHTML = '<img src="/static/img/loading.gif">';
    let path = window.location.origin;
    let URL = path + `/residents/${clickedId}`;
    let httpRequest = new XMLHttpRequest();

    httpRequest.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {

            let data = JSON.parse(this.response);
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