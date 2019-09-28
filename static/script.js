function table2html(tableData) {
    var s = "<table>";
    var tdTag;
    for (let row of tableData) {
        s += "<tr>";
        for (let value of row) {
            tdTag = value == "[BLANK]" ? "<td class=blank>" : "<td>";
            s += tdTag + value + "</td>";
        }
        s += "</tr>";
    }
    s += "</table>";
    return s;
}

function getCurrentTableData() {
    var data = [];
    $("td").each(function(index) {
        data.push($(this).text());
    })
    return data;
}

function refreshTable(newTable) {
    // remove <table> if it exists
    $("table").remove();
    // create new table after main div
    $(table2html(newTable)).appendTo("#main");
}
