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

function forgot()
{
    let emp_id = document.getElementById("femp_id").value
    let emp_dob = document.getElementById("femp_dob").value
    let emp_mail = document.getElementById("femp_mail").value

    toastr.warning("Please Wait...\nIt may take upto 10 sec.")
    $.post('/api/forgot-password/',
    "emp_id="+emp_id+"&emp_dob="+emp_dob+"&emp_mail="+emp_mail,
    function(data,status)
    {
        alert(data)
        window.location = "/";
    }
    )
}