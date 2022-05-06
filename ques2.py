Name="Abhishek Tomar"
Sid="21107007"
dept="Mechanical Engineering"
Cgpa="9.94"

info='''
Hey, ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is 9.9 '''

# string formatting
info=info.replace("ABC",Name)
info=info.replace("2110XXXX",Sid)
info=info.replace("XYZ",dept)
info=info.replace("9.9",Cgpa)

print(info)