function register()
{   
    //get data from html
   let remployee_name = document.getElementById("remp_name").value;
   let remployee_pass = document.getElementById("remp_pass").value;
   let remployee_num = document.getElementById("remp_mobile").value;
   let remployee_dob = document.getElementById("remp_dob").value;
   let remployee_addr = document.getElementById("remp_address").value;
   let remployee_mail = document.getElementById("remp_email").value;
   let employee_doj = new Date().toDateString()
   // verify data
   if(remployee_pass.length < 8)
   {
       toastr.error("Password too short");
   }
   else
   {
        //post to api
        $.post('/api/register-user/',"name="+remployee_name+"&pass="+
        remployee_pass+"&num="+remployee_num+"&dob="+remployee_dob+
        "&addr="+remployee_addr+"&mail="+remployee_mail+"&doj="+employee_doj,
        function(data,status){
            if(status=="success")
            {
                alert("Your Employee Id is\n"+data.Employee_Id)
                window.location="/"
            }
            
            })

   }
   
}