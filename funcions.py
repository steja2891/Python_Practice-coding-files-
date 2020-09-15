def para(string):
    str = "my name is sai, sai is 20 years old. sai used to wake up early in the "
    "morning. sai always used time effectively to learn new things"
    if "sai" in str:
        print(str.replace("sai",string))
        return str

para("Rohit Sharma")
para("Sachin Tendulakar")