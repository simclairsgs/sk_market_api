function change_pass()
{
    //get data
    let emp_id = document.getElementById("cemp_id").value
    let emp_old_pass = document.getElementById("cemp_old_pass").value
    let emp_new_pass = document.getElementById("cemp_new_pass").value

    if(emp_new_pass.length < 8)
   {
       toastr.error("Password too short");
   }
   else
   {
        $.post('/api/change-password/',
        "emp_id="+emp_id+"&emp_pwd_old="+emp_old_pass+"&emp_pwd_new="+emp_new_pass,
        function(data,status)
        {
            alert(data)
            window.location = "/";
        }
        )
   }

}