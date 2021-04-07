function getTableSums(tableId, endTableId){
    var tds = document.getElementById(tableId).getElementsByTagName('td');
    var sum = 0;
    for(var i = 0; i < tds.length; i ++) {
        if(tds[i].className == 'count-me') {
            sum += isNaN(tds[i].innerHTML) ? 0 : parseInt(tds[i].innerHTML);
        }
    }
    document.getElementById(endTableId).innerHTML += '<tr><td>' + sum + '</td><td>total</td></tr>';

}