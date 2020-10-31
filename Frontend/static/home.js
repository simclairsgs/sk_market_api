function auth(event)
{
   let emp_id = document.getElementById("emp_id").value;
   let emp_pass = document.getElementById("emp_pass").value;
   $.post('/api/login-auth/',"emp_id="+emp_id+"&emp_pass="+emp_pass,function(data,status){
     if(data.Status != null || data.Status != undefined)
     {
        if(data.Status == true)
        {   
            sessionStorage.setItem("auth_status",true)
            let data_serial = JSON.stringify(data);
            sessionStorage.setItem("employee_data",data_serial)
            window.location="/home";
        }
        else
        {
            toastr.error('Unauthorised user');
        }
     }
     else
        {
            toastr.error('Invalid Credentials');
        }
      
    });

}