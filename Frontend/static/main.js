if(!sessionStorage.getItem("auth_status"))
{
    window.location='/';
}
const data = JSON.parse(sessionStorage.getItem("employee_data"))

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
    document.getElementById("husrnm").innerHTML=data.Employee_Name;
  });

function logout(e)
{
    e.preventDefault();
    sessionStorage.clear();
    window.location = '/';
}

function billing(e)
{
    e.preventDefault();
    document.getElementById("main-content").src = '/billing'
}

function product_enq(e)
{
    e.preventDefault();
    $('#main-content').attr('src','/products-enq')
}

function stock_enq(e)
{

    e.preventDefault();
    document.getElementById("main-content").src = '/stock-enq'
}