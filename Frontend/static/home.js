function auth(event)
{
   //event.preventDefault();
   let emp_id = document.getElementById("emp_id").value;
   let emp_pass = document.getElementById("emp_pass").value;
   alert(emp_id+emp_pass);
   //$.post('/api/login-auth/',"emp_id="+emp_id+"&emp_pass="+emp_pass,function(data,status){alert(status+data)});
    $.get('api/products/', function(data){alert(JSON.stringify(data))})
}