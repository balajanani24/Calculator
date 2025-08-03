#!C:\Python3.12\python.exe
print("Content-Type:text/html \n\r")
import pymysql
import webbrowser
import cgi

f = cgi.FieldStorage()
name=f.getvalue('name')
phone=f.getvalue('phone')
age=f.getvalue('age')
passw=f.getvalue('pwd')
cpassw=f.getvalue('Cpwd')
remember=f.getvalue('remember')

if passw==cpassw:
    signup = pymysql.Connect(host="127.0.0.1", user="root", database="doc_pat")
    cursor = signup.cursor()
    cursor.execute("INSERT INTO pat_det(name, age, phone, passw) VALUES(%s, %s, %s, %s)", (name, age, phone, passw))
    signup.commit()
    print(''' 
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login Page</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link
                href="https://fonts.googleapis.com/css2?family=Delius&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap"
                rel="stylesheet">
            <style>
                * {
                    font-family: "Delius", serif;
                    font-weight: 400;
                    font-style: normal;
                    padding: 0px;
                    margin: 0px;
                    position: relative;
                    color: rgb(0, 0, 0);
                    font-weight: bold;
                }

                body {
                    background-image: url('img3.jpg');
                    background-size: cover;
                    background-repeat: no-repeat;
                    display: flex;
                    flex-direction: row;
                    justify-content: center;
                }

                .loginpage {
                    /* background-color: rgb(255, 224, 251);
                    background-position: center; */
                    width: 800px;
                    height: 500px;
                    margin-top: 50px;
                    border-radius: 20px;
                    border-color: rgb(255, 192, 203);
                    background: transparent;
                    border-style: solid;
                    display: flex;
                    flex-direction: column;
                    backdrop-filter: blur(15px);

                }

                img {
                    left: 360px;
                    top: 80px;
                    backdrop-filter: blur(0);

                }

                .allinputs {
                    bottom: 230px;
                    margin: 10px;
                    left: 20px;
                }

                .allinputs h1 {
                    left: 75px;
                    margin-bottom: 50px;
                }

                .inputs {
                    margin-top: 10px;
                    margin-left: 20px;
                    font-size: 15px;
                    margin-top: 30px;
                }

                .inputs input {
                    width: 200px;
                    height: 25px;
                    border-radius: 13px;
                    padding: 2px;
                    background: transparent;
                }

                .butt input {
                    width: 210px;
                    height: 35px;
                    background-color: pink;
                    border-radius: 10px;
                    left: 20px;
                    margin-top: 20px;
                }

                .butt input:hover {
                    background-color: palevioletred;
                }

                .signuplink p {
                    font-size: 12px;
                    display: flex;
                    left: 50px;
                }

                .signuplink a {
                    display: flex;
                    left: 100px;
                }
                .forget a{
                    left:65px ;
                }
            </style>
        </head>

        <body>
          <form action="secondpage.py" method="post">
                <div class="loginpage">
                    <img src="kk.png" alt="description" width="430px" height="400px">
                    <div class="allinputs">
                        <h1>Login</h1>

                        <div class="inputs">
                            Phone No<br><input type="mail" name="Lphone" placeholder="Phone No">
                        </div>

                        <div class="inputs">
                            Password<br><input type="password" name="Lpwd" placeholder="Password">
                        </div>

                        <br>
                        <div class="butt">
                            <input type="submit" value=" Login">
                        </div>
                        <div class="signuplink">
                            <p>If already haven't an account</p>
                            <a href="signup.html">Signup</a>
                            <br>
                        </div>
                        <div class="forget">
                            <a href="#">Forget Password</a>
                        </div>
                    </div>
                </div>
            </form>
        </body>

        </html> ''')

else:
    print("not found")




