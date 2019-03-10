M.AutoInit();

// NAVBAR mobile
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
});

// add.html
const cnt = document.getElementById('toDoCnt')
cnt.value = 0